# GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep

print('~*' * 10)
jogador = int(input('''Para começar a jogar Jokenpô contra mim, escolha o primeiro movimento:
[ 1 ] Para pedra
[ 2 ] Para papel
[ 3 ] Para tesoura
Então, qual é a sua jogada? '''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('~*' * 10)
lista = {1: '💎',
         2: '📜',
         3: '✂'}
comp = randint(1, 3)
if jogador == comp:
    print('\033[1:33mVocê: {}\033[m'.format(lista[jogador]))
    print('\033[1:33mEu: {}\033[m'.format(lista[comp]))
    print('~*' * 10)
    print('\033[1:97:43mEMPATE!\033[m')
elif jogador == 1 and comp == 2 or jogador == 2 and comp == 3 or jogador == 3 and comp == 1:
    print('\033[:31mVocê: {}\033[m'.format(lista[jogador]))
    print('\033[:32mEu: {}\033[m'.format(lista[comp]))
    print('~*' * 10)
    print('\033[:97:42mEU VENCI!\033[m')
elif jogador == 1 and comp == 3 or jogador == 2 and comp == 1 or jogador == 3 and comp == 2:
    print('\033[:32mVocê: {}\033[m'.format(lista[jogador]))
    print('\033[:31mEu: {}\033[m'.format(lista[comp]))
    print('~*' * 10)
    print('\033[:97:42mVOCÊ VENCEU!\033[m')
else:
    print('Opção inválida! Tente novamente.')
