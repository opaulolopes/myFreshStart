# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando o nome {}:'.format(nome))
print('Seu primeiro nome é {}.'.format(nome[:nome.find(' ')]))
print('Seu último nome é {}.'.format(nome[nome.rfind(' ') + 1:]))
