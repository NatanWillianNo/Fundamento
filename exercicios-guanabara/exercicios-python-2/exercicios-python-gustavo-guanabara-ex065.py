# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
print('=== Validação de Dados ===')
sexo = input('Qual é o seu sexo [M/F]?: ')
while sexo.upper() != 'M' and sexo.upper() != 'F':
    print('Você digitou um dado inválido, tente novamente!')
    sexo = input('Qual é o seu sexo [M/F]?: ')
print('Obrigado por usar')

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import time 
import random
print('Jogo da Adivinhação 2.0')
time.sleep(1)
print('Processando...')
time.sleep(1)
print('Vamos jogar um jogo?')
computador = random.randrange(0, 10)
print(computador)
while True:
    numalt = int(input('Escolha um número: '))
    if numalt == computador:
        print('Parabéns! Você acertou o número!')
    else:
        print('Tente novamente!')

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('=== Calculadora ===')
while True:
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira outro número: '))
    print('Insira sua opção:')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = int(input())
    if opcao == 1:
        resultado = num1 + num2
        print('A soma de {} e {} é {}'.format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('O produto de {} e {} é {}'.format(num1, num2, resultado))
    elif opcao == 3:
        maior = max(num1, num2)
        print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
    elif opcao == 4:
        continue
    elif opcao == 5:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')

# Faça um programa que leia um número qualquer e mostre o seu fatorial.
print('Calculadora de Fatorial')
resultado = 1
fator = int(input('Insira um número: '))
ant = fator
while ant > 1:
    resultado *= ant
    ant -= 1
print('O fatorial de {} é {}.'.format(fator, resultado))

# Refaça o exercício de PA, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('===== Termos de uma PA =====')
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo_atual = primeiro_termo
contador = 1
while True:
    print(f'{termo_atual}', end=' -> ')
    termo_atual += razao
    contador += 1
    opcao = int(input('\nDeseja mostrar mais termos? Digite a quantidade desejada (0 para encerrar): '))
    if opcao == 0:
        break
print('Fim da PA.')

# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
print('===== Sequência de Fibonacci =====')
N = int(input('Digite a quantidade de termos que deseja exibir: '))
fibonacci = [0, 1]
while len(fibonacci) < N:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print('Os primeiros {} termos da Sequência de Fibonacci são: {}'.format(N, fibonacci))

# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('=== Programa de Leitura de Números ===')
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break  # Sai do loop se o usuário digitar 999
    else:
        soma += numero
        contador += 1
print('\nPrograma encerrado. Você digitou {} números e a soma entre eles é {}.'.format(contador, soma))

# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('=== Programa de Análise de Números ===')
continuar = 'S'
soma = contador = 0
maior = menor = None
while continuar.upper() == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        maior = max(maior, numero)
        menor = min(menor, numero)
    continuar = input('Deseja continuar? (S para Sim, qualquer outra tecla para Não): ')
if contador > 0:
    media = soma / contador
    print(f'\nAnálise final:')
    print(f'Média dos números: {media:.2f}')
    print(f'Maior número digitado: {maior}')
    print(f'Menor número digitado: {menor}')
else:
    print('Nenhum número foi digitado.')

