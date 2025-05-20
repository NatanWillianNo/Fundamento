# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros_por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = int(input('Escolha um número de 0 a 20: '))
if 0 <= escolha <= 20:
    print(numeros_por_extenso[escolha])
else:
    print('Número fora do intervalo permitido.')

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
from time import sleep
tabela = (
    "Corinthians - SP", "Palmeiras - SP", "Santos - SP", "Grêmio - RS", "Cruzeiro - MG",
    "Flamengo - RJ", "Vasco da Gama - RJ", "Chapecoense - SC", "Atlético - MG", "Botafogo - RJ",
    "Atlético - PR", "Bahia - BA", "São Paulo - SP", "Fluminense - RJ", "Sport - PE",
    "Vitória - BA", "Coritiba - PR", "Avaí - SC", "Ponte Preta - SP", "Atlético - GO"
)
time_chapecoense = "Chapecoense - SC"
posicao_chapecoense = tabela.index(time_chapecoense) + 1
print('=== Tabela do Brasileirão ===')
print('Os cinco primeiros colocados são:')
sleep(1)
for time in tabela[:5]:
    print('- {}'.format(time))
print('\nOs rebaixados desse ano são:')
sleep(1)
for time in tabela[-4:]:
    print('- {}'.format(time))
print('\nOs times em ordem alfabética:')
sleep(1)
for time in sorted(tabela):
    print('- {}'.format(time))
sleep(1)
print('O time Chapecoense está na posição: {}'.format(posicao_chapecoense))

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
numeros_aleatorios = tuple(random.sample(range(0, 999), 5))
print('Números gerados:', numeros_aleatorios)
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)
print('Menor valor na tupla:', menor_valor)
print('Maior valor na tupla:', maior_valor)

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))
tupla_valores = (valor1, valor2, valor3, valor4)
quantidade_nove = tupla_valores.count(9)
posicao_tres = tupla_valores.index(3) + 1 if 3 in tupla_valores else None
numeros_pares = tuple(filter(lambda x: x % 2 == 0, tupla_valores))
print(f'A) O valor 9 apareceu {quantidade_nove} vezes.')
print(f'B) O primeiro valor 3 foi digitado na posição {posicao_tres}.' if posicao_tres else 'B) O valor 3 não foi digitado.')
print(f'C) Números pares digitados: {numeros_pares}')

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
num_produtos = int(input("Digite o número de produtos: "))
produtos_precos = []
for _ in range(num_produtos):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    produtos_precos.append((nome_produto, preco_produto))
print("{:<15} {:<10}".format("Produto", "Preço"))
for produto, preco in produtos_precos:
    print("{:<15} R${:<10.2f}".format(produto, preco))

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
entrada_usuario = input("Digite as palavras separadas por vírgula: ")
palavras = [palavra.strip() for palavra in entrada_usuario.split(',')]
for palavra in palavras:
    vogais_na_palavra = [letra for letra in palavra if letra.lower() in "aeiou"]
    print(f'Vogais em "{palavra}": {", ".join(vogais_na_palavra)}')
