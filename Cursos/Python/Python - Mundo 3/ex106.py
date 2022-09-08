# Interactive helping system in Python
def titulo(cor=0, cabecalho=''):
    tamanho = 2 * len(cabecalho)
    print(f'\033[{cor}m-' * tamanho)
    print(f'{cabecalho:^{tamanho}}')
    print('-' * tamanho)
    print('\033[m', end='')


def ajuda(busca=''):
    while True:
        biblioteca = str(input(busca)).strip().lower()
        if biblioteca == 'fim':
            break
        titulo(104, f'Acessando o manual do comando \'{biblioteca}\'')
        print('\033[7m')
        help(biblioteca)
        print('\033[m', end='')


# Programa Principal
titulo(46, 'SISTEMA DE AJUDA PyHELP')
ajuda('Função ou biblioteca > ')
titulo(101, 'PROGRAMA ENCERRADO!')
