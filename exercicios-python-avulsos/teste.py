'''
Dado o escore de alergia de uma pessoa, determine se ela é ou não alérgica a um item específico e liste todas as alergias que ela possui.
Um teste de alergia gera um único escore numérico que contém informações sobre todas as alergias que a pessoa tem (para as quais foram testadas).
A lista de itens (e seus valores) que foram testados é a seguinte:
- ovos (1)
- amendoins (2)
- frutos do mar (4)
- morangos (8)
- tomates (16)
- chocolate (32)
- pólen (64)
- gatos (128)
O programa deve ser capaz de dizer:
Se Tom é alérgico a algum dos alérgenos listados acima e Todas as alergias às quais Tom é alérgico.
'''

print('-'*50)
print('=== Diagnóstico de Alergias ===')
print('-'*50)

score = 0

while True:
    print('- ovos (1)\n- amendoins (2)\n- frutos do mar (4)\n- morangos (8)\n- tomates (16)\n- chocolate (32)\n- pólen (64)\n- gatos (128)')
    alerg = int(input('Quais são os produtos que você é alérgico? '))

    if alerg == 1:
        score += 1
    elif alerg == 2:
        score += 2
    elif alerg == 4:
        score += 4
    elif alerg == 8:
        score += 8
    elif alerg == 16:
        score += 16
    elif alerg == 32:
        score += 32
    elif alerg == 64:
        score += 64
    elif alerg == 128:
        score += 128

    continuar = input('Deseja adicionar mais alérgenos? (s/n) ').lower()
    if continuar != 's':
        break

    if score == 0:
    return "Nada alérgico"
    elif 0 < score <= 4:
        return "Baixo nível de alergia"
    elif 5 <= score <= 32:
        return "Médio nível de alergia"
    elif 33 <= score <= 64:
        return "Alto nível de alergia"
    else:
        return "Muito alto nível de alergia"
print('Você é alérgico a {}')
print(f'Seu escore total de alergias é: {score}')
