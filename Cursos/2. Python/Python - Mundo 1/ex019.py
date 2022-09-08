# Sorteando um item na lista
from random import choice

n1 = input('Primeirx alunx: ')
n2 = input('Segundx alunx: ')
n3 = input('Terceirx alunx: ')
n4 = input('Quartx alunx: ')
alunos = [n1, n2, n3, n4]
sorteado = choice(alunos)
print(f'O aluno escolhido foi {sorteado}.')
