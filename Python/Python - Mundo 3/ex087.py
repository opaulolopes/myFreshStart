# Matriz em Python
pares = soma3 = maior2 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        if col == 2:
            soma3 += matriz[lin][col]
        if matriz[1]:
            maior2 = max(matriz[1])
print('-'*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[  {matriz[lin][col]:^5}  ]', end='')
    print()
print('-'*30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior2}.')
