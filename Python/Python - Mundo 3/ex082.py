# Dividindo valores em várias listas
cont = 'S'
lista = []
impar = []
par = []
while cont == 'S':
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os valores digitados são {lista}.')
print(f'Os valores ímpares são {impar}.')
print(f'Os valores pares são {par}')
