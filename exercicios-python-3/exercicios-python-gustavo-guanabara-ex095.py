# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média de {}: '.format(aluno["nome"])))
if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] <= 5.9:  
    aluno['situação'] = 'Recuperação'
else: 
    aluno['situação'] = 'Aprovado'
print('Nome:', aluno['nome'])
print('Média:', aluno['media'])
print('Situação:', aluno['situação'])
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
import time
while True:
    num_jogadores = int(input("Digite a quantidade de jogadores: "))
    jogadores = [f'Jogador {i}' for i in range(1, num_jogadores + 1)]
    resultados = {}
    for jogador in jogadores:
        resultado = random.randint(1, 6)
        print(f'{jogador} tirou: {resultado}')
        resultados[jogador] = resultado
        time.sleep(2)
    while True:
        resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1])
        print('\nResultados finais em ordem:')
        for jogador, resultado in resultados_ordenados:
            print(f'{jogador}: {resultado}')
        empates = [jogador for jogador, resultado in resultados_ordenados if resultado == resultados_ordenados[0][1]]
        if len(empates) == len(jogadores):
            print('\nTodos os jogadores empataram. Novo sorteio para desempate:')
            for jogador in jogadores:
                resultado = random.randint(1, 6)
                print(f'{jogador} tirou: {resultado}')
                resultados[jogador] = resultado
                time.sleep(2)
        elif len(empates) == 1:
            print(f'\nO vencedor é {empates[0]}!')
            break
        else:
            print(f'\nHouve um empate entre {", ".join(empates)}. Novo sorteio para desempate:')
            for jogador in empates:
                resultado = random.randint(1, 6)
                print(f'{jogador} tirou: {resultado}')
                resultados[jogador] = resultado
                time.sleep(2)
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        break

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

