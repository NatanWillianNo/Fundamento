from tinydb import TinyDB, Query
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
import os

titulo_lista = []
link_lista = []
data_lista = []
horario_lista = []
numero_da_nota_lista = []
paragrafos_lista = []
categoria_lista = []


def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    http_code = html.status_code
    return bs, http_code

#TODO Extrair data, horário e número da nota, parágrafos, categorias (OBS: Colocar com tag)
#TODO Atualizar o banco com as informações acima 

# Função para extrair informações de um artigo
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
        for p in lista_paragrafos:
            p = p.text.strip()
            print(p)
        categorias = artigo[0].find('div', class_='contenttree-widget relationchoice-field').text
        

'''
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
'''
def main():
    extrair_infos()
    # inserir_bd()

if __name__ == '__main__':
    main()
