# Funções (Parte 1)
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print('-' * 30)


# O código das linhas 2 a 15 pode ser reescrito por:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=1, b=2)
print('-' * 30)


# Se não souber quantos parâmetros existirão, podemos desempacotar(*):
def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# Utilizando funções em listas:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)
