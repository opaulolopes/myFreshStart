# Função para Fatorial
def fatorial(numero, show=False):
    fat = 1
    for f in range(numero, 0, -1):
        if show:
            print(f, end='')
            if f > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= f
    if numero >= 0:
        print('{}'.format(fat))


# Programa Principal
fatorial(5, show=True)
