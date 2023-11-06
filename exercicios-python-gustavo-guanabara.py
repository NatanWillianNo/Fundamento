# Crie um programa que escreva "Olá mundo" na tela
print('Olá mundo! print simples')
msg = 'Olá mundo! variavel'
print(msg)
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
print('Vamos dar as boas vindas?')
nome = input("Qual é o seu nome? ")
print("Seja bem-vindo, {}.".format(nome))
# Crie um programa que leia dois números e mostre a soma entre eles. 
print('Vamos somar dois números?')          
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print('Vamos ver o tipo primitivo de um valor e todas as informações possíveis sobre ele?')
tcld = input('Digite aqui: ')
print('Tipo primitivo: ', type(tcld))
print('Só tem espaços? ', tcld.isspace())
print('É um número?', tcld.isnumeric())
print('É alfabético?', tcld.isalpha())
print('É alfanúmerico?', tcld.isalnum())
print('Está em maiúsculas?', tcld.isupper())
print('Está em minúsculas?', tcld.islower())
print('Está capitalizada?', tcld.istitle())
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
print('Vamos calcular o sucessor e antecessor de um determinado número?')
ex006 = int(input('Digite um número: '))
suc = ex006+1
ant = ex006-1
print('Sabendo que o número inserido é o {}. O seu sucessor é {} e o seu antecessor é {}'.format(ex006, suc, ant))
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('Vamos calcular a média de um aluno?')
nomealuno = input('Qual é o nome desse aluno?: ')
nota1 = float(input('Insira a nota do primeiro bimestre: ' ))
nota2 = float(input('Insira a nota do segundo bimestre: '))
nota3 = float(input('Inisra a nota do terceiro bimestre: '))
nota4 = float(input('Insira a nota do quarto e último bimestre: '))
media = (nota1+nota2+nota3+nota4)/4
print('A média de {} é igual a {}'.format(nomealuno, media))
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Uma distância em metros: '))
print('A distância de {} metros equivale a '.format(medida))
km = medida/1000
hm = medida/100
dam = medida/10
m = medida/1
dm = medida*10
cm = medida*100
mm = medida*1000