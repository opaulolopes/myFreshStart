# Extraindo dados de uma Lista
cont = 'S'
lista = []
while cont == 'S':
    num=int(input('Digite um valor: '))
    cont=str(input('Quer continuar? [S/N] ')).strip().upper()
    lista.append(num)
lista.sort(reverse=True)
print('--'*20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
