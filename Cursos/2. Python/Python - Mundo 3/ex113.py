# Tratamento de Erros e Exceções
def leiaInt(numero):
    while True:
        try:
            i = int(input(numero))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return i


def leiaFloat(numero):
    while True:
        try:
            r = float(input(numero).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return r


inte = leiaInt('Digite um valor inteiro: ')
real = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {inte} e o real foi {real}.')
