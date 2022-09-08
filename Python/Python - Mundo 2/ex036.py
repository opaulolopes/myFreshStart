# Aprovando Empréstimo
print('=' * 31)
valor = float(input('Olá, qual é o valor da casa? R$'))
salario = float(input('Qual é o salário mensal do comprador? R$'))
tempo = int(input('Em quanto tempo, em anos, o comprador pretende pagar a casa? '))
print('-=' * 16)
prestacao = valor / (tempo * 12)
if prestacao > salario * 0.3:
    print(
        'Infelizmente você não pode financiar esta casa. O valor da prestação, de R${:.2f} excede 30% do salário '
        'mensal do comprador, de R${:.2f}.'.format(
            prestacao, salario))
else:
    print('Parabéns! Você conseguiu o financiamento. Sua parcela é de R${:.2f}.'.format(prestacao))
