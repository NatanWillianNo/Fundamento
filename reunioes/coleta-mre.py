import requests
from bs4 import BeautifulSoup
import os
from time import sleep
import random
import csv
from tqdm import tqdm

# --- Configuração do CSV ---
DATA_DIR = '/home/labri_natannoronha/codigo/Fundamento/dados'  # Substitua pelo seu diretório

# Cria a pasta de dados se ela não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CSV_FILE = os.path.join(DATA_DIR, 'mre_notas.csv')
CSV_HEADER = ['TÍTULO DA TABELA', 'TÍTULO DA NOTA', 'LINK', 'DATA DE PUBLICAÇÃO', 'HORÁRIO DE PUBLICAÇÃO', 'DATA DE ATUALIZAÇÃO', 'HORÁRIO DE ATUALIZAÇÃO', 'ANO', 'MÊS', 'NÚMERO DA NOTA', 'CATEGORIA']

# --- Função para acessar uma página web e retornar o HTML e o código de status HTTP ---
def acessar_pagina(url, tentativas=5, intervalo=15):
    """
    Acessa uma página web e retorna o objeto BeautifulSoup e o código de status HTTP.
    Implementa retentativas em caso de erro 503 (Backend fetch failed).

    Args:
        url: A URL da página a ser acessada.
        tentativas: O número máximo de tentativas de acesso (padrão: 5).
        intervalo: O tempo de espera em segundos entre cada tentativa (padrão: 15).

    Returns:
        Um par (bs, http_code) onde bs é o objeto BeautifulSoup e http_code é o código de status HTTP.
        Retorna (None, None) em caso de erro após todas as tentativas.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    for tentativa in range(1, tentativas + 1):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lança uma exceção para erros HTTP
            bs = BeautifulSoup(response.text, 'html.parser')
            return bs, response.status_code
        except requests.exceptions.RequestException as e:
            if '503' in str(e):
                print(f"Erro 503 ao acessar a página: {e}")
                if tentativa < tentativas:
                    print(f"Tentativa {tentativa + 1}/{tentativas} após {intervalo} segundos...")
                    sleep(intervalo)
                else:
                    print(f"Falha ao acessar a página após {tentativas} tentativas.")
            else:
                print(f"Erro ao acessar a página: {e}")
                break
    return None, None

# --- Função para adicionar dados ao CSV ---
def salvar_dados(nota):
    """
    Adiciona os dados de uma nota ao arquivo CSV.

    Args:
        nota: Um dicionário contendo os dados da nota.
    """
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Notas à Imprensa - Itamaraty', nota['Título'], nota['Link'], nota['Data Publicação'], nota['Horário Publicação'], nota['Data Atualização'], nota['Horário Atualização'], nota['Ano'], nota['Mês'], nota['Número da Nota'], nota['Categoria']])

# --- Função para extrair informações de uma página ---
def extrair_infos_pagina(url):
    """
    Extrai informações de uma página de notas à imprensa.

    Args:
        url: A URL da página a ser extraída.

    Returns:
        True se a extração for bem-sucedida, False caso contrário.
    """
    print(f"Extraindo informações de: {url}")
    try:
        bs, http_code = acessar_pagina(url)
        if bs is None:
            print(f"Erro ao acessar a página: {url}. Status Code: {http_code}")
            return False

        # Tenta encontrar a lista de artigos usando a abordagem original
        lista_tag_article = bs.find('ul', class_='noticias listagem-noticias-com-foto')

        # Se a abordagem original não funcionar, use uma abordagem alternativa
        if lista_tag_article is None:
            print(f"A abordagem original não encontrou a lista de artigos. Usando abordagem alternativa para {url}.")
            lista_tag_article = bs.find('ul', class_='noticias')  # Adicionando uma classe alternativa

        # Se ainda assim não encontrar nada, retorna False
        if lista_tag_article is None:
            print(f"Nenhuma lista de artigos encontrada na página: {url}.")
            return False

        articles = lista_tag_article.find_all('li')

        # Verifica se a lista de artigos está vazia (última página)
        if not articles:
            print("Última página alcançada ou página sem artigos.")
            return False

        for tag_article in articles:
            conteudo = tag_article.find('div', class_='conteudo')
            if conteudo is None:
                print("Elemento 'conteudo' não encontrado. Seguindo para próxima nota.")
                continue

            numero_da_nota_element = conteudo.find('div', class_='subtitulo-noticia')
            if numero_da_nota_element:
                numero_da_nota_raw = numero_da_nota_element.text.strip().lower()

                # Tratamento para diferentes formatos de número da nota
                if 'nota à imprensa n°' in numero_da_nota_raw:
                    numero_da_nota = numero_da_nota_raw.split('nota à imprensa n°')[-1].strip()
                elif 'nota à imprensa nº' in numero_da_nota_raw:
                    numero_da_nota = numero_da_nota_raw.split('nota à imprensa nº')[-1].strip()
                elif 'nota' in numero_da_nota_raw:
                    numero_da_nota = numero_da_nota_raw.split('nota')[-1].replace('nº', '').replace('n°', '').strip()
                else:
                    numero_da_nota = "N/A"

                # Separa número e ano se estiverem no formato "630/2008"
                if '/' in numero_da_nota:
                    partes = numero_da_nota.split('/')
                    if len(partes) == 2 and partes[1].isdigit() and len(partes[1]) == 4:
                        numero_da_nota = partes[0]  # Pega apenas a parte numérica
                        nota_ano = partes[1]
                    else:
                        numero_da_nota = numero_da_nota.split('/')[0]
                        nota_ano = "Ano não encontrado"
                else:
                    nota_ano = "Ano não encontrado"  # Define nota_ano aqui se não houver '/'
            else:
                numero_da_nota = "N/A"
                nota_ano = "Ano não encontrado"

            titulo_element = conteudo.find('h2', class_='titulo')
            titulo = titulo_element.text.strip() if titulo_element else "Título não encontrado"

            link_element = conteudo.find('a')
            link = link_element['href'].strip() if link_element else "#"
            
            # Modificação para corrigir o link
            if not link.startswith('http'):
                link = f"https://www.gov.br{link}"

            # Acessa a página da nota individual
            artigo, artigo_http_code = acessar_pagina(link)
            if artigo is None:
                print(f"Não foi possível acessar a página da nota: {link}. Seguindo para próxima nota")
                continue

            # Extrai as datas e horários de publicação e atualização do 'documentByLine'
            document_byline = artigo.find('div', class_='documentByLine')

            # Extrai data e horário de publicação
            publicado_em_element = document_byline.find('span', class_='documentPublished') if document_byline else None
            if publicado_em_element:
                publicado_em_value = publicado_em_element.find('span', class_='value')
                publicado_em = publicado_em_value.text.strip() if publicado_em_value else "Publicação não encontrada"
            else:
                publicado_em = "Publicação não encontrada"

            # Extrai data e horário de atualização
            atualizado_em_element = document_byline.find('span', class_='documentModified') if document_byline else None
            if atualizado_em_element:
                atualizado_em_value = atualizado_em_element.find('span', class_='value')
                atualizado_em = atualizado_em_value.text.strip() if atualizado_em_value else "Atualização não encontrada"
            else:
                atualizado_em = "Atualização não encontrada"

            # Separa data e horário de publicação
            if publicado_em != "Publicação não encontrada":
                try:
                    data_publicacao, horario_publicacao = publicado_em.split()
                except ValueError:
                    print(f"Erro ao separar data e horário de publicação: {publicado_em}")
                    data_publicacao, horario_publicacao = publicado_em, ""
            else:
                data_publicacao, horario_publicacao = "Data não disponível", "Horário não disponível"

            # Separa data e horário de atualização
            if atualizado_em != "Atualização não encontrada":
                try:
                    data_atualizacao, horario_atualizacao = atualizado_em.split()
                except ValueError:
                    print(f"Erro ao separar data e horário de atualização: {atualizado_em}")
                    data_atualizacao, horario_atualizacao = atualizado_em, ""
            else:
                data_atualizacao, horario_atualizacao = "Data não disponível", "Horário não disponível"

            # Extrai o ano e mês da string de data de publicação
            meses = {
                '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
                '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
                '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
            }
            if data_publicacao != "Data não disponível":
                try:
                    dia, mes, ano = data_publicacao.split('/')
                    ano = ano[:4]  # Garante que o ano tenha 4 dígitos
                    if not ano.isdigit() or len(ano) != 4:
                        print(f"Ano inválido na data de publicação: {ano}.")
                        ano = nota_ano  # Usa nota_ano aqui
                    else:
                        ano = ano
                    if nota_ano == "Ano não encontrado":
                        nota_ano = ano
                except (ValueError, IndexError):
                    print(f"Erro ao extrair o ano ou mês da data de publicação: {data_publicacao}")
                    ano = nota_ano  # Usa nota_ano em caso de erro
                    mes = "Mês não encontrado"
            else:
                ano = nota_ano  # Usa nota_ano se a data de publicação não estiver disponível
                mes = "Mês não encontrado"
            
            mes_nome = meses.get(mes, "Mês inválido")

            # Extração dos parágrafos (NÃO utilizada no CSV)
            paragrafos_element = artigo.find('div', property='rnews:articleBody')
            paragrafos_temp = [p.text.strip() for p in paragrafos_element.find_all('p')] if paragrafos_element else []

            categorias_element = artigo.find('div', class_='contenttree-widget relationchoice-field')
            categorias = categorias_element.text.strip() if categorias_element else "Sem categoria"

            # --- Dicionário para armazenar os dados da nota ---
            nota = {
                'Título': titulo,
                'Link': link,
                'Data Publicação': data_publicacao,
                'Horário Publicação': horario_publicacao,
                'Data Atualização': data_atualizacao,
                'Horário Atualização': horario_atualizacao,
                'Ano': ano,
                'Mês': mes_nome,
                'Número da Nota': numero_da_nota,
                'Categoria': categorias,
                'Parágrafos': paragrafos_temp  # Não será salvo no CSV
            }

            # --- Salva os dados no CSV ---
            salvar_dados(nota)

            # --- Impressão das informações para verificação ---
            print('-' * 100)
            print('Título:', titulo)
            print('Link:', link)
            print('Data Publicação:', data_publicacao)
            print('Horário Publicação:', horario_publicacao)
            print('Data Atualização:', data_atualizacao)
            print('Horário Atualização:', horario_atualizacao)
            print('Ano:', ano)
            print('Mês:', mes_nome)
            print('Número da Nota:', numero_da_nota)
            print('Categoria:', categorias)
            print('-' * 100)

        return True
    except Exception as e:
        print(f"Erro ao processar a página {url}: {e}")
        return False

#Nova função para encontrar a última página
def encontrar_ultima_pagina():
    """
    Encontra o número da última página de notas à imprensa no site do Itamaraty.

    Args:
        session: A sessão aiohttp a ser usada para acessar a página.

    Returns:
        O número da última página ou None se não for encontrado.
    """
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=0"
    try:
        bs, _ = acessar_pagina(url)
        if bs:
            elemento_paginacao = bs.find('ul', class_='paginacao listingBar')
            if elemento_paginacao:
                links_paginas = elemento_paginacao.find_all('a', class_='pagina')
                if links_paginas:
                    ultimo_link = links_paginas[-1]
                    numero_ultima_pagina = int(ultimo_link.get_text())
                    return numero_ultima_pagina * 30 # Cada página tem 30 itens
        return None
    except Exception as e:
        print(f"Erro ao encontrar a última página: {e}")
        return None

def extrair_paginas(max_offset):
    """
    Função para gerenciar a extração de múltiplas páginas.

    Agora, a extração é feita de trás para frente, começando da última página e indo em direção à primeira.

    Args:
        max_offset: O offset máximo para a paginação (número da última página).
    """
    base_url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    
    # Itera de trás para frente, diminuindo o offset em 30 a cada iteração
    for offset in tqdm(range(max_offset, -1, -30), desc="Extraindo páginas"):
        url = f"{base_url}{offset}"
        extrair_infos_pagina(url)
        sleep(random.uniform(1, 5))

def extrair_infos():
    """
    Função principal para extrair informações de todas as páginas de notas à imprensa do site do Itamaraty.
    """
    max_offset = encontrar_ultima_pagina()
    if max_offset is None:
        print("Não foi possível encontrar a última página. Usando valor padrão.")
        max_offset = 5700  # Valor padrão, ajuste se necessário
    extrair_paginas(max_offset)

# --- Função principal (main) ---
def main():
    """
    Função principal do script.
    Apaga o arquivo CSV anterior e cria um novo com o cabeçalho, e então inicia a extração de dados.
    """
    # Apaga o arquivo CSV anterior, se existir
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)
    # Cria um novo arquivo CSV e escreve o cabeçalho
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)

    # Inicia a extração de informações das páginas do Itamaraty
    extrair_infos()

# Executa o script
if __name__ == '__main__':
    main()