# Criando um menu
pessoa = dict()
registros = list()
while True:
    titulo('MENU PRINCIPAL')
    menu()
    try:
        opc = int(input('\033[92mSua opção: \033[m'))
    except:
        print('ERRO!')
    if opc == 1:
        titulo('PESSOAS CADASTRADAS')
        for c in registros:
            print(f'{c["Nome"]:<23}{c["Idade"]} anos')
    elif opc == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        pessoa.clear()
        pessoa['Nome'] = nome
        pessoa['Idade'] = idade
        registros.append(pessoa.copy())
        print(f'Registro de {nome} adicionado.')
    elif opc == 3:
        titulo('Saindo do sistema... Até logo!')
        break
