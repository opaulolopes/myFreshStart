# Função de Contador
from time import sleep


def progarit(inicio, fim, passo):
    cont = 1
    while True:
        sleep(0.25)
        s = inicio + (cont - 1) * passo
        print(s, end=' ')
        cont += 1
        if cont > (fim - inicio) / passo + 1:
            break
    print('FIM!')


def contador(inicio, fim, passo):
    print('-' * 35)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        progarit(inicio, fim, passo)
    if inicio > fim:
        passo *= -1
        progarit(inicio, fim, passo)


# Programa Principal
contador(1, 10, 1)
contador(80, 40, 4)
print('-' * 35)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
