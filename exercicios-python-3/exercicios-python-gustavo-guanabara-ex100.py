# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.



def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"A área do terreno é: {area_terreno} metros quadrados.")
largura = float(input("Informe a largura do terreno em metros: "))
comprimento = float(input("Informe o comprimento do terreno em metros: "))
area(largura, comprimento)

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
Ex: escreva('Olá, Mundo!')
Saída: ~~~~~~~~~
       Olá, Mundo!
       ~~~~~~~~~
``
'''

def escreva(texto):
    largura_linha = len(texto) + 4
    linha = '~' * largura_linha
    print(linha)
    print(f' {texto} ')
    print(linha)
     
texto_usuario = input('Digite o texto que deseja formatar: ')
escreva(texto_usuario)

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
def contador(i, f, p):
    if p == 0:
        print("O passo não pode ser zero.")
        return
    if i < f:
        for i in range(i, f + 1, p):
            print(i, end=' ')
        print()
    else:
        for i in range(i, f - 1, -p):
            print(i, end=' ')
        print()
print("Contagem de 1 até 10, de 1 em 1:")
contador(1, 10, 1)
print("\nContagem de 10 até 0, de 2 em 2:")
contador(10, 0, 2)
print("\nContagem personalizada:")
inicio_personalizado = int(input("Digite o valor inicial: "))
fim_personalizado = int(input("Digite o valor final: "))
passo_personalizado = int(input("Digite o passo: "))
contador(inicio_personalizado, fim_personalizado, passo_personalizado)

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*valores):
    if len(valores) == 0:
        print("Nenhum valor foi informado.")
    else:
        max_valor = max(valores)
        print(f"O maior valor informado é: {max_valor}")
valores = []
while True:
    valor = input("Digite um valor (ou 'sair' para encerrar): ")
    if valor.lower() == 'sair':
        break
    elif valor.isdigit():
        valores.append(int(valor))
    else:
        print("Por favor, digite um valor inteiro válido.")
maior(*valores)

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random
def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
    print(f"Números sorteados: {numeros}")
    return numeros
def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Soma dos números pares: {soma}")
numeros_sorteados = sorteia()
somaPar(numeros_sorteados)

