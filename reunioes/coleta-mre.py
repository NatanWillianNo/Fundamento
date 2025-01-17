from bs4 import BeautifulSoup  # Biblioteca para analisar HTML e XML
import requests  # Biblioteca para fazer requisições HTTP
import os  # Módulo para interagir com o sistema operacional
from time import sleep  # Função para pausar a execução
import random  # Módulo para geração de números aleatórios
import csv  # Módulo para trabalhar com arquivos CSV

# --- Configuração do CSV ---

# Caminho para o diretório onde os dados serão armazenados
DATA_DIR = '/home/labri_natannoronha/codigo/Fundamento/dados'  # Substitua pelo seu diretório

# Cria a pasta de dados se ela não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Caminho completo para o arquivo CSV onde os dados serão salvos
CSV_FILE = os.path.join(DATA_DIR, 'mre_notas.csv')

# Cabeçalho do arquivo CSV (nomes das colunas)
CSV_HEADER = [
    'TÍTULO DA TABELA',
    'TÍTULO DA NOTA',
    'LINK',
    'DATA DE PUBLICAÇÃO',
    'HORÁRIO DE PUBLICAÇÃO',
    'DATA DE ATUALIZAÇÃO',
    'HORÁRIO DE ATUALIZAÇÃO',
    'ANO',
    'MÊS',
    'NÚMERO DA NOTA',
    'CATEGORIA'
]

# --- Função para acessar uma página web e retornar o HTML e o código de status HTTP ---

def acessar_pagina(url):
    """
    Acessa uma página web e retorna o objeto BeautifulSoup correspondente e o código de status HTTP.

    Args:
        url: A URL da página a ser acessada.

    Returns:
        Um par (bs, http_code) onde bs é o objeto BeautifulSoup (representação analisada do HTML)
        e http_code é o código de status HTTP da resposta.
        Retorna (None, None) em caso de erro na requisição.
    """
    # Define o cabeçalho User-Agent para simular um navegador real e evitar bloqueios
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    try:
        # Pausa a execução por um tempo aleatório entre 0.5 e 1.5 segundos para evitar sobrecarga no servidor
        sleep(random.uniform(0.5, 1.5))

        # Faz a requisição GET para a URL especificada, com o cabeçalho definido
        html = requests.get(url, headers=headers)

        # Lança uma exceção se o código de status da resposta for um erro (4xx ou 5xx)
        html.raise_for_status()

        # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
        bs = BeautifulSoup(html.text, 'html.parser')

        # Obtém o código de status HTTP da resposta
        http_code = html.status_code

        # Retorna o objeto BeautifulSoup e o código de status
        return bs, http_code

    except requests.exceptions.RequestException as e:
        # Em caso de erro na requisição (ex: conexão, timeout), imprime uma mensagem de erro
        print(f"Erro ao acessar a página: {e}")
        # Retorna None, None para indicar que houve um erro
        return None, None

# --- Função para adicionar dados ao CSV ---

def salvar_dados(nota):
    """
    Adiciona os dados de uma nota (representada como um dicionário) ao arquivo CSV.

    Args:
        nota: Um dicionário contendo os dados da nota, com chaves correspondendo aos nomes das colunas no CSV.
    """
    # Abre o arquivo CSV em modo de anexação ('a'), com codificação UTF-8 e newline='' para evitar linhas em branco extras
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        # Cria um objeto writer para escrever dados no formato CSV
        writer = csv.writer(f)

        # Escreve uma linha no CSV com os dados da nota, precedidos pelo título "Notas à Imprensa - Itamaraty"
        writer.writerow([
            'Notas à Imprensa - Itamaraty',
            nota['Título'],
            nota['Link'],
            nota['Data Publicação'],
            nota['Horário Publicação'],
            nota['Data Atualização'],
            nota['Horário Atualização'],
            nota['Ano'],
            nota['Mês'],
            nota['Número da Nota'],
            nota['Categoria']
        ])

# --- Função para extrair informações de uma página ---

