# Analisando e gerando Dicionários
def notas(*n, sit=False):
    desempenho = dict()
    desempenho['total'] = sum(n)
    desempenho['maior'] = max(n)
    desempenho['menor'] = min(n)
    desempenho['media'] = sum(n) / len(n)
    for v in desempenho.values():
        print(f'{v:<17.1f}', end='')
    if sit:
        if desempenho['media'] >= 7:
            print(f'{"BOA":<17}')
        elif 5 <= desempenho['media'] < 7:
            print(f'{"RAZOÁVEL":<17}')
        else:
            print(f'{"RUIM":<17}')
    else:
        print('-')


# Programa Principal
print('-' * 76)
print(f'{"QTD. DE NOTAS":<17}{"MAIOR NOTA":<17}{"MENOR NOTA":<17}{"MÉDIA DA TURMA":<17}{"SITUAÇÃO":<17}')
print('-' * 76)
notas(3.5, 2, 6.5, 2, 7, 4)
print('-' * 76)
