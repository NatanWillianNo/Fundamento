# Importa a biblioteca TinyDB para trabalhar com um banco de dados NoSQL leve em formato JSON
from tinydb import TinyDB, Query

# Importa a biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env
from dotenv import load_dotenv

# Importa a biblioteca BeautifulSoup para fazer web scraping em HTML e XML de forma eficaz
from bs4 import BeautifulSoup

# Importa a biblioteca requests para enviar solicitações HTTP e receber respostas
import requests

# Importa o módulo os para interagir com funcionalidades dependentes do sistema operacional
import os

from time import sleep

# Listas para armazenar informações extraídas
titulo_lista = []
link_lista = []
data_lista = []
horario_lista = []
numero_da_nota_lista = []
categoria_lista = []
paragrafos_lista = []

# Função para acessar uma página web e retornar o HTML e o código de status HTTP
def acessar_pagina(url):
    try:
        html = requests.get(url)
        html.raise_for_status()  # Verifica se houve erro na requisição (status 4xx ou 5xx)
        bs = BeautifulSoup(html.text, 'html.parser')
        http_code = html.status_code
        return bs, http_code
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None, None

# URL da página de onde as informações serão extraídas
def extrair_infos():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=30"
    bs, http_code = acessar_pagina(url)
    if bs is None:
        return

    # Atualizado para usar a div com id 'content' que parece conter os artigos agora.
    # A classe 'tileContent' parece ser mais consistente para identificar cada nota.
    lista_tag_article = bs.find('div', attrs={'id': 'content'}).find_all('div', attrs={'class': 'tileContent'})

    for tag_article in lista_tag_article:
        # Extrai o título
        titulo_element = tag_article.find('h2', class_='tileHeadline')
        if titulo_element is None:
            print("Título não encontrado. Pulando nota.")
            continue
        titulo = titulo_element.text.strip()
        titulo_lista.append(titulo)

        # Extrai o link
        link_element = tag_article.find('a', class_='nitf-title-link')
        if link_element is None:
            print(f"Link não encontrado para o título: {titulo}. Pulando nota.")
            continue
        link = link_element['href'].strip()
        link_lista.append(link)

        # Extrai data e horário
        data_horario_element = tag_article.find('span', class_='subtitle')
        if data_horario_element is None:
            print(f"Data e horário não encontrados para o título: {titulo}. Pulando nota.")
            continue

        data_horario = data_horario_element.text.strip().split('|')
        if len(data_horario) != 2:
            print(f"Formato de data e horário inválido para o título: {titulo}. Pulando nota.")
            continue

        data = data_horario[0].strip()
        horario = data_horario[1].strip()
        data_lista.append(data)
        horario_lista.append(horario)

        # Extrai o número da nota
        try:
            numero_da_nota = data_horario_element.find_previous_sibling('span').text.strip().lower().replace('nota à imprensa', '').replace('n°', '').replace('nº', '').strip()
            numero_da_nota_lista.append(numero_da_nota)
        except:
            print(f"Número da nota não encontrado para {titulo}")
            numero_da_nota_lista.append("")
            

        # Acessa a página da nota individual
        artigo, artigo_http_code = acessar_pagina(link)
        if artigo is None:
            print(f"Não foi possível acessar a página da nota: {link}. Pulando nota.")
            continue

        # Extrai os parágrafos
        paragrafos_element = artigo.find('div', property='rnews:articleBody')
        if paragrafos_element is None:
            print(f"Corpo do artigo não encontrado para a nota: {link}. Pulando nota.")
            paragrafos_lista.append([])
            continue

        lista_paragrafos = paragrafos_element.find_all('p')
        paragrafos_temp = []
        for p in lista_paragrafos:
            paragrafo = p.text.strip()
            paragrafos_temp.append(paragrafo)
        paragrafos_lista.append(paragrafos_temp)

        # Extrai as categorias
        categorias_element = artigo.find('div', class_='contenttree-widget relationchoice-field')
        if categorias_element is None:
            print(f"Categorias não encontradas para a nota: {link}. Pulando nota.")
            categoria_lista.append([])
            continue

        categorias = categorias_element.text.strip()
        categoria_lista.append(categorias)

        # Impressão das informações para verificação
        sleep(2)
        print('-' * 100)
        print('Título:', titulo)
        print('Link:', link)
        print('Data:', data)
        print('Horário:', horario)
        print('Número da Nota:', numero_da_nota)
        print('Categoria:', categorias)
        print('Parágrafos:')
        for paragrafo in paragrafos_temp:
            print(paragrafo)
        print('-' * 100)
        sleep(1)
        print('Processando próxima nota...')
        sleep(1)
        print('Próxima nota encontrada!')

def main():
    extrair_infos()

if __name__ == '__main__':
    main()