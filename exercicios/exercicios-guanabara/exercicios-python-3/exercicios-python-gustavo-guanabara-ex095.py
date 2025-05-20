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

from datetime import datetime
nome = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
carteira_trabalho = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))
cadastro = {
    'Nome': nome,
    'Ano de Nascimento': ano_nascimento,
    'Idade': datetime.now().year - ano_nascimento
}
if carteira_trabalho != 0:
    ano_contratacao = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o salário: "))
    cadastro['Carteira de Trabalho'] = carteira_trabalho
    cadastro['Ano de Contratação'] = ano_contratacao
    cadastro['Salário'] = salario
    anos_contribuicao_minima = 35
    idade_aposentadoria = (ano_contratacao + anos_contribuicao_minima) - ano_nascimento
    cadastro['Idade de Aposentadoria'] = idade_aposentadoria
print("\nCadastro completo:")
for chave, valor in cadastro.items():
    print(f"{chave}: {valor}")

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

nome = input("Digite o nome: ")
partidas = int(input('Quantas partidas {} jogou: '.format(nome)))
cadastro_fut = {
    'Nome': nome,
    'Partidas': partidas,
    'Gols': []
}
total_gols = 0
for partida in range(partidas):
    gols_partida = int(input(f'Quantos gols {nome} fez na partida {partida + 1}: '))
    cadastro_fut['Gols'].append(gols_partida)
    total_gols += gols_partida
cadastro_fut['Total de Gols'] = total_gols
print('\nCadastro do Jogador:')
print(f"Nome: {cadastro_fut['Nome']}")
print("Gols em cada partida:")
for partida, gols in enumerate(cadastro_fut['Gols'], start=1):
    print(f"Partida {partida}: {gols} gols")
print(f"Total de gols no campeonato: {cadastro_fut['Total de Gols']}")

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

lista_pessoas = []
total_pessoas = 0
soma_idades = 0
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    idade = int(input("Digite a idade da pessoa: "))
    pessoa = {
        'Nome': nome,
        'Sexo': sexo,
        'Idade': idade
    }
    lista_pessoas.append(pessoa)
    total_pessoas += 1
    soma_idades += idade
if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas
    mulheres = [pessoa['Nome'] for pessoa in lista_pessoas if pessoa['Sexo'] == 'F']
    acima_da_media = [pessoa['Nome'] for pessoa in lista_pessoas if pessoa['Idade'] > media_idade]
    print("\nResultados:")
    print(f"A) Quantidade de pessoas cadastradas: {total_pessoas}")
    print(f"B) Média de idade: {media_idade:.2f}")
    print(f"C) Lista de mulheres: {mulheres}")
    print(f"D) Lista de pessoas acima da média de idade: {acima_da_media}")
else:
    print("Nenhuma pessoa cadastrada.")

# Aprimore o exercício dos jogadores para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista_jogadores = []
while True:
    print("\n1 - Cadastrar novo jogador")
    print("2 - Visualizar detalhes de um jogador")
    print("3 - Exibir ranking de jogadores por gols")
    print("4 - Exibir ranking de jogadores por aproveitamento")
    print("5 - Sair")
    opcao = input("Escolha uma opção (1 a 5): ")
    if opcao == '1':
        nome = input("Digite o nome do jogador: ").upper()
        partidas = int(input(f'Quantas partidas {nome} jogou: '))
        cadastro_fut = {
            'Nome': nome,
            'Partidas': partidas,
            'Gols': []
        }
        total_gols = 0
        for partida in range(partidas):
            gols_partida = int(input(f'Quantos gols {nome} fez na partida {partida + 1}: '))
            cadastro_fut['Gols'].append(gols_partida)
            total_gols += gols_partida
        cadastro_fut['Total de Gols'] = total_gols
        lista_jogadores.append(cadastro_fut)
        print(f'\nJogador {nome} cadastrado com sucesso!')
    elif opcao == '2':
        nome_busca = input("Digite o nome do jogador que deseja visualizar: ").upper()
        encontrado = False
        for jogador in lista_jogadores:
            if jogador['Nome'] == nome_busca:
                encontrado = True
                print('\nDetalhes do Jogador:')
                print(f"Nome: {jogador['Nome']}")
                print("Gols em cada partida:")
                for partida, gols in enumerate(jogador['Gols'], start=1):
                    print(f"Partida {partida}: {gols} gols")
                print(f"Total de gols no campeonato: {jogador['Total de Gols']}")
                aproveitamento = (jogador['Total de Gols'] / jogador['Partidas']) * 100 if jogador['Partidas'] > 0 else 0
                print(f"Aproveitamento: {aproveitamento:.2f}%")
                break
        if not encontrado:
            print(f"Jogador {nome_busca} não encontrado.")
    elif opcao == '3':
        ranking_gols = sorted(lista_jogadores, key=lambda x: x['Total de Gols'], reverse=True)
        print("\nRanking de jogadores por gols:")
        for i, jogador in enumerate(ranking_gols, start=1):
            print(f"{i}. {jogador['Nome']} - {jogador['Total de Gols']} gols")
    elif opcao == '4':
        ranking_aproveitamento = sorted(lista_jogadores, key=lambda x: (x['Total de Gols'] / x['Partidas']) * 100 if x['Partidas'] > 0 else 0, reverse=True)
        print("\nRanking de jogadores por aproveitamento:")
        for i, jogador in enumerate(ranking_aproveitamento, start=1):
            aproveitamento = (jogador['Total de Gols'] / jogador['Partidas']) * 100 if jogador['Partidas'] > 0 else 0
            print(f"{i}. {jogador['Nome']} - {aproveitamento:.2f}%")
    elif opcao == '5':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha entre 1 e 5.")