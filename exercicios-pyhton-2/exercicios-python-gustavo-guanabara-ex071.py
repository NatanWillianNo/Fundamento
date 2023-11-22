# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print('Programa de Soma de Números Inteiros')
som = 0
con = 0
while True:
    num = int(input('Coloque um número (ou 999 para parar): '))
    
    if num == 999:
        break
    som += num
    con += 1
print("\n=== Resultados ===")
print(f"Foram digitados {con} números.")
print(f"A soma entre eles é: {som}")

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 
while True:
    numero = int(input("Digite um número para ver a tabuada (ou um número negativo para parar): "))
    if numero < 0:
        break
        print(f"\n=== Tabuada do {numero} ===")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
print("\nPrograma encerrado. Obrigado!")

# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
vitorias_consecutivas = 0
while True:
    print('=== PAR OU ÍMPAR ===')
    import time 
    import random
    
    time.sleep(1)
    print('Processando...')
    time.sleep(1)
    
    escolha = str(input('Escolha par ou ímpar [P/I] ')).upper()
    
    if escolha == 'P':
        print('Você escolheu PAR!')
    elif escolha == 'I':
        print('Você escolheu ímpar!')
    
    escolhauser = int(input('Escolha um número: '))
    escolhacomp = random.randrange(0, 10)
    
    time.sleep(2)
    print('Processando...')
    print(f'O computador escolheu {escolhacomp}')
    time.sleep(1)
    print('Processando...')
    
    calc = (escolhauser + escolhacomp) % 2
    
    if calc == 0 and escolha == 'P':
        print('Deu par! Você venceu!')
        vitorias_consecutivas += 1
    elif calc != 0 and escolha == 'I':
        print('Deu ímpar! Você venceu!')
        vitorias_consecutivas += 1
    else:
        print('Você perdeu! Fim do jogo.')
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")

# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
pessoas_maior_18 = 0
homens_cadastrados = 0
mulheres_menor_20 = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa [M/F]: ").upper()
    if idade > 18:
        pessoas_maior_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

    continuar = input("Deseja cadastrar mais uma pessoa? (S/N): ").upper()
    if continuar != 'S':
        break
print("\n=== Resultados ===")
print(f"A) Total de pessoas com mais de 18 anos: {pessoas_maior_18}")
print(f"B) Total de homens cadastrados: {homens_cadastrados}")
print(f"C) Total de mulheres com menos de 20 anos: {mulheres_menor_20}")

# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
total = 0
cont = 0
produtos_mais_caros = []
nome_do_produto_mais_barato = ""
preco_do_produto_mais_barato = float('inf')  
while True:
    nome = input("Insira o nome do produto (ou pressione Enter para encerrar): ")
    if nome == "":
        break
    preco = float(input("Insira o preço do produto: R$"))
    total += preco
    cont += 1
    if preco > 1000:
        produtos_mais_caros.append(nome)
    if preco < preco_do_produto_mais_barato:
        nome_do_produto_mais_barato = nome
        preco_do_produto_mais_barato = preco
print("\n=== Resultados ===")
print("A) Total Gasto: R${:.2f}".format(total))
print("B) Produtos Mais Caros: {}".format(produtos_mais_caros))
print("C) Nome do Produto Mais Barato: {}".format(nome_do_produto_mais_barato))

# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# Solicita ao usuário o valor a ser sacado
valor_saque = int(input("Digite o valor que deseja sacar: R$ "))
while valor_saque <= 0:
    print("Por favor, insira um valor válido.")
    valor_saque = int(input("Digite o valor que deseja sacar: R$"))
cedulas_disponiveis = [50, 20, 10, 2]
quantidade_cedulas = {}
for cedula in cedulas_disponiveis:
    quantidade = valor_saque // cedula
    if quantidade > 0:
        quantidade_cedulas[cedula] = quantidade
        valor_saque %= cedula
print("Quantidade de cédulas a serem entregues:")
for cedula, quantidade in quantidade_cedulas.items():
    print(f"R${cedula}: {quantidade} cédulas")
