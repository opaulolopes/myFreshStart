# Analisador de Textos
nome = str(input('Digite seu nome completo:')).strip()
print('1. Seu nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print('2. Seu nome com todas as letras minúsculas é {}.'.format(nome.lower()))
print('3. O nome possui {} letras ao todo (sem considerar espaços).'.format(len(nome) - nome.count(' ')))
print('4. O primeiro nome possui {} letras.'.format(nome.find(' ')))
div = nome.split()
print('4. O primeiro nome possui {} letras.'.format(len(div[0])))
