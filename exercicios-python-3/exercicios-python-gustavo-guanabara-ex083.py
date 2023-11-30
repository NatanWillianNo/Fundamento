# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
from time import sleep
print('=== Organizador de 5 Números===')
listanum = []
num0 = int(input('Qual é o número na posição 0: '))
listanum.append(num0)
num1 = int(input('Qual é o número na posição 1: '))
listanum.append(num1)
num2 = int(input('Qual é o número na posição 2: '))
listanum.append(num2)
num3 = int(input('Qual é o número na posição 3: '))
listanum.insert(2, num3)
num4 = int(input('Qual é o número na posição 4: '))
listanum.insert(3, num4)
listanum.sort()
sleep(2)
print('Pensando...')
sleep(2)
print('A lista teve 5 números, os quais são? {}'.format(listanum))
print('O maior valor da lista é {}'.format(listanum[-1]))
print('O menor valor da lista é {}'.format(listanum[0]))

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
print('=== Organizador de Números ===')
listanum2 = []
while True:
    num2 = int(input('Que número você quer colocar na lista?: '))
    if num2 not in listanum2:
        listanum2.append(num2)
    else:
        print('Esse número já está na lista. Não será adicionado novamente.')
    escolha = input('Se deseja continuar digite [S/N]: ').upper()
    if escolha != 'S':
        break
listanum2.sort()
sleep(2)
print('Processando...')
print('Valores únicos digitados, em ordem crescente:', listanum2)

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.
# Cria uma lista vazia
lista_numeros = []
for _ in range(5):
    valor = int(input('Digite um valor numérico: '))
    for i in range(len(lista_numeros)):
        if valor < lista_numeros[i]:
            lista_numeros.insert(i, valor)
            break
    else:
        lista_numeros.append(valor)
print('Lista ordenada:', lista_numeros)

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
print('=== Extrator de dados de uma Lista ===')
lista_numeros2 = []
while True:
    numeros2 = int(input('Que número você quer colocar na lista?: '))
    if numeros2 not in lista_numeros2:
        lista_numeros2.append(numeros2)
    else:
        print('Esse número já está na lista. Não será adicionado novamente.')
    escolha = input('Se deseja continuar digite [S/N]: ').upper()
    if escolha != 'S':
        break
quantidade_numeros = len(lista_numeros2)
print(f'Foram digitados {quantidade_numeros} números.')
lista_numeros2.sort(reverse=True)
print('Lista de valores em ordem decrescente:', lista_numeros2)
if 5 in lista_numeros2:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')

# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
lista_num = []
lista_par = []
lista_impar = []
print('Par ou Ímpar em Listas')
while True:
    parimpar = int(input('Que número você quer colocar na lista?: ')) 
    if parimpar not in lista_num:
        lista_num.append(parimpar)
    else:
        print('Esse número já está na lista. Não será adicionado novamente.')
    if parimpar % 2 == 0:
        lista_par.append(parimpar)
    else:
        lista_impar.append(parimpar)
    escolha = input('Se deseja continuar digite [S/N]: ').upper() 
    if escolha != 'S':
        break   
print('Lista de números:', lista_num)
print('Lista de números pares:', lista_par)
print('Lista de números ímpares:', lista_impar)

    
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao_usuario = input('Digite uma expressão com parênteses: ')
pilha = []
for char in expressao_usuario:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if not pilha:
            print('Os parênteses não estão balanceados!')
            break
        pilha.pop()

if not pilha:
    print('Os parênteses estão balanceados!')
else:
    print('Os parênteses não estão balanceados!')


    