# Sorteando uma ordem na lista
from random import shuffle

n1 = input('Primeirx alunx: ')
n2 = input('Segundx alunx: ')
n3 = input('Terceirx alunx: ')
n4 = input('Quartx alunx: ')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print(f'A ordem de apresentação será {alunos}.')
