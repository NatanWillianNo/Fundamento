# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import time
def fatorial(fatorando, show=False):
    resultado = 1
    if show:
        print(f'Calculando o fatorial de {fatorando}...')
    for i in range(1, fatorando + 1):
        resultado *= i
        if show:
            print(f'{fatorando} x {i} = {resultado}')
            time.sleep(0.5)  # Adiciona um atraso de 0.5 segundos entre as operações
    return resultado
num = int(input("Digite um número para calcular o fatorial: "))
mostrar_processo = input("Deseja mostrar o processo de cálculo? (S/N): ").upper()
if mostrar_processo == "S":
    mostrar_processo = True
else:
    mostrar_processo = False
print(f'O fatorial de {num} é {fatorial(num, mostrar_processo)}')

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
import time
def fatorial(fatorando, show=False):
    resultado = 1
    if show:
        time.sleep(1)
        print(f'Calculando o fatorial de {fatorando}...')
    for i in range(1, fatorando + 1):
        resultado *= i
        if show:
            print(f'{fatorando} x {i} = {resultado}')
            time.sleep(1)  
    return resultado
num = int(input("Digite um número para calcular o fatorial: "))
mostrar_processo = input("Deseja mostrar o processo de cálculo? (S/N): ").upper()
if mostrar_processo == "S":
    mostrar_processo = True
else:
    mostrar_processo = False
print(f'O fatorial de {num} é {fatorial(num, mostrar_processo)}')

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="Desconhecido", gols=0):
    print(f"O jogador {nome} marcou {gols} gol(s).")

nome_jogador = input("Digite o nome do jogador: ")
gols_jogador = input("Digite a quantidade de gols marcados pelo jogador: ")

# Verifica se foi inserido um valor para os gols
if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
    ficha(nome_jogador, gols_jogador)
else:
    ficha(nome_jogador)



