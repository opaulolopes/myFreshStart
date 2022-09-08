# Aquele clássico da Média
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Meus parabéns! Você foi APROVADO com média {}.'.format(media))
elif media < 5:
    print('Você está REPROVADO! Sua média foi {}.'.format(media))
else:
    print('Você está em RECUPERAÇÃO! Sua média foi {}.'.format(media))
