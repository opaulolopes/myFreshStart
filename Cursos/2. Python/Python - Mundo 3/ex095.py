# Aprimorando os Dicionários
desempenho = dict()
gols = list()
jogador = list()
while True:
    desempenho.clear()
    desempenho['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
    gols.clear()
    for partida in range(1, partidas + 1):
        gols.append(int(input(f'- Número de gols na Partida {partida}: ')))
    desempenho['gols'] = gols.copy()
    desempenho['total'] = sum(gols)
    jogador.append(desempenho.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if continuar in 'N':
        break
print('-'*40)
print(f'{"CÓD.":<5}{"NOME":<15}{"GOLS":<15}{"TOTAL":<5}')
print('-'*40)
for cod, val in enumerate(jogador):
    print(f'{cod:<5}{val["nome"]:<15}{str(val["gols"]):<15}{val["total"]:<5}')
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 p/ sair] '))
    if busca >= len(jogador):
        print(f'ERRO! Não existe jogador {busca}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador[busca]["nome"]}: ')
        for cont, gols in enumerate(jogador[busca]['gols']):
            print(f'No jogo {cont + 1} fez {gols} gols.')
    if busca == 999:
        break
print('PROGRAMA ENCERRADO.')
