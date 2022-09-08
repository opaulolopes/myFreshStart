# Lista composta e análise de dados
dado = []
registros = []
menorPeso = maiorPeso = 0
continuar = 'S'
while continuar != 'N':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if len(registros) == 0:
        menorPeso = maiorPeso = dado[1]
    if menorPeso >= dado[1]:
        menorPeso = dado[1]
    if maiorPeso <= dado[1]:
        maiorPeso = dado[1]
    registros.append(dado[:])
    dado.clear()
print('-'*33)
print(f'Ao todo, você cadastrou {len(registros)} pessoas.')
print(f'O maior peso foi de {maiorPeso}kg, de ', end='')
for p in registros:
    if p[1] == maiorPeso:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menorPeso}kg, de ', end='')
for p in registros:
    if p[1] == menorPeso:
        print(f'{p[0]} ', end='')
