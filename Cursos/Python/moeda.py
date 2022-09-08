def aumentar(n=0, pu=0, f=False):
    res = (1 + pu / 100) * n
    return res if f is False else moeda(res)


def diminuir(n=0, pd=0, f=False):
    res = (1 - pd / 100) * n
    return res if f is False else moeda(res)


def dobro(n=0, f=False):
    res = 2 * n
    return res if f is False else moeda(res)


def metade(n=0, f=False):
    res = n / 2
    return res if f is False else moeda(res)


def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, pu, pd):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{pu}% de redução: \t{aumentar(n, pu, True)}')
    print(f'{pd}% de redução: \t{diminuir(n, pd, True)}')
    print('-' * 30)
