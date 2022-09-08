# Ficha do Jogador
def ficha(nome='Desconhecido', gols=0):
    if gols == '0':
        gols = 0
    return f'O Jogador {nome} fez {gols} gol(s) no campeonato.'


# Programa Principal
nome = str(input('Nome do Jogador: ')).strip().capitalize()
gols = str(input('Número de gols: '))
print(ficha())
