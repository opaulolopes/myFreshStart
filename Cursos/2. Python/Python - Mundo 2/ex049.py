# Tabuada v.2.0
n = int(input('Digite um número para conhecer sua tabuada: '))
print('='*12)
for cont in range(1, 11):
    print('{} x {:2} = {}'.format(n, cont, n*cont))
print('='*12)

# Código que fiz pela primeira vez (awn, que fofo)
# n = int(input('Digite um número para conhecer sua tabuada: '))
# print('=' * 13)
# multiplicador=0
# for tab in range(1, 11):
#     multiplicador += 1
#     print('{} x {:2} = {}'.format(n, multiplicador, n * multiplicador))
# print('=' * 13)
