# Classificando Atletas
from datetime import date

nasc = int(input('Qual é o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('Este ano, o atleta completa {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM'.format(idade))
elif idade <= 14:
    print('Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('Classificação: JUNIOR'.format(idade))
elif idade <= 20:
    print('Classificação: SÊNIOR'.format(idade))
else:
    print('Classificação: MASTER'.format(idade))
