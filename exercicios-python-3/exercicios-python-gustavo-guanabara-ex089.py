# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# Atribuindo listas vazias para variável de dados temporario e para lista dados pessoas
dadosPessoa = []
maior = menor = 0
while True:
    nome = input('NOME: ').strip().capitalize()
    peso = float(input('PESO: '))
    print('-' * 30)
    if len(dadosPessoa) == 0:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    dadosPessoa.append({'nome': nome, 'peso': peso})
    continuar = input('Continuar? [S/N]: ').strip().upper()
    while continuar not in ('S', 'N'):
        print('\nValor incorreto, informe a opção correta...')
        continuar = input('Continuar? [S/N]: ').strip().upper()
    print('-' * 30)
    if continuar == 'N':
        print('Programa finalizado...')
        print('-' * 30)
        break
print(f'\nPESSOAS CADASTRADAS: {len(dadosPessoa)}')
print(f'MAIOR PESO FOI DE {maior}Kg --> ', end='')
for pessoa in dadosPessoa:
    if pessoa['peso'] == maior:
        print(f'{pessoa["nome"]}', end=' ')
print()
print(f'MENOR PESO FOI DE {menor}Kg --> ', end='')
for pessoa in dadosPessoa:
    if pessoa['peso'] == menor:
        print(f'{pessoa["nome"]}', end=' ')

# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
pares = []
impares = []
for _ in range(7):
    valor = int(input("Digite um valor numérico: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Valores pares em ordem crescente:", sorted(pares))
print("Valores ímpares em ordem crescente:", sorted(impares))

# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
matriz = []
for linha in range(3):
    valor = []
    for coluna in range(3):
        valor.append(int(input(f'Informe o valor para [{linha}, {coluna}]: ')))
    matriz.append(valor)
print()
print('-' * 21 + f'\n{"MATRIZ":^22}\n' + '-' * 21)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.  
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i+1}, {j+1}]: '))
print('\nMatriz:')
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end='')
    print()
soma_pares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
print(f'\nA) A soma de todos os valores pares é: {soma_pares}')
soma_terceira_coluna = sum(matriz[i][2] for i in range(3))
print(f'B) A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
maior_segunda_linha = max(matriz[1])
print(f'C) O maior valor da segunda linha é: {maior_segunda_linha}')

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

sistema_de_notas = []
alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    alunos.append([nome, nota1, nota2])
print("\n=== Boletim ===")
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)
    print(f"{nome}: Média = {media:.2f}")
aluno_escolhido = input("\nDigite o nome do aluno para ver as notas individuais (ou 'sair' para encerrar): ")
while aluno_escolhido.lower() != 'sair':
    encontrado = False
    for aluno in alunos:
        if aluno[0].lower() == aluno_escolhido.lower():
            encontrado = True
            print(f"\nNotas de {aluno_escolhido}: {aluno[1:]}")
            break
    if not encontrado:
        print(f"\nAluno '{aluno_escolhido}' não encontrado.")
    aluno_escolhido = input("\nDigite o nome do aluno para ver as notas individuais (ou 'sair' para encerrar): ")

