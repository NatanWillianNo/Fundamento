# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange
computador = randrange(5)
print('=== Jogo da Adivinhação v.1.0 ===')
print('Vamos jogar um jogo?')
print('Escolha um número de 0 a 5')
palpite = int(input('Coloque o número aqui: '))
if palpite == computador:
    print('Você ganhou!')
    print('Eu pensei no mesmo número que você: {}'.format(computador))
else:
    print('Você perdeu')
    print('Eu pensei no {}'.format(computador))
print('Obrigado por jogar! Volte sempre')

# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
print('=== Radar eletrônico ===')
print('Bem-vindo ao Radar')
vel = float(input('Qual foi a velocidade do carro?: '))
limite = int(input('Qual é o limite de velocidade?: '))
multa = float(input('Por cada kilômetro ultrapassado, quanto custa a multa?: R$ '))
valor = (vel - limite)*multa
if vel > limite:
    print('Você foi multado!')
    print('O valor da sua multa é de R${:.2f}'.format(valor))
else:
    print('Dessa vez você não foi multado!')
print('Dirija com Segurança e se beber não dirija')

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('=== Verificador de Paridade ===')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))

# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('=== SERVIÇO DE VIAGENS ===')
print('Olá, seja bem-vindo ao sistema de cálculo de viagens')
dest = str(input('Pra onde você deseja ir?: '))
said = str(input('De onde você está partindo?: '))
print('Ótima escolha! Adoramos ir pra {}'.format(dest))
print('Para viagens menores de 200 kilômetros cobraremos R$0,50 por kilômetro rodado! Para viagens maiores ou iguais a essa distância cobraremos apenas R$ 0,40 por kilômetro')
kmdest = str(input('Qual é a distância de {} até {}'.format(dest, said)))
if kmdest > 200:
    valorviagem = kmdest*0.5
else: 
    valorviagem = kmdest*0.45
print('O valor da viagem que você deseja fazer é: {} '.format(valorviagem))
print('Não se esqueça que você vai para {} e está saindo de {}'.format(dest, said))

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('=== Análise de Ano Bissexto ===')
ano = int(input('Coloque um ano pra verificar se ele é bisessexto ou não?: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# Pergunta o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))
if salario > 1250.00:
    aumento = salario * 0.10  
else:
    aumento = salario * 0.15  
novo_salario = salario + aumento
print(f"Salário antes do aumento: R${salario:.2f}")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("Verificador de Triângulo")
print('Lembrando que a Condição de existência de um triângulo é')
print('Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.')
ladoa = float(input('Coloque o primeiro lado do seu triângulo: '))
ladob = float(input('Coloque o segundo lado do seu triângulo: '))
ladoc = float(input('Coloque o terceiro e último lado desse triângulo: '))
modulo_ab = abs((ladoa - ladob))
modulo_ac = abs((ladoa - ladoc))
modulo_bc = abs((ladob - ladoc))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    print('Os valores fornecidos formam um triângulo.')
    if ladoa == ladob == ladoc:
        print('Este é um triângulo equilátero.')
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print('Este é um triângulo isósceles.')
    else:
        print('Este é um triângulo escaleno.')
else:
    print('Os valores fornecidos não formam um triângulo.')

