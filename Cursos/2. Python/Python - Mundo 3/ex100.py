# Funções para sortear e somar
from random import choice

def sorteia():
    sorteio = list()
    while True:
        sort = choice(numeros)
        if sort in sorteio:
            pass
        else:
            sorteio.append(sort)
        if len(sorteio) == 5:
            break
    print(f'Os 5 números sorteados foram {sorteio}.')
    return sorteio

def somaPar():
    sorteio = sorteia()
    soma = 0
    for num in sorteio:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {sorteio}, temos {soma}.')


# Programa principal
numeros = list()
sorteio = ()
cont = 0
while True:
    cont += 1
    num = int(input(f'Digite o {cont}º valor: '))
    numeros.append(num)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if continuar in 'N':
        break
somaPar()
