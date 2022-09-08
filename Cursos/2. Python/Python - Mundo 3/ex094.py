# Unindo dicionários e listas
pessoa = dict()
registros = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['genero'] = str(input('Gênero: [M/F] ')).strip().upper()[0]
        if pessoa['genero'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa["idade"]
    registros.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    pessoa.clear()
    if continuar in 'N':
        break
print('-'*30)
print(f'Foram cadastradas {len(registros)} pessoas.')
media = soma / (len(registros))
print(f'A média de idade do grupo é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for mulheres in registros:
    if mulheres['genero'] in 'F':
        print(f'{mulheres["nome"]} ', end='')
print('\nLista de pessoas que estão acima da média:')
for acima in registros:
    if acima["idade"] > media:
        for k, v in acima.items():
            print(f'{k}: {v} | ', end='')
