# Jogo de Adivinhação v2.0
from random import randint
from time import sleep

tentativas = 0
print('--' * 32)
valor = int(input('Vou pensar em um número de 0 a 10. Você consegue adivinhar qual? '))
print('--' * 32)
sleep(0.5)
print('Hmmmmmm, serasse...')
sleep(0.5)
sorteio = randint(0, 10)
while valor != sorteio:
    tentativas += 1
    valor = int(input('Ihhhhh, você errou :/\nEu não pensei em {}. Tente novamente: '.format(valor)))
    print('--' * 32)
    sleep(1)
print('MORTO, SIM! você acertou!!! Olha, você tentou {} vezes.'.format(tentativas + 1))
