# Jogo do Par ou Ímpar
from random import randint

total = 0
print('==' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('==' * 12)
while True:
    jogador = int(input('Digite um número inteiro: '))
    paridade = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    comp = randint(0, 10)
    soma = jogador + comp
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('--' * 12)
    print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} deu {resultado}.')
    print('--' * 12)
    if paridade == resultado[0:1]:
        print('Você GANHOU!')
        print('=='*12)
        print('Vamos jogar novamente...', end=' ')
        total += 1
    else:
        print('Você PERDEU!')
        print('==' * 12)
        print(f'GAME OVER! Você venceu {total} vezes consecutivas.')
        break

# CÓDIGO DO PROFESSOR
# from random import randint
#
# total = 0
# while True:
#     jogador = int(input('Digite um número inteiro: '))
#     comp = randint(0, 10)
#     soma = jogador + comp
#     paridade = ' '
#     while paridade not in 'PI':
#         paridade = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} ', end='')
#     print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
#     if paridade == 'P':
#         if soma % 2 == 0:
#             print('Você GANHOU!')
#             total += 1
#         else:
#             print('Você PERDEU!')
#             break
#     elif paridade == 'I':
#         if soma % 2 == 1:
#             print('Você GANHOU!')
#             total += 1
#         else:
#             print('Você PERDEU!')
#             break
#     print('Vamos jogar novamente...', end=' ')
# print(f'GAME OVER! Você venceu {total} vezes consecutivas.')
