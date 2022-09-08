# Tabuada v3.0
while True:
    print('--' * 31)
    num = int(input('Quer ver a tabuada de qual valor? [Número negativo p/ encerrar] '))
    print('--' * 31)
    cont = 1
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont:>2} = {num * cont}')
        cont += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
