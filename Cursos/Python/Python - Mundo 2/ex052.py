# Números primos
total = 0
valor = int(input('Digite um número inteiro: '))
for contador in range (1, valor + 1):
    if valor % contador == 0:
        total += 1
        print('\033[33m', end='')
    else:
        print('\033[m', end='')
    print(contador, end=' ')
print(f'\n\033[mO número {valor} foi divisível {total} vezes.')
if total == 2:
    print(f'Então {valor} é um número primo.')
else:
    print(f'Então {5} não é um número primo.')
