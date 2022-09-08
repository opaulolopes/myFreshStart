# Progressão Aritmética v1.0
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for pa in range(0, 10):
    print('{}'.format(a1 + r * pa), end=' → ')
print('Fim da PA de 10 termos')