def extrair_infos_pagina(url):
    """
    Extrai informações de uma página de notas à imprensa do site do Itamaraty.

    Args:
        url: A URL da página a ser extraída.

    Returns:
        True se a extração for bem-sucedida (ou seja, se a página for acessada e contiver notas).
        False caso contrário (se a página não for acessada ou se for a última página/não contiver notas).
    """
    print(f"Extraindo informações de: {url}")

    # Acessa a página usando a função acessar_pagina
    bs, http_code = acessar_pagina(url)

    # Se a página não for acessada (bs é None), retorna False
    if bs is None:
        return False

    # Encontra a lista de notas à imprensa na página
    # A lista é uma tag <ul> com a classe 'noticias listagem-noticias-com-foto'
    # Cada nota é uma tag <li> dentro dessa lista
    lista_tag_article = bs.find('ul', class_='noticias listagem-noticias-com-foto').find_all('li')

    # Verifica se a lista de artigos está vazia.
    # Isso indica que é a última página ou que a página não contém artigos.
    if not lista_tag_article:
        print("Última página alcançada ou página sem artigos.")
        return False

    # Itera sobre cada nota na lista
    for tag_article in lista_tag_article:
        # Encontra o elemento div com a classe 'conteudo', que contém as informações da nota
        conteudo = tag_article.find('div', class_='conteudo')

        # Se o elemento 'conteudo' não for encontrado, pula para a próxima nota
        if conteudo is None:
            print("Elemento 'conteudo' não encontrado. Seguindo para próxima nota.")
            continue

        # --- Extração do número da nota ---

        # Encontra o elemento div com a classe 'subtitulo-noticia', que contém o número da nota
        numero_da_nota_element = conteudo.find('div', class_='subtitulo-noticia')

        # Se o número da nota for encontrado
        if numero_da_nota_element:
            # Extrai o texto do elemento, converte para minúsculas e remove espaços em branco
            numero_da_nota_raw = numero_da_nota_element.text.strip().lower()

            # Tratamento para diferentes formatos de número da nota
            if 'nota à imprensa n°' in numero_da_nota_raw:
                # Extrai o número da nota do texto que está após 'nota à imprensa n°'
                numero_da_nota = numero_da_nota_raw.split('nota à imprensa n°')[-1].strip()
            elif 'nota à imprensa nº' in numero_da_nota_raw:
                # Extrai o número da nota do texto que está após 'nota à imprensa nº'
                numero_da_nota = numero_da_nota_raw.split('nota à imprensa nº')[-1].strip()
            elif 'nota' in numero_da_nota_raw:
                # Extrai o número da nota do texto que está após 'nota' e remove 'nº' e 'n°'
                numero_da_nota = numero_da_nota_raw.split('nota')[-1].replace('nº', '').replace('n°', '').strip()
            else:
                # Se o formato for desconhecido, define o número da nota como "N/A"
                numero_da_nota = "N/A"

            # Separa número e ano se estiverem no formato "630/2008"
            if '/' in numero_da_nota:
                partes = numero_da_nota.split('/')
                # Se o número da nota estiver no formato número/ano (ex: 630/2008)
                if len(partes) == 2 and partes[1].isdigit() and len(partes[1]) == 4:
                    numero_da_nota = partes[0]  # Pega apenas a parte numérica
                    nota_ano = partes[1]  # Pega o ano
                else:
                    # Se não estiver nesse formato, pega apenas o primeiro número
                    numero_da_nota = numero_da_nota.split('/')[0]
                    nota_ano = "Ano não encontrado"
        else:
            # Se o elemento com o número da nota não for encontrado, define como "N/A"
            numero_da_nota = "N/A"
            nota_ano = "Ano não encontrado"

        # --- Extração do título ---

        # Encontra o elemento <h2> com a classe 'titulo', que contém o título da nota
        titulo_element = conteudo.find('h2', class_='titulo')
        # Extrai o texto do título e remove espaços em branco extras
        titulo = titulo_element.text.strip() if titulo_element else "Título não encontrado"

        # --- Extração do link ---

        # Encontra a tag <a>, que contém o link para a nota completa
        link_element = conteudo.find('a')
        # Extrai o atributo 'href', que contém o link, e remove espaços em branco extras
        link = link_element['href'].strip() if link_element else "#"

        # --- Acesso à página individual da nota ---

        # Acessa a página da nota individual usando a função acessar_pagina e o link extraído
        artigo, artigo_http_code = acessar_pagina(link)
        # Se a página da nota não for acessada (artigo é None), pula para a próxima nota
        if artigo is None:
            print(f"Não foi possível acessar a página da nota: {link}. Seguindo para próxima nota")
            continue

        # --- Extração das datas e horários de publicação e atualização ---

        # Encontra o elemento div com a classe 'documentByLine', que contém as informações de publicação e atualização
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
        try:
            # Tenta dividir a string de publicação em data e horário usando espaço como delimitador
            data_publicacao, horario_publicacao = publicado_em.split(" ")
        except ValueError:
            # Se a separação falhar (por exemplo, se não houver espaço), imprime uma mensagem de erro
            print(f"Erro ao separar data e horário de publicação: {publicado_em}")
            # Define data_publicacao como a string original e horario_publicacao como uma string vazia
            data_publicacao, horario_publicacao = publicado_em, ""

        # Separa data e horário de atualização
        try:
            # Tenta dividir a string de atualização em data e horário usando espaço como delimitador
            data_atualizacao, horario_atualizacao = atualizado_em.split(" ")
        except ValueError:
            # Se a separação falhar, imprime uma mensagem de erro
            print(f"Erro ao separar data e horário de atualização: {atualizado_em}")
            # Define data_atualizacao como a string original e horario_atualizacao como uma string vazia
            data_atualizacao, horario_atualizacao = atualizado_em, ""

        # --- Extração do ano e mês ---

        # Extrai o ano e mês da string de data de publicação
        try:
            # Tenta dividir a data de publicação em dia, mês e ano usando '/' como delimitador
            dia, mes, ano = data_publicacao.split('/')
            ano = ano[:4]  # Garante que o ano tenha 4 dígitos
            # Verifica se o ano é um número válido de 4 dígitos
            if not ano.isdigit() or len(ano) != 4:
                print(f"Ano inválido na data de publicação: {ano}.")
                # Usa o ano extraído anteriormente do número da nota, se disponível
                ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"
        except (ValueError, IndexError):
            # Se a extração falhar (por exemplo, se a data não estiver no formato esperado), imprime uma mensagem de erro
            print(f"Erro ao extrair o ano ou mês da data de publicação: {data_publicacao}")
            # Usa o ano extraído anteriormente do número da nota, se disponível
            ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"
            mes = "Mês não encontrado"

        # Mapeamento de meses: converte o número do mês para o nome por extenso
        meses = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
        }
        # Obtém o nome do mês a partir do dicionário meses. Se o número do mês não estiver no dicionário, retorna "Mês inválido"
        mes_nome = meses.get(mes, "Mês inválido")

        # --- Extração dos parágrafos (NÃO utilizada no CSV) ---

        # Encontra o elemento div com a propriedade 'rnews:articleBody', que contém os parágrafos da nota
        paragrafos_element = artigo.find('div', property='rnews:articleBody')
        # Extrai o texto de cada parágrafo (<p>) dentro do elemento e remove espaços em branco extras
        paragrafos_temp = [p.text.strip() for p in paragrafos_element.find_all('p')] if paragrafos_element else []

        # --- Extração das categorias ---

        # Encontra o elemento div com a classe 'contenttree-widget relationchoice-field', que contém as categorias
        categorias_element = artigo.find('div', class_='contenttree-widget relationchoice-field')
        # Extrai o texto das categorias e remove espaços em branco extras
        categorias = categorias_element.text.strip() if categorias_element else "Sem categoria"

        # --- Dicionário para armazenar os dados da nota ---

        # Cria um dicionário para armazenar as informações extraídas da nota
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
            'Parágrafos': paragrafos_temp  # Lista de parágrafos (não será salva no CSV)
        }

        # --- Salva os dados no CSV ---

        # Chama a função salvar_dados para salvar as informações da nota no arquivo CSV
        salvar_dados(nota)

        # --- Impressão das informações para verificação ---
        # (Opcional) Imprime as informações extraídas para fins de depuração e verificação
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

        # Pausa a execução por 1 segundo para evitar sobrecarga
        sleep(1)

    # Retorna True para indicar que a extração da página foi bem-sucedida
    return True

