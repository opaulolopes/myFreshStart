# Jogo da Adivinhação v.10
from random import randint
from time import sleep

print('*-'*32+'*')
valor = int(input('Vou pensar em um número de 0 a 5. Você consegue adivinhar qual? '))
print('*-'*32+'*')
sleep(1)
print('Hmmmmmm, serasse...')
sleep(3)
sorteio = randint(0, 5)
if valor == sorteio:
    print('MORTO, você acertou. Meus parabéns!!!')
else:
    print('Ihhhhh, você errou :/\nEu pensei em {} e não em {}.'.format(sorteio, valor))
print('*-'*13, end='*')
