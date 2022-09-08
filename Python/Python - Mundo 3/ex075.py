# Análise de dados em uma Tupla
num = tuple(int(input('Digite um número inteiro: ')) for cont in range(5))
print(f'Você digitou os números {num}.')
n9 = num.count(9)
print(f'O valor 9 apareceu {n9} vezes.')
if 3 in num:
    p3 = num.index(3) + 1
    print(f'O valor 3 foi digitado pela primeira vez na {p3}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares digitados foram ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares, end=' ')
