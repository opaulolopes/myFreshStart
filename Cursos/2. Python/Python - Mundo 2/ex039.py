# Alistamento Militar
from datetime import date

ano = int(input('Para saber se você deve se alistar, digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    tempo = 18 - idade
    print('Você precisa se alistar quando completar 18 anos. Ainda faltam {} anos.'.format(tempo))
elif idade == 18:
    print('Você precisa se alistar este ano!')
else:
    tempo = idade - 18
    print(
        'O ano do seu alistamento já passou há {} anos. Caso ainda não tenha se alistado, deve se apresentar '
        'urgentemente!'.format(
            tempo))
