from tinydb import TinyDB, Query
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text,'html.parser')
    http_code = html.status_code
    return bs, http_code

def extrair_infos():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=30"
    bs = acessar_pagina(url)[0]

def inserir_bd(): 
    pass

def main():
    extrair_infos()

if __name__ == '__main__':
    main()
