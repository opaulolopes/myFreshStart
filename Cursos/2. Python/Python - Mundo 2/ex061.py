# Progressão Aritmética v2.0
an = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = 1
while termo <= 10:
    print('{}º termo: {}'.format(termo, an))
    an += r
    termo += 1
