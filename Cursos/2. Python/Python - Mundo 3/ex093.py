# Cadastro de Jogador de Futebol
desempenho = dict()
gols = list()
desempenho['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
desempenho['partidas'] = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
for cont in range(1, desempenho['partidas'] + 1):
    gols.append(int(input(f'Número de gols na partida {cont}: ')))
desempenho['total'] = sum(gols)
print('-'*30)
print(f'{desempenho["nome"]} jogou {desempenho["partidas"]} partidas.')
for i, v in enumerate(gols):
    print(f'→ Na partida {i + 1}, {desempenho["nome"]} fez {v} gols.')
print(f'Foi um total de {desempenho["total"]} gols.')