# --- Função principal para extrair informações ---

def extrair_infos():
    """
    Função principal que extrai informações de todas as páginas de notas à imprensa do site do Itamaraty.
    Itera sobre as páginas, chama a função extrair_infos_pagina para cada página e salva os dados no CSV.
    """
    # URL base para a listagem de notas à imprensa
    base_url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="

    # Número máximo de itens a serem buscados (ajuste conforme necessário)
    # **VERIFIQUE** esse número no site, ele pode mudar!
    max_offset = 5580

    # Variável para controlar o loop (continua até que a última página seja alcançada)
    continuar = True
    # Deslocamento inicial (offset) para a paginação
    offset = 0

    # Loop principal: continua até que a última página seja alcançada ou o max_offset seja atingido
    while continuar and offset <= max_offset:
        # Monta a URL completa da página atual, com base no offset
        url = f"{base_url}{offset}"

        # Extrai as informações da página atual
        continuar = extrair_infos_pagina(url)

        # Incrementa o offset em 30 para a próxima página (cada página tem 30 itens)
        offset += 30

        # Pausa a execução por 5 segundos para evitar sobrecarga (ajuste se necessário e confira o robots.txt)
        sleep(5)

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

# --- Execução do script ---

# Executa a função main() quando o script é executado diretamente
if __name__ == '__main__':
    main()