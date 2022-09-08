# Verificando as primeiras letras de um texto
cidade = str(input('Digite o nome de uma cidade:')).strip().title().split()
print('O nome da cidade começa com "Santo?" [TRUE/FALSE]: {}'.format('Santo' == cidade[0]))
