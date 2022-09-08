# Função que descobre o maior
def maior(*num):
    total = len(numeros)
    if numeros == [0]:
        total = 0
    print('-' * 34)
    print('Analisando os valores digitados...')
    print(f'{numeros} | Foram informados {total} valores ao todo.')
    print(f'O maior valor informado foi {max(numeros)}.')
    print('-' * 34)


# Programa Principal
numeros = list()
while True:
    num = int(input('Informe um valor inteiro: '))
    numeros.append(num)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if continuar in 'N':
        break
maior(num)
