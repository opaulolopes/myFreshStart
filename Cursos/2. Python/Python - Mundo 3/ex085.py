# Listas com pares e ímpares
valores = [[], []]
num = 0
for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
        valores[0].sort()
    else:
        valores[1].append(num)
        valores[1].sort()
print('-'*20)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
