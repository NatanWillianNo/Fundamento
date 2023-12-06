from tinydb import TinyDB, Query
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import os

def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text,'html.parser')
    http_code = html.status_code
    return bs, http_code

def extrair_infos():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=30"
    bs = acessar_pagina(url)[0]
    # <div id="content-core">
    # <article class="tileItem visualIEFloatFix tile-collective-nitf-content">
    lista_tag_article = bs.find('div', attrs={'id': 'content-core'}).find_all('article', attrs={'class': 'tileItem visualIEFloatFix tile-collective-nitf-content'})
    for tag_article in lista_tag_article:
        titulo = tag_article.h2.text.strip()
        link = tag_article.h2.a['href'].strip()
        #TODO Extrair data, horário e número da nota, parágrafos, categorias (OBS: Colocar com tag)
        #TODO Atualizar o banco com as informações acima 
        print(titulo)
        print(link)
        print('-'*40)
        inserir_bd(titulo, link)


def inserir_bd(titulo, link): 
    env_dir = load_dotenv('.env_dir')
    DIR_DADOS_FINAL = os.getenv('DIR_DADOS_FINAL')
    criar_dir = os.makedirs(DIR_DADOS_FINAL, exist_ok= True)
    print(DIR_DADOS_FINAL)
    bd = TinyDB(f'{DIR_DADOS_FINAL}/coleta.json', indent=4,ensure_ascii=False)
    buscar = Query()
    verificar_bd = bd.contains(buscar.link == link)
    if not verificar_bd:
        bd.insert({
            'título': titulo,
            'link': link
        
        })
    else:
        print('Já está na base!')
    # bd = TinyDB('{}/coleta.json'.format(DIR_DADOS_FINAL))

def main():
    extrair_infos()
    # inserir_bd()

if __name__ == '__main__':
    main()
