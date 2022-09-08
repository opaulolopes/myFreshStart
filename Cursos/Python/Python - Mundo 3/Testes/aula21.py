help(input)
print('**' * 30)
print(input.__doc__)
print('**' * 30)


def contador(i, f, p):
    """
    -> Faz uma contagem
    """


help(contador)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
# Para retornar vários valores em uma mesma linha
print('*' * 30)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
print('*' * 30)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
par(num)
if par(num):
    print('É par!')
else:
    print('Não é par!')
