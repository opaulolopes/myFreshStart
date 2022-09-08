# Maior e menor valores em Tupla
from random import randint

# Dear Jesus, what the fuck?
sorteio = tuple(randint(1, 5) for cont in range(5))
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')
