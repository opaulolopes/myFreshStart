# Análise de dados do grupo
total18 = homens = mulheres20 = 0
while True:
    print('''-------------------\nCADASTRE UMA PESSOA\n-------------------''')
    idade = int(input('Idade: '))
    if idade >= 18:
        total18 += 1
    genero = cont = ' '
    while genero not in 'MF':
        genero = str(input('Gênero [M/F]: ')).strip().upper()
    if genero == 'M':
        homens += 1
    if idade < 20 and genero == 'F':
        mulheres20 += 1
    print('-' * 19)
    while cont not in 'NS':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'''----- FIM DO PROGRAMA -----
Total de pessoas com mais de 18 anos: {total18}.
Ao todo, temos {homens} homens cadastrados.
Existem {mulheres20} mulheres com menos de 20 anos.''')
