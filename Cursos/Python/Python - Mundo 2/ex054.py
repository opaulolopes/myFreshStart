# Grupo da Maioridade
from datetime import date

menores = 0
for cont in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cont)))
    idade = date.today().year - nasc
    if idade < 21:
        menores += 1
print('{} pessoas são maiores e {} pessoas são menores de idade.'.format(7 - menores, menores))
