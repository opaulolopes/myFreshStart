# Boletim com listas compostas
boletim = []
total = 0
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    total += 1
    if continuar in 'N':
        break
print('-'*25)
print(f'{"Nº.":<5}{"NOME":<14}{"MÉDIA":<6}')
print('-'*25)
for num, aluno in enumerate(boletim):
    print(f'{num:<5}{aluno[0]:<14}{aluno[2]:<6}')
while True:
    print('-'*25)
    individual = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if individual == 999:
        break
    print(f'Notas de {boletim[individual][0]} são {boletim[individual][1]}.')
