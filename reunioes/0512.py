from tinydb import TinyDB, Query
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import os

# Listas para armazenar informações extraídas
titulo_lista = []
link_lista = []
data_lista = []
horario_lista = []
numero_da_nota_lista = []
categoria_lista = []

# Função para acessar uma página web e retornar o HTML e o código de status HTTP
def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    http_code = html.status_code
    return bs, http_code

#TODO Extrair data, horário e número da nota, parágrafos, categorias (OBS: Colocar com tag)
#TODO Atualizar o banco com as informações acima 

# Função para extrair informações de um artigo
def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    http_code = html.status_code
    return bs, http_code

# URL da página de onde as informações serão extraídas
def extrair_infos():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=30"
    bs = acessar_pagina(url)[0]
    lista_tag_article = bs.find('div', attrs={'id': 'content-core'}).find_all('article', attrs={'class': 'tileItem visualIEFloatFix tile-collective-nitf-content'})
    for tag_article in lista_tag_article:
        titulo = tag_article.h2.text.strip()
        titulo_lista.append(titulo)
        
        link = tag_article.h2.a['href'].strip()
        link_lista.append(link)
        
        data = tag_article.find('i', class_='icon-day').parent.text.strip()
        data_lista.append(data)
        
        horario = tag_article.find('i', class_='icon-hour').parent.text.strip()
        horario_lista.append(horario)
        
        numero_da_nota = tag_article.find('span', class_='subtitle').text.strip().replace('NOTA À IMPRENSA ', '')
        numero_da_nota_lista.append(horario)
        
        artigo = acessar_pagina(link)
        paragrafos = artigo[0].find('div', property='rnews:articleBody')
        lista_paragrafos = paragrafos.find_all('p')
        paragrafos_lista = []
        for p in lista_paragrafos:
            p = p.text.strip()
            paragrafos_lista.append(p)
        
        categorias = artigo[0].find('div', class_='contenttree-widget relationchoice-field').text
        categoria_lista.append(categorias)
        
        # Impressão das informações para verificação
        print('Título:', titulo)
        print('Link:', link)
        print('Data:', data)
        print('Horário:', horario)
        print('Número da Nota:', numero_da_nota)
        print('Parágrafo:', paragrafos_lista)
        print('Categoria:', categorias)
        print('-' * 40)

# Função para criar o ambiente virtual
def criar_ambiente_virtual():
    env_dir = load_dotenv('.env_dir')
    DIR_DADOS_FINAL = os.getenv('DIR_DADOS_FINAL')
    os.makedirs(DIR_DADOS_FINAL, exist_ok=True)
    print(f"Ambiente virtual criado em {DIR_DADOS_FINAL}")


# Função para inserir informações na base de dados
def inserir_bd(titulo, link, data, horario, numero_da_nota, categorias, paragrafos_lista): 
    # Criação ou abertura do arquivo de base de dados
    bd = TinyDB(f'{DIR_DADOS_FINAL}/coleta.json', indent=4, ensure_ascii=False)
    buscar = Query()
    verificar_bd = bd.contains(buscar.link == link)
    
    # Verifica se o link já está na base de dados
    if not verificar_bd:
        # Insere as informações na base de dados
        bd.insert({
            'título': titulo,
            'link': link,
            'data': data,
            'horario': horario,
            'numero_da_nota': numero_da_nota,
            'categorias': categorias,
            'paragrafos_lista': paragrafos_lista
        })
    else:
        print('Já está na base!')

def main():
    extrair_infos()
    inserir_bd()

if __name__ == '__main__':
    main()
