# Detector de Palíndromo
from time import sleep

frase = str(input('Digite uma frase: ')).strip().lower().split()
semespaco = ''.join(frase)
inverso = ''
for caracter in range(len(semespaco) - 1, -1, -1):
    inverso += semespaco[caracter]
    print(inverso)
    sleep(0.25)
if semespaco == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
