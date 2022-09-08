# Contando vogais em Tupla
texto = ('Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit')
for palavra in texto:
    print(f'\nNa palavra {palavra.upper()}, temos a(s) vogal(is) ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
