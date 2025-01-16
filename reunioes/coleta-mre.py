from bs4 import BeautifulSoup
import requests
import os
from time import sleep
import random
import csv

# --- Configuração do CSV ---
DATA_DIR = '/home/labri_natannoronha/codigo/Fundamento/dados'
"""
Diretório onde os dados extraídos serão armazenados.
"""

# Cria a pasta de dados se ela não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CSV_FILE = os.path.join(DATA_DIR, 'mre_notas.csv')
"""
Caminho completo do arquivo CSV onde os dados serão salvos.
"""

CSV_HEADER = ['TÍTULO DA TABELA', 'TÍTULO DA NOTA', 'LINK', 'DATA DE PUBLICAÇÃO', 'HORÁRIO DE PUBLICAÇÃO', 'DATA DE ATUALIZAÇÃO', 'HORÁRIO DE ATUALIZAÇÃO', 'ANO', 'MÊS', 'NÚMERO DA NOTA', 'CATEGORIA']
"""
Lista com os nomes das colunas do cabeçalho do CSV.
"""

# Dicionário para mapear número do mês para nome do mês
MESES = {
    '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho',
    '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
}
"""
Dicionário para mapear os números dos meses para seus respectivos nomes por extenso.
"""

# --- Cabeçalho Fixo ---
CABECALHO_FIXO = {
    'TÍTULO DA TABELA': 'Notas à Imprensa - Itamaraty',
    'TÍTULO DA NOTA': 'Título da Nota',
    'LINK': 'Link para a Nota',
    'DATA DE PUBLICAÇÃO': 'Data de Publicação',
    'HORÁRIO DE PUBLICAÇÃO': 'Horário de Publicação',
    'DATA DE ATUALIZAÇÃO': 'Data de Atualização',
    'HORÁRIO DE ATUALIZAÇÃO': 'Horário de Atualização',
    'ANO': 'Ano',
    'MÊS': 'Mês',
    'NÚMERO DA NOTA': 'Número da Nota',
    'CATEGORIA': 'Categoria'
}
"""
Dicionário contendo informações fixas para o cabeçalho do CSV, incluindo descrições das colunas.
"""

# Cria o arquivo CSV e escreve o cabeçalho se ele não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CABECALHO_FIXO.values())

# Função para acessar uma página web e retornar o HTML e o código de status HTTP
def acessar_pagina(url):
    """
    Acessa uma página web e retorna o objeto BeautifulSoup correspondente e o código de status HTTP.

    Args:
        url: A URL da página a ser acessada.

    Returns:
        Um par (bs, http_code) onde bs é o objeto BeautifulSoup e http_code é o código de status HTTP.
        Retorna (None, None) em caso de erro.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    try:
        sleep(random.uniform(0.5, 1.5))  # Pausa aleatória para evitar sobrecarga
        html = requests.get(url, headers=headers)
        html.raise_for_status()  # Verifica se houve erro na requisição HTTP
        bs = BeautifulSoup(html.text, 'html.parser')
        http_code = html.status_code
        return bs, http_code
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None, None

# Função para adicionar dados ao CSV
def salvar_dados(nota):
    """
    Adiciona os dados de uma nota ao arquivo CSV.

    Args:
        nota: Um dicionário contendo os dados da nota.
    """
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([CABECALHO_FIXO['TÍTULO DA TABELA'], nota['Título'], nota['Link'], nota['Data Publicação'], nota['Horário Publicação'], nota['Data Atualização'], nota['Horário Atualização'], nota['Ano'], nota['Mês'], nota['Número da Nota'], nota['Categoria']])

# Função para extrair informações de uma página
def extrair_infos_pagina(url):
    """
    Extrai informações de uma página de notas à imprensa, incluindo título, link, datas e horários de publicação e atualização, ano, mês, número da nota e categoria.

    Args:
        url: A URL da página a ser extraída.

    Returns:
        True se a extração for bem-sucedida, False caso contrário.
    """
    print(f"Extraindo informações de: {url}")
    bs, http_code = acessar_pagina(url)
    if bs is None:
        return False

    lista_tag_article = bs.find('ul', class_='noticias listagem-noticias-com-foto').find_all('li')

    # Verifica se a lista de artigos está vazia (última página)
    if not lista_tag_article:
        print("Última página alcançada ou página sem artigos.")
        return False

    for tag_article in lista_tag_article:
        conteudo = tag_article.find('div', class_='conteudo')
        if conteudo is None:
            print("Elemento 'conteudo' não encontrado. Seguindo para próxima nota.")
            continue

        # --- Extração do Número da Nota ---
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
                    nota_ano = partes[1]  # Armazena o ano extraído da nota para possível uso posterior
                else:
                    numero_da_nota = numero_da_nota.split('/')[0]
                    nota_ano = "Ano não encontrado" #para forçar a comparação posteriormente
        else:
            numero_da_nota = "N/A"
            nota_ano = "Ano não encontrado" #para forçar a comparação posteriormente

        # --- Extração do Título ---
        titulo_element = conteudo.find('h2', class_='titulo')
        titulo = titulo_element.text.strip() if titulo_element else "Título não encontrado"

        # --- Extração do Link ---
        link_element = conteudo.find('a')
        link = link_element['href'].strip() if link_element else "#"

        # Acessa a página da nota individual
        artigo, artigo_http_code = acessar_pagina(link)
        if artigo is None:
            print(f"Não foi possível acessar a página da nota: {link}. Seguindo para próxima nota")
            continue

        # --- Extração das datas e horários de publicação e atualização ---
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
            data_publicacao, horario_publicacao = publicado_em.split(" ")
        except ValueError:
            print(f"Erro ao separar data e horário de publicação: {publicado_em}")
            data_publicacao, horario_publicacao = publicado_em, ""

        # Separa data e horário de atualização
        try:
            data_atualizacao, horario_atualizacao = atualizado_em.split(" ")
        except ValueError:
            print(f"Erro ao separar data e horário de atualização: {atualizado_em}")
            data_atualizacao, horario_atualizacao = atualizado_em, ""

        # Extrai o ano da string de data de publicação, priorizando a data
        try:
            ano = data_publicacao.split('/')[2][:4]
            if not ano.isdigit() or len(ano) != 4:
                print(f"Ano inválido na data de publicação: {ano}.")
                ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"
        except IndexError:
            print(f"Erro ao extrair o ano da data de publicação: {data_publicacao}")
            ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"

        # Extrai o mês da data de publicação
        try:
            mes_num = data_publicacao.split('/')[1]
            mes = MESES.get(mes_num, "Mês não encontrado")
        except IndexError:
            print(f"Erro ao extrair o mês da data de publicação: {data_publicacao}")
            mes = "Mês não encontrado"

        # --- Extração dos Parágrafos (mantida no código, mas não salva no CSV) ---
        paragrafos_element = artigo.find('div', property='rnews:articleBody')
        paragrafos_temp = [p.text.strip() for p in paragrafos_element.find_all('p')] if paragrafos_element else []

        # --- Extração das Categorias ---
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
            'Mês': mes,
            'Número da Nota': numero_da_nota,
            'Categoria': categorias,
            'Parágrafos': paragrafos_temp # Apenas para eventual uso futuro, não será salvo no CSV
        }

        # Salva os dados no CSV
        salvar_dados(nota)

        # Impressão das informações para verificação (opcional)
        print('-' * 100)
        print('Título:', nota['Título'])
        print('Link:', nota['Link'])
        print('Data Publicação:', nota['Data Publicação'])
        print('Horário Publicação:', nota['Horário Publicação'])
        print('Data Atualização:', nota['Data Atualização'])
        print('Horário Atualização:', nota['Horário Atualização'])
        print('Ano:', nota['Ano'])
        print('Mês:', nota['Mês'])
        print('Número da Nota:', nota['Número da Nota'])
        print('Categoria:', nota['Categoria'])
        print('-' * 100)
        sleep(1)
    return True

# Função principal para extrair informações
def extrair_infos():
    """
    Função principal que extrai informações de todas as páginas de notas à imprensa do site do Itamaraty.
    """
    base_url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    max_offset = 5580  # Última página conhecida

    continuar = True
    offset = 0
    while continuar and offset <= max_offset:
        url = f"{base_url}{offset}"

        continuar = extrair_infos_pagina(url)
        offset += 30
        sleep(5)  # Pausa para evitar sobrecarga (ajuste se necessário, confira o robots.txt)

def main():
    """
    Função principal que inicia a extração de dados.
    """
    extrair_infos()

if __name__ == '__main__':
    main()