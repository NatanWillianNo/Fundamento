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

# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
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