# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
for contagem in range(10, 0, -1):
    print(contagem)
    time.sleep(1)
print("Feliz Ano Novo! 🎆")
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for par in range(50, 0, -2):
    print(par)
print('Esses são os números pares que estão no intervalo entre 1 e 50.')

# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma dos múltiplos de três no intervalo de 1 a 500 é: {soma}')

# Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('Vamos calcular a tabuada de um número até o 10')
ex049 = int(input('Coloque um número inteiro e mostraremos a sua tabuada até o 10: '))
for tabuada in range(1, 11):
    resultado = ex049 * tabuada
    print('{} multiplicado por {} é {}'.format(ex049, tabuada, resultado))

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
par = 0
tem_par = False  
for _ in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        par += num 
        tem_par = True  
if tem_par:
    print('A soma dos números pares é: {}'.format(par))
else:
    print('Somente há números ímpares, tente novamente!')

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
print('=== Calculadora de PA ===')
n1 = float(input('Insira o primeiro termo de uma progressão aritmética: '))
rz = float(input('Insira a razão dessa progressão aritmética: '))
termos = []  
for c in range(10):
    termo = n1 + c * rz
    termos.append(termo)
print('Aqui estão os 10 primeiros termos da progressão aritmética: {}'.format(termos))

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print("Não é um número primo.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False

    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase_usuario = input("Digite uma frase: ")
frase_sem_espacos = frase_usuario.replace(" ", "")
frase_invertida = ""
for char in frase_sem_espacos:
    frase_invertida = char + frase_invertida
if frase_sem_espacos == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior18 = 0
menor18 = 0
from datetime import date
atual = date.today().year
ano_atual = int(input("Coloque o ano atual: "))
for idade in range(6):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = atual - ano_nascimento
    if idade >= 18:
        maior18 += 1
    else:
        menor18 += 1
print('O número total de maiores de idade nesse grupo é: {}'.format(maior18))
print('O número total de menores de idade nesse grupo é: {}'.format(menor18))

# Faça um programa que leia o peso de cinco pessoas. 
peso = float(input('Digite o peso da pessoa 1: '))
maior_peso = peso
menor_peso = peso
for i in range(2, 6):
    peso = float(input(f'Digite o peso da pessoa {i}: '))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print('\nO maior peso lido foi: {:.2f} kg'.format(maior_peso))
print('O menor peso lido foi: {:.2f} kg'.format(menor_peso))
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# Inicialize variáveis para a soma da idade, nome do homem mais velho e contador de mulheres menores de 20 anos
soma_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
contagem_mulheres_menor_20 = 0
for i in range(1, 5):
    print(f'--- Pessoa {i} ---')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()
    soma_idade += idade
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        contagem_mulheres_menor_20 += 1
media_idade = soma_idade / 4
print('\n--- Resultados ---')
print('Média de idade do grupo: {:.2f} anos'.format(media_idade))
print('Nome do homem mais velho: {}'.format(nome_homem_mais_velho))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(contagem_mulheres_menor_20))
