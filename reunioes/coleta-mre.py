from bs4 import BeautifulSoup
import requests
import os
from time import sleep
import random
import csv

# --- Configuração do CSV ---
DATA_DIR = '/home/labri_natannoronha/codigo/Fundamento/dados'

# Cria a pasta de dados se ela não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CSV_FILE = os.path.join(DATA_DIR, 'mre_notas.csv')
CSV_HEADER = ['Título', 'Link', 'Data', 'Ano', 'Horário', 'Número da Nota', 'Categoria']

# Cria o arquivo CSV e escreve o cabeçalho se ele não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)

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
        sleep(random.uniform(0.5, 1.5))
        html = requests.get(url, headers=headers)
        html.raise_for_status()
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
        writer.writerow([nota['Título'], nota['Link'], nota['Data'], nota['Ano'], nota['Horário'], nota['Número da Nota'], nota['Categoria']])

# Função para extrair informações de uma página
def extrair_infos_pagina(url):
    """
    Extrai informações de uma página de notas à imprensa.

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
                    nota_ano = partes[1] # Captura o ano da nota para comparação
                else:
                    numero_da_nota = numero_da_nota.split('/')[0] 
                    nota_ano = "Ano não encontrado" # Atribui "Ano não encontrado" para comparação posterior se o ano da nota é invalido
        else:
            numero_da_nota = "N/A"
            nota_ano = "Ano não encontrado"

        titulo_element = conteudo.find('h2', class_='titulo')
        titulo = titulo_element.text.strip() if titulo_element else "Título não encontrado"

        link_element = conteudo.find('a')
        link = link_element['href'].strip() if link_element else "#"

        data_element = conteudo.find('span', class_='data')
        data = data_element.text.strip() if data_element else "Data não encontrada"
        
        # Extrai o ano da string de data, priorizando a data
        try:
            ano = data.split('/')[-1]
            if not ano.isdigit() or len(ano) != 4:
                print(f"Ano inválido na data: {ano}.")
                ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"
        except IndexError:
            print(f"Erro ao extrair o ano da data: {data}")
            ano = nota_ano if nota_ano != "Ano não encontrado" else "Ano não encontrado"

        horario = ""

        # Acessa a página da nota individual
        artigo, artigo_http_code = acessar_pagina(link)
        if artigo is None:
            print(f"Não foi possível acessar a página da nota: {link}. Seguindo para próxima nota")
            continue

        # Extração dos parágrafos (mantida no código, mas não salva no CSV)
        paragrafos_element = artigo.find('div', property='rnews:articleBody')
        paragrafos_temp = [p.text.strip() for p in paragrafos_element.find_all('p')] if paragrafos_element else []

        categorias_element = artigo.find('div', class_='contenttree-widget relationchoice-field')
        categorias = categorias_element.text.strip() if categorias_element else "Sem categoria"

        # Dicionário para armazenar os dados da nota
        nota = {
            'Título': titulo,
            'Link': link,
            'Data': data,
            'Ano': ano,
            'Horário': horario,
            'Número da Nota': numero_da_nota,
            'Categoria': categorias,
            'Parágrafos': paragrafos_temp
        }

        # Salva os dados no CSV (sem os parágrafos)
        salvar_dados(nota)

        # Impressão das informações para verificação (opcional)
        print('-' * 100)
        print('Título:', titulo)
        print('Link:', link)
        print('Data:', data)
        print('Ano:', ano)
        print('Horário:', horario)
        print('Número da Nota:', numero_da_nota)
        print('Categoria:', categorias)
        print('-' * 100)
        sleep(1)
    return True

# Função principal para extrair informações
def extrair_infos():
    """
    Função principal que extrai informações de todas as páginas de notas à imprensa do site do Itamaraty.
    """
    base_url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int="
    max_offset = 5580

    continuar = True
    offset = 0
    while continuar and offset <= max_offset:
        url = f"{base_url}{offset}"

        continuar = extrair_infos_pagina(url)
        offset += 30
        sleep(5)  # Pausa para evitar sobrecarga (ajuste se necessário, confira o robots.txt)

def main():
    extrair_infos()

if __name__ == '__main__':
    main()