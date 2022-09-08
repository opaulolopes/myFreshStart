# Comparando números
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('O primeiro valor ({}) é maior do que o segundo valor ({}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) é maior do que o primeiro valor ({}).'.format(n2, n1))
else:
    print('Os dois valores são iguais!')
