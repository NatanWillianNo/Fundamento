# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from time import sleep
from math import sqrt

print('CALCULADORA DE BHASKARA')
sleep(1)
print('Lembre-se que a equação geral do segundo grau é ax² + bx + c.')
sleep(1)

a = float(input('Informe o coeficiente a: '))
if a == 0:
    print('Coeficiente "a" não pode ser zero. Encerrando o programa.')
else:
    b = float(input('Informe o coeficiente b: '))
    c = float(input('Informe o coeficiente c: '))

    delta = b**2 - 4*a*c
    print('Δ = {}'.format(delta))

    if delta < 0:
        print('Sua equação não tem raízes reais.')
    elif delta == 0:
        print('Sua equação tem uma raiz, que é:')
        raiz0 = -b + sqrt(delta) / (2 * a)
        print('A raiz da sua equação é: {}'.format(raiz0))
    elif delta > 0:
        print('Sua equação tem duas raízes, que são:')
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print('As raízes da sua equação são {} e {}'.format(raiz1, raiz2))

# Desenvolva uma função que calcule o valor final de um investimento com base em uma taxa de juros e um período de tempo. (M = C * (1 + i)^t)
from time import sleep
print('-'*30)
print('CALCULADORA DE JUROS')
print('-'*30)
sleep(1)
print('Vamos calcular o montante no regime de Juros Compostos')
capital = float(input('Insira o capital que deseja investir: '))
taxa = float(input(('Insira o valor da taxa percentual (mensal): ')))
tempo = float(input(('Insira o tempo que deseja aplicar (meses): ' )))
montante = capital * (1 + taxa/100)**tempo
sleep(1)
print('Calculando...')
sleep(1)
print('Calculando...')
sleep(1)
print('-'*30)
sleep(1)
print('Aplicando um capital de R${:.2f} numa taxa de {}% e num tempo de {} meses'.format(capital, taxa, tempo))
print('O montante total é de R${:.2f}'.format(montante))
print('-'*30)
print('Obrigado por usar o CALCULADORA DE JUROS')

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print("=== CALCULADORA COM ANÁLISE DOS RESULTADOS ===")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sleep(1)
print('-' * 40)
print('Menu de Opções')
print('-' * 40)
print('1 - Adição (+)')
print('2 - Subtração (-)')
print('3 - Multiplicação (*)')
print('4 - Divisão (÷)')
operacao = int(input('Qual operação você quer utilizar?: '))
if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Não é possível dividir por zero.")
        exit()
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
    exit()
par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"
positivo_ou_negativo = "positivo" if resultado > 0 else "negativo"
inteiro_ou_decimal = "inteiro" if resultado.is_integer() else "decimal"
print(f"Resultado: {resultado}")
print(f"O resultado é {par_ou_impar}, {positivo_ou_negativo}, e {inteiro_ou_decimal}.")

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print('=== FORMATADOR DE DATA ===')
ano = int(input('Coloque um ano: '))
mes = int(input('Coloque um mês: '))
dia = int(input('Coloque um dia: '))
meses_com_31_dias = [1, 3, 5, 7, 8, 10, 12]
meses_com_30_dias = [4, 6, 9, 11]
if not (0 <= ano <= 9999):
    print('Data inválida')
elif not (1 <= mes <= 12):
    print('Data inválida')
elif mes == 2 and not (1 <= dia <= 29 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 1 <= dia <= 28):
    print('Data inválida')
elif mes in meses_com_31_dias and not (1 <= dia <= 31):
    print('Data inválida')
elif mes in meses_com_30_dias and not (1 <= dia <= 30):
    print('Data inválida')
else:
    print('Data válida')
print('{}/{}/{}'.format(dia, mes, ano))

# Faça um programa para o cálculo de uma folha de pagamento, 
# Sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#       Salário Bruto: (5 * 220)        : R$ 1100,00
#       (-) IR (5%)                     : R$   55,00  
#       (-) INSS ( 10%)                 : R$  110,00
#       FGTS (11%)                      : R$  121,00
#       Total de descontos              : R$  165,00
#       Salário Liquido                 : R$  935,00

valor_hora = float(input("Digite o valor da hora trabalhada: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_horas
ir = 0
inss = 0
fgts = 0

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR (5%)                     : R$ {ir:.2f}")
print(f"(-) INSS (10%)                  : R$ {inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {total_descontos:.2f}")
print(f"Salário Liquido                 : R$ {salario_liquido:.2f}")

# Escreva um programa que retorne os pontos obtidos em um jogo de Dardos.
import random
import time

print('=== Jogo de Dardos ===')
print('Vamos jogar um jogo?')
print('Qual é o seu nome?')
user = str(input(''))
time.sleep(1)
print('Seja bem-vindo(a) {}'.format(user))

time.sleep(1)
print('\nTutorial:')
print(' - Na mosca: Acertar exatamente o número alvo ganha 10 pontos.')
print(' - Muito perto: Acertar a até 4 unidades do número alvo ganha pontos equivalentes à proximidade.')
print(' - Perto: Acertar de 5 a 8 unidades do número alvo ganha pontos equivalentes à proximidade.')
print(' - Longe: Não acertar ganha 0 pontos.')

pontuação_total = 0

for lançamento in range(1, 6):
    alvo = random.randint(0, 10)

    tiro = int(input(f'\nLançamento {lançamento}: Escolha um número de 0 a 10: '))
    pontos = abs(alvo - tiro)

    if pontos == 0:
        print(f'Na mosca! Você ganhou 10 pontos.')
        pontuação_total += 10
    elif pontos <= 4:
        print(f'Muito perto! Você ganhou {10 - pontos} pontos!')
        pontuação_total += (10 - pontos)
    elif pontos <= 8:
        print(f'Perto! Você ganhou {5 - (pontos - 5)} pontos!')
        pontuação_total += (5 - (pontos - 5))
    else:
        print(f'Longe! Você não ganhou pontos desta vez.')

    print(f'O número alvo era: {alvo}')

time.sleep(1)
print('Processando pontuação...')
time.sleep(1)
print('Processando pontuação...')
time.sleep(1)
print('Processando pontuação...')
time.sleep(1)
print('Processando pontuação...')
time.sleep(1)
print(f'\nA pontuação total foi: {pontuação_total} pontos.')

# Faça um programa que calcule produtos notavéis: 
# Quadrado da Soma = (x + y)²
# Quadrado da Diferença = (x - y)²
# Produto da soma pela diferença = (x + y)(x – y)
# Cubo da Soma = (x + y)³
# Cubo da Diferença = (x - y)³
from time import sleep
from sympy import symbols, expand

tipo_incognitas_x = input("Deseja inserir a primeira incógnita como número (float) ou como símbolo (str)? ").lower()
tipo_incognitas_y = input("Deseja inserir a segunda incógnita como número (float) ou como símbolo (str)? ").lower()

if tipo_incognitas_x == 'float':
    x = symbols('x')
else:
    x = float(input("Digite o valor de x: "))

if tipo_incognitas_y == 'float':
    y = symbols('y')
else:
    y = float(input("Digite o valor de y: "))

print('-' * 40)
print('Menu de Opções')
print('-' * 40)
print('1 - Quadrado da Soma (x + y)²')
print('2 - Quadrado da Diferença (x - y)²')
print('3 - Produto da soma pela diferença = (x + y)(x – y)')
print('4 - Cubo da Soma = (x + y)³')
print('5 - Cubo da Diferença = (x - y)³')

opcao = int(input("Escolha uma opção (1 a 5): "))

if opcao == 1:
    resultado = expand((x + y) ** 2)
    print(f"Resultado: ({x} + {y})² = {resultado}")
elif opcao == 2:
    resultado = expand((x - y) ** 2)
    print(f"Resultado: ({x} - {y})² = {resultado}")
elif opcao == 3:
    resultado = expand((x + y) * (x - y))
    print(f"Resultado: ({x} + {y})({x} – {y}) = {resultado}")
elif opcao == 4:
    resultado = expand((x + y) ** 3)
    print(f"Resultado: ({x} + {y})³ = {resultado}")
elif opcao == 5:
    resultado = expand((x - y) ** 3)
    print(f"Resultado: ({x} - {y})³ = {resultado}")
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

'''
Dado o escore de alergia de uma pessoa, determine se ela é ou não alérgica a um item específico e liste todas as alergias que ela possui.
Um teste de alergia gera um único escore numérico que contém informações sobre todas as alergias que a pessoa tem (para as quais foram testadas).
A lista de itens (e seus valores) que foram testados é a seguinte:
- ovos
- amendoins (2)
- frutos do mar (4)
- morangos (8)
- tomates (16)
- chocolate (32)
- pólen (64)
- gatos (128)
O programa deve ser capaz de dizer:
Se usuário é alérgico a algum dos alérgenos listados acima e Todas as alergias às quais o usuário é alérgico. 
E um score que mostra o quão alérgico o usuário é
'''

print('-'*50)
print('=== Diagnóstico de Alergias ===')
print('-'*50)
print("Pontuação possível:\n- Baixo nível de alergia: 1-4\n- Médio nível de alergia: 5-32\n- Alto nível de alergia: 33-64\n- Muito alto nível de alergia: 65 ou mais")
print('-'*50)

score = 0
alergias = []

while True:
    print('- ovos (1)\n- amendoins (2)\n- frutos do mar (4)\n- morangos (8)\n- tomates (16)\n- chocolate (32)\n- pólen (64)\n- gatos (128)')
    alerg = int(input('Quais são os produtos que você é alérgico? '))

    if alerg == 1:
        score += 1
        alergias.append('ovos')
    elif alerg == 2:
        score += 2
        alergias.append('amendoins')
    elif alerg == 4:
        score += 4
        alergias.append('frutos do mar')
    elif alerg == 8:
        score += 8
        alergias.append('morangos')
    elif alerg == 16:
        score += 16
        alergias.append('tomates')
    elif alerg == 32:
        score += 32
        alergias.append('chocolate')
    elif alerg == 64:
        score += 64
        alergias.append('pólen')
    elif alerg == 128:
        score += 128
        alergias.append('gatos')

    continuar = input('Deseja adicionar mais alérgenos? (s/n) ').lower()
    if continuar != 's':
        break

print('-'*50)
print('=== Resultado do Diagnóstico ===')
print('-'*50)

if score == 0:
    print("Nada alérgico")
elif 0 < score <= 4:
    print("Baixo nível de alergia")
elif 5 <= score <= 32:
    print("Médio nível de alergia")
elif 33 <= score <= 64:
    print("Alto nível de alergia")
else:
    print("Muito alto nível de alergia")

print(f'Você é alérgico a: {", ".join(alergias)}')
print(f'Seu escore total de alergias é: {score}')

# Programa de Lista de Compras com Subtotal

# Inicializa uma lista vazia para armazenar os itens da compra
lista_de_compras = []

# Função para formatar o nome do item
def formatar_nome(nome):
    return nome.capitalize()

# Função para adicionar um item à lista de compras com um valor
def adicionar_item():
    item = input("Digite o nome do item: ")
    item_formatado = formatar_nome(item)
    preco = input("Digite o preço do item: ").replace(',', '.')
    preco = float(preco)
    quantidade = float(input("Digite a quantidade desejada: "))
    quantidade = math.floor(quantidade)  # Pega a parte inteira e arredonda sempre para baixo
    subtotal = preco * quantidade
    lista_de_compras.append({"item": item_formatado, "preco": preco, "quantidade": quantidade, "subtotal": subtotal})
    print(f"{quantidade} {item_formatado}(s) foram adicionados à lista de compras por R${subtotal:.2f}.")

# Função para calcular e exibir o subtotal e o valor total da lista de compras
def calcular_subtotal_e_total():
    subtotal_total = sum(item['subtotal'] for item in lista_de_compras)
    valor_total = subtotal_total
    print(f"\nSubtotal da Lista de Compras: R${subtotal_total:.2f}")
    print(f"Valor total da Lista de Compras: R${valor_total:.2f}")

# Função para exibir a lista de compras
def exibir_lista():
    print("\nLista de Compras:")
    for i, item in enumerate(lista_de_compras, start=1):
        print(f"{i}. {item['quantidade']} {item['item']}(s) por R${item['subtotal']:.2f} cada")

# Função para retirar itens da lista
def retirar_item():
    exibir_lista()
    escolha = input("Digite o número do item que deseja retirar ou '0' para cancelar: ")
    
    if escolha.isdigit():
        index = int(escolha) - 1
        if 0 <= index < len(lista_de_compras):
            quantidade_retirar = float(input("Digite a quantidade que deseja retirar: "))
            quantidade_atual = lista_de_compras[index]['quantidade']

            if quantidade_retirar >= quantidade_atual:
                del lista_de_compras[index]
                print(f"Item removido completamente da lista.")
            else:
                lista_de_compras[index]['quantidade'] -= quantidade_retirar
                lista_de_compras[index]['subtotal'] -= lista_de_compras[index]['preco'] * quantidade_retirar
                print(f"{quantidade_retirar} {lista_de_compras[index]['item']}(s) retirado(s) da lista.")

        else:
            print("Número do item inválido. Nenhum item foi removido.")
    else:
        print("Entrada inválida. Nenhum item foi removido.")

# Função principal
def main():
    print("Bem-vindo ao Programa de Lista de Compras!")

    while True:
        print("\nOpções:")
        print("1. Adicionar item à lista")
        print("2. Exibir lista de compras")
        print("3. Calcular e exibir subtotal e valor total")
        print("4. Retirar item da lista")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "1":
            adicionar_item()
        elif escolha == "2":
            exibir_lista()
        elif escolha == "3":
            calcular_subtotal_e_total()
        elif escolha == "4":
            retirar_item()
        elif escolha == "5":
            print("Saindo do programa. Obrigado por usar a Lista de Compras!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
 