# Separando dígitos de um número
valor = int(input('Digite um valor de 0 a 9999: '))
num = str(valor)
uni = valor // 1 % 10
dez = valor // 10 % 10
cen = valor // 100 % 10
mil = valor // 1000 % 10
print('Analisando o número {}:'.format(valor))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
