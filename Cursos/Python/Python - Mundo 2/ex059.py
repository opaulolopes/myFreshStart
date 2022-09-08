# Criando um Menu de Opções
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('--' * 12)
menu = 1
while 1 <= menu <= 4:
    menu = int(input('''Escolha uma opção:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    Sua opção é: '''))
    print('--' * 12)
    if menu == 1:
        print('A soma entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, n1 + n2))
        print('--' * 12)
    elif menu == 2:
        print('O produto entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, n1 * n2))
        print('--' * 12)
    elif menu == 3:
        print('O maior número entre {:.1f} e {:.1f} é {:.1f}.'.format(n1, n2, max(n1, n2)))
        print('--' * 12)
    elif menu == 4:
        n1 = float(input('Certo! Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print('--' * 12)
    elif menu == 5:
        print('')
    else:
        print('Opção inválida. Por favor, digite um número válido: ')
