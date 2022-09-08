# Funções para votação
from datetime import date


def voto(nasc):
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
