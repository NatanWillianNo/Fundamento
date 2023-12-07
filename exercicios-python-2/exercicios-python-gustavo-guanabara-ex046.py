# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('=== Aprovando Empréstimo ===')
valcasa = float(input('Qual é o valor da casa que deseja comprar?:R$ '))
salario = float(input('Qual é o valor do seu salário?:R$ '))
periodo = float(input('Em meses, em quanto tempo você deseja pagar esse empréstimo?: '))
prestação = valcasa / periodo
anos = periodo/12
if prestação <= 0.3*salario:
    print('Você consegue pegar o empréstimo. Você pagará essa casa em {} meses com parcelas de R${:.2f}'.format(periodo,prestação))
    print('Empréstimo APROVADO')
else:
    print('Você não consegue ainda. Seu salário não permite a retirada do empréstimo!')
    print('Em {} anos ou {} meses você pagaria parcelas de R${:.2f} que é superior a 30% do seu salário atual de {}'.format(anos, periodo, prestação, salario))
    print('Empréstimo NEGADO')

# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# Ṕeça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('=== Conversor de Inteiro para: Binário, Octal, Hexadecimal')
num = (int(input('Insira o número que deseja converter: ')))
base = int(input('Insira a base para a qual você deseja converter:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha a opção (1, 2 ou 3): '))
if   base == 1:
    resultado = bin(num)
    print('O valor em binário é: {}'.format(resultado))
elif base == 2:
    resultado = oct(num)
    print('O valor em octal é {}'.format(octal))
elif base == 3:
    resultado = hex(num)
    print('O valor em hexadecimal é {}'.format(resultado))
print('Obrigado por usar o conversor!')

# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior 
# - Não existe valor maior, os dois são iguais
print('=== Comparador de números inteiros ===')
int1 = int(input('Coloque um valor inteiro: '))
int2 = int(input('Coloque outro número inteiro: '))
if int1 > int2:
    print('O primeiro número {} é maior que o segundo {}'.format(int1, int2))
elif int1 < int2:
    print('O segundo número {} é maior que o primeiro {}'.format(int2, int1))
elif int1 == int2:
    print('Os números inseridos são exatamente iguais!')
print('Obrigado por usar o comparador de números')

# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('=== Alistamento Militar Obrigatório ===')
atual = date.today().year
anonasc = int(input('Qual é o ano do seu nascimento?: '))
idd = atual - anonasc
if idd == 18:
    print('Você deve se alistar nesse ano')
elif idd < 18:
    print('Vocẽ não precisa se alistar agora, volte daqui {} anos'.format(18-idd))
else:
    print('Você está atrasado no seu alistamento! Se passaram {} anos do prazo'.format(idd-18))
print('Exército Brasileiro agradece a compreensão')

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print('=== Boletim automático ===')
nota1 = float(input('Qual foi a primeira nota?: '))
nota2 = float(input('Qual foi a segunda nota?: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('O aluno foi aprovado!')
elif 5.0 <= media < 6.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno está reprovado!')

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
print('=== Confederação Nacional de Natação ===')
print('=== Categoria automática 1.0 ===')
atualnat = date.today().year
print(atualnat)
iddnat = int(input('Coloque o ano de seu nascimento: '))
iddatual = atualnat - iddnat
print(iddatual)
if iddatual <= 9:
    print('Você está inscrito na categoria MIRIM!')
elif iddatual <= 14:
    print('Você está inscrito na categoria INFANTIL!')
elif iddatual <= 19:
    print('Você está inscrito na categoria JÚNIOR!')
elif iddatual <= 25:
    print('Você está inscrito na categoria SÊNIOR')
else:
    print('Você está inscrito na categoria MASTER!')

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente 
# - ESCALENO: todos os lados diferentes
print("=== Verificador de Triângulo 2.0 ===")
print('Lembrando que a Condição de existência de um triângulo é')
print('Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.')
ladoa = float(input('Coloque o primeiro lado do seu triângulo: '))
ladob = float(input('Coloque o segundo lado do seu triângulo: '))
ladoc = float(input('Coloque o terceiro e último lado desse triângulo: '))
modulo_ab = abs((ladoa - ladob))
modulo_ac = abs((ladoa - ladoc))
modulo_bc = abs((ladob - ladoc))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    if ladoa == ladob == ladoc:
        print('O triângulo é equilátero.')
    elif ladoa == ladob or ladob == ladoc or ladoa == ladoc:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os valores fornecidos não formam um triângulo.')

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print("=== Análise de IMC ===")
print('O Índice de Massa Corporal (IMC) é uma medida usada para avaliar a quantidade de gordura corporal de uma pessoa com base em sua altura e peso')
alt = float(input('Qual é a sua altura em metros?: ' ))
pes = float(input('Qual é o seu peso em kilogramas?: '))
imc = pes / alt ** 2
print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    status = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    status = 'Peso Ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'
print('Logo seu status é de', status)
print('Obrigado por usar o Análise de IMC')

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print("=== Calculadora de Pagamento ===")
preco = float(input("Digite o preço do produto: R$ "))
print("Escolha a condição de pagamento:")
print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço formal)")
print("4 - 3x ou mais no cartão (20% de juros)")
opcao = int(input("Digite o número da opção desejada: "))
if opcao == 1:
    valor_final = preco - (preco * 0.10)
    print(f"Total a ser pago: R$ {valor_final:.2f} (10% de desconto)")
elif opcao == 2:
    valor_final = preco - (preco * 0.05)
    print(f"Total a ser pago: R$ {valor_final:.2f} (5% de desconto)")
elif opcao == 3:
    valor_final = preco
    print(f"Total a ser pago: R$ {valor_final:.2f} (Preço formal em até 2x no cartão)")
elif opcao == 4:
    parcelas = int(input("Digite o número de parcelas desejado: "))
    if parcelas >= 3:
        valor_final = preco + (preco * 0.20)
        print(f"Total a ser pago: R$ {valor_final:.2f} (20% de juros em {parcelas}x no cartão)")
    else:
        print("Opção inválida para parcelamento. Escolha uma opção válida.")
else:
    print("Opção inválida. Escolha uma opção de 1 a 4.")
print("Obrigado por utilizar a Calculadora de Pagamento.")
# Crie um programa que faça o computador jogar Jokenpô com você.
import random
print("Jogo de Jokenpô: Pedra, Papel, Tesoura")
opcoes = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(opcoes)
usuario = input("Escolha: Pedra, Papel ou Tesoura? ").capitalize()
print(f"Você escolheu: {usuario}")
print(f"Computador escolheu: {computador}")
if usuario == computador:
    print("Empate!")
elif usuario == "Pedra" and computador == "Tesoura":
    print("Você venceu!")
elif usuario == "Papel" and computador == "Pedra":
    print("Você venceu!")
elif usuario == "Tesoura" and computador == "Papel":
    print("Você venceu!")
else:
    print("Você perdeu!")
