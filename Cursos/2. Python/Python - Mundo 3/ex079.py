# Valores únicos em uma Lista
cont = 'S'
lista = []
while cont == 'S':
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não será adicionado.')
        cont = str(input('Quer continuar? [S/N] ')).upper()
    else:
        print('Valor adicionado com sucesso...')
        cont = str(input('Quer continuar? [S/N] ')).upper()
        lista.append(num)
print('--'*20)
lista.sort()
print(f'Você adicionou os valores {lista}.')
