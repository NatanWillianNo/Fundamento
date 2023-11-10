# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print("=== Exibição da Parte Inteira de um Número Real ===")
import math
from math import trunc
numero_real = float(input('Digite um número real: '))
parte_inteira = trunc(numero_real)
print('A parte inteira do número {} é {}'.format(numero_real, parte_inteira))

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
print("=== Cálculo da Hipotenusa ===")
from math import sqrt
catadj = float(input('Qual é valor do cateto adjacente? '))
catopo = float(input('Qual é o valor do cateto oposto? '))
hipo = sqrt(catopo**2 +catadj**2)
print('O valor da hipotenusa é: {}'.format(hipo))

#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
print("=== Cálculo do Seno, Cosseno e Tangente de um Ângulo ===")
from math import sin, cos, tan, radians
ang_graus = float(input("Digite o valor do ângulo em graus: "))
ang_radiano = radians(ang_graus) 
seno = sin(ang_radiano) 
cosseno = cos(ang_radiano)
tangente = tan(ang_radiano)
print('O valor do seno de {}° equivale a {:.2f}'.format(ang_graus, seno))
print('O valor do cosseno de {}° equivale a {:.2f}'.format(ang_graus, cosseno))
print('O valor da tangente de {}° equivale a {:.2f}'.format(ang_graus, tangente))

#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
print("=== Sorteio do Aluno ===")
from random import choice
aluno1 = str(input('Coloque o nome do primeiro aluno: '))
aluno2 = str(input('Coloque o nome do segundo aluno:  '))
aluno3 = str(input('Coloque o nome do terceiro aluno: '))
aluno4 = str(input('Coloque o nome do quarto e último aluno: '))
nomes = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(nomes)
print('O aluno escolhido foi: {}'.format(sorteado))
#
#  O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print("=== Sorteio da ordem ===")
from random import shuffle
al1 = str(input('Insira o nome do primeiro aluno: '))
al2 = str(input('Insira o nome do segundo aluno: '))
al3 = str(input('Insira o nome do terceiro aluno: '))
al4 = str(input('Insira o nome do quarto e último aluno: '))
nomes2 = [al1,al2,al3, al4]
shuffle(nomes2)
print('A ordem de apresentação é: {}'.format(nomes2))

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('ex021mario.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()