# num = (2, 5, 9, 1)
# num[2] = 3
# print(num)
# O print dará erro, pois tuplas são imutáveis
num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 > Não funcionará. Para adicionar o valor 7 na posição 4, fazemos:
num.append(7)
# A seguir, a lista fica em ordem decrescente
num.sort(reverse=True)
# A seguir, é inserido o valor 0 na posição 2.
num.insert(2, 0)
# A seguir, deletamos o último valor da lista.
num.pop()
# A seguir, buscamos remover um valor sem saber se ele existe na lista.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número.')
print(num)
print(f'Esta lista tem {len(num)} elementos.')

print('--' * 20)

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

print('--' * 20)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

print('--' * 20)

a = [2, 3, 4, 7]
# Listas ficam ligadas entre si para sempre:
b = a
# Para quebrar a ligação, faz-se:
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
