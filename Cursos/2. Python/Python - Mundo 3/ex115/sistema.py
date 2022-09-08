from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        print(f'Registro de {nome} adicionado.')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(1)
