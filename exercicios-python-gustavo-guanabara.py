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
ex005 = int(input('Digite um número: '))
suc = ex005+1
ant = ex005-1
print('Sabendo que o número inserido é o {}. O seu sucessor é {} e o seu antecessor é {}'.format(ex005, suc, ant))
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('Vamos calcular o dobro, triplo e raiz quadrada. de um determinado número?')
ex006 = float(input('Digite um número: '))
dobro = ex006*2
triplo = ex006*3
raiz = ex006**0.5 
print('O número escolhido foi {}. O seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(ex006, dobro, triplo, raiz))
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
print("A medida de {} metros em kilômetros é {} km.".format(medida, km))
print("A medida de {} metros em hectômetros é {} hm.".format(medida, hm))
print("A medida de {} metros em decâmetros é {} dam.".format(medida, dam))
print("A medida de {} metros em metros é {} m.".format(medida, m))
print("A medida de {} metros em decímetros é {} dm.".format(medida, dm))
print("A medida de {} metros em centímetros é {} cm.".format(medida, cm))
print("A medida de {} metros em milímetros é {} mm.".format(medida, mm))
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
print('Vamos calcular a tabuada de um número até o 10')
ex009 = int(input('Coloque um número inteiro e mostraremos a sua tabuada até o 10: '))
print('A tabuada do número {} é:'.format(ex009))
print('{} multiplicado por 0 é {}'.format(ex009, ex009*0))
print('{} multiplicado por 1 é {}'.format(ex009, ex009*1))
print('{} multiplicado por 2 é {}'.format(ex009, ex009*2))
print('{} multiplicado por 3 é {}'.format(ex009, ex009*3))
print('{} multiplicado por 4 é {}'.format(ex009, ex009*4))
print('{} multiplicado por 5 é {}'.format(ex009, ex009*5))
print('{} multiplicado por 6 é {}'.format(ex009, ex009*6))
print('{} multiplicado por 7 é {}'.format(ex009, ex009*7))
print('{} multiplicado por 8 é {}'.format(ex009, ex009*8))
print('{} multiplicado por 9 é {}'.format(ex009, ex009*9))
print('{} multiplicado por 10 é {}'.format(ex009, ex009*10))
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
carteira_str = input('Quantos reais você tem na carteira?: R$ ')
carteira_str = carteira_str.replace(',', '.')
carteira = float(carteira_str)
usd_str = input('Quantos está custando o dólar hoje?: US$ ')
usd_str = usd_str.replace(',', '.')
usd = float(usd_str)
conv = carteira / usd
print('Você tem R${:.2f}, isso é equivalente a US${:.2f}'.format(carteira, conv))
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input('Coloque a largura da parede em metros: '))
alt = float(input('Coloque a altura da parede em metros: '))
area = larg * alt
litros_por_metro_quadrado = float(input('Coloque a quantidade de tinta por metro quadrado: '))
tinta_necessaria = area / litros_por_metro_quadrado
print('Sabendo que a área da parede equivale a {:.2f} metros quadrados, será necessário utilizar {:.2f} litros de tinta'.format(area, tinta_necessaria))
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prod = input('Qual é o produto que você quer analisar?: ')
preço = float(input('Qual é o preço do produto?: '))
desc = float(input('Qual é o desconto do produto?: '))
preçodesc = preço*(desc/100)+preço
print('{} custava {:.2f} antes do desconto de {:.2f}%, agora custa {:.2f}'.format(produto, preço, desc, preçodesc))