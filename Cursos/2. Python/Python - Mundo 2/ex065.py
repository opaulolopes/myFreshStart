# Maior e Menor valores
cont = num = soma = media = 0
lista = []
while num != 999:
    cont += 1
    num = int(input('Digite o {}º número inteiro [Digite 999 para sair]: '.format(cont)))
    soma += num
    lista += [num]
media = (soma - 999) / (cont - 1)
lista.remove(999)
print('A média dos valores digitados é igual a {}.'.format(media))
print('O maior valor foi {} e o menor valor foi {}.'.format(max(lista), min(lista)))
