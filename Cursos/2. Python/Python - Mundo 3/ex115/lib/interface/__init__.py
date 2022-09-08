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


def linha(tam=30):
    print('-' * tam)


def cabecalho(t):
    linha()
    print(f'{t:^30}')
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - \033[94m{item}\033[m')
        c += 1
    linha()
    opc = leiaInt('\033[92mSua opção: \033[m')
    return opc


def cad(nome, idade):
    print(f'{nome} \t\t\t {idade}')
