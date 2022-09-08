# Cálculo do Fatorial
num = int(input('Digite um número inteiro: '))
print('Calculando {}! = '.format(num), end='')
fat = num
fatorial = 1
while fat > 0:
    fatorial *= fat
    print('{} '.format(fat), end='')
    print('x ' if fat > 1 else '= ', end='')
    fat -= 1
if num >= 0:
    print('{}'.format(fatorial))
else:
    print('Não existe fatorial de número negativo.')
