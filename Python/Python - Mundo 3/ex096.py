# Função que calcula área
def area(l, c):
    A = l*c
    print(f'A área de um terreno de {larg:.1f}x{comp:.1f}m é de {A}m².')


# Programa Principal
larg = float(input('Largura do terreno retangular [m]: '))
comp = float(input('Comprimento do terreno retangular [m]: '))
area(larg, comp)
