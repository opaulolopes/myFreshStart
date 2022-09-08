# Palpites para a Mega Sena
from random import sample
from time import sleep

jogo = ''
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
total = int(input('Quantos jogos você quer que eu sorteie? '))
for mega in range(0, total):
    jogo = sample(range(0, 61), 6)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print(f'------ SORTEANDO {total} JOGOS ------')
for cont in range(1, total + 1):
    print(f'Jogo {cont}: {jogos[cont - 1]}')
    sleep(0.5)
