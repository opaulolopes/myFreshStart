def aumentar(n, pu, f=False):
    moeda(n, f)
    return (1 + pu / 100) * n


def diminuir(n, pd, f=False):
    moeda(n, f)
    return (1 - pd / 100) * n


def dobro(n, f=False):
    moeda(n, f)
    return 2 * n


def metade(n, f=False):
    moeda(n, f)
    return n / 2


def moeda(n, f=False):
    if f:
        return f'R${n:.2f}'
    else:
        return n


def resumo(n, pu, pd):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(n, True):<10}')
    print(f'{"Dobro do preço:":<20}{moeda(dobro(n), True):<10}')
    print(f'{"Metade do preço:":<20}{moeda(metade(n), True):<10}')
    print(f'{pu}{"% de redução:":<18}{moeda(aumentar(n, pu), True):<10}')
    print(f'{pd}{"% de redução:":<18}{moeda(diminuir(n, pd), True):<10}')
    print('-' * 30)
