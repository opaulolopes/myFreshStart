# Sequência de Fibonacci v1.0
t1 = 0
t2 = 1
cont = 3
num = int(input('Digite um número inteiro: '))
print(f'{t1} → {t2}', end='')
while cont <= num:
    t = t1 + t2
    print(f' → {t}', end='')
    cont += 1
    t1 = t2
    t2 = t
