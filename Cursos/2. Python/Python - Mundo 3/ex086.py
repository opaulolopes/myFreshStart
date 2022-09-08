# Matriz em Python
matriz = []
x = y = 0
for cont in range(1, 10):
    valor = int(input(f'Digite um valor para [{x}, {y}]: '))
    matriz.append(valor)
    y += 1
    if y > 2:
        y = 0
    if cont % 3 == 0:
        x += 1
print('-'*30)
for cont in range(1, 10):
    print(f'[  {matriz[cont - 1]}  ] ', end='')
    if cont > 0 and cont % 3 == 0:
        print('')

# Solução do professor com listas compostas
# # Matriz em Python
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for lin in range(0, 3):
#     for col in range(0, 3):
#         matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
# print('-'*30)
# for lin in range(0, 3):
#     for col in range(0, 3):
#         print(f'[  {matriz[lin][col]:^5}  ]', end='')
#     print()
