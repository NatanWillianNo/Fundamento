# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
print("=== Análise de Nome ===")
nome_pessoa = str(input('Insira seu nome completo: '))
nome_mai = nome_pessoa.upper()
nome_min = nome_pessoa.lower()
num_letras = len(nome_pessoa.replace(" ", ""))  
primeiro_nome = nome_pessoa.split()[0]
num_letras_primeiro_nome = len(primeiro_nome)
print('O seu nome com todas as letras maiúsculas é {}'.format(nome_mai))
print('O seu nome com todas as letras minúsculas é {}'.format(nome_min))
print('O seu nome tem {} letras (sem considerar espaços)'.format(num_letras))
print('O primeiro nome tem {} letras'.format(num_letras_primeiro_nome))

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print('=== Sistema de numeração decimal ===')
num = input('Insira um número de 0 a 9999: ')
unidades = num[0]
dezenas = num[1]
centenas = num[2]
milhares = num[3]
print('As unidades do seu número equivale a: {}'.format(unidades))
print('As dezenas do seu número equivale a {}'.format(dezenas))
print('As centenas do seu número equivale a {}'.format(centenas))
print('Os milhares do seu número equivale a {}'.format(milhares))

# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
print('=== Análise de Cidades ===')
cdd = str(input('Insira o nome de uma cidade: '))
cddarrumado = cdd.lower()  
cddarrumado = cddarrumado.capitalize() 
cddsanto = 'Santo' in cddarrumado or 'Santa' in cddarrumado  
print('Essa cidade tem a palavra Santo/Santa: {}'.format(cddsanto))

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('=== Análise de "Silvas" ===')
nome = str(input('Insira o nome de uma pessoa?: '))
nomearrumado = nome.lower()  
nomearrumado = nomearrumado.replace('s', 'S') 
slv = 'Silva' in nomearrumado
print('O nome inserido tem/não tem o sobrenome Silva: {}'.format(slv))

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('=== Análise de Letra "A" ===')
frase = str(input('Insira uma frase: '))
frasemod = frase.lower()
contar = frasemod.count('a')
encontrar = frasemod.find('a') and frasemod.rfind('a')
print('A frase escolhida tem {} letras A'.format(contar))
print('Ela aparece na {}ª posição e na {}ª posição'.format(encontrar, encontrar)) 

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('=== Análise do Primeiro e Último nome ===')
nomecomp = input('Insira seu nome completo aqui: ')
nomes = nomecomp.capitalize()
nomes = nomecomp.split()
primeiro = nomes[0].capitalize()
ultimo= nomes[-1].capitalize()
print('O seu primeiro nome é: {}'.format(primeiro))
print('O seu último nome é: {}'.format(ultimo))
