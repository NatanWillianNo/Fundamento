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
