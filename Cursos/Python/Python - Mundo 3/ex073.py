# Tuplas com Times de Futebol
personagens = 'Joyce', 'Hopper', 'Mike', 'Eleven', 'Dustin', 'Lucas', 'Nancy', 'Jonathan', 'Karen', 'Brenner', 'Will',\
              'Max', 'Steve', 'Billy', 'Bob', 'Owens', 'Robin', 'Erica', 'Murray', 'Eddie'
pos = personagens.index('Eleven')+1
print('=='*25)
print(f'Lista de personagens principais de Stranger Things: {personagens}')
print('=='*25)
print(f'Os 5 primeiros personagens são {personagens[:5]}.')
print('=='*25)
print(f'Os últimos 4 colocados são {personagens[-4:]}')
print('=='*25)
print(f'Personagens em ordem alfabética: {sorted(personagens)}')
print('=='*25)
print(f'A Eleven está na {pos}ª posição.')
