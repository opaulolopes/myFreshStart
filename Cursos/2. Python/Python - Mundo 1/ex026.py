# Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra "A" (sem acentos) aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" (sem acentos) aparece pela primeira vez na {}ª posição.'.format(frase.find('A')+1))
print('A letra "A" (sem acentos) aparece pela última vez na {}ª posição.'.format(frase.rfind('A')+1))
