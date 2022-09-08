# Maior e menor da sequência
lista = []
for cont in range(1, 6):
    peso = (float(input('Digite o peso da {}ª pessoa: '.format(cont))))
    lista += [peso]
print('O maior peso foi {:.1f}kg e o menor peso foi {:.1f}kg.'.format(max(lista), min(lista)))
