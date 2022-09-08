# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = []
print('------ VALORES SORTEADOS ------')
for cont in range(0, 4):
    jogo[f'Jogador {cont + 1}'] = randint(1, 6)
for k, v in jogo.items():
    sleep(0.6)
    print(f'{k} tirou {v}')
print('------ RANKING DOS JOGADORES ------')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.6)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
