# Rada eletrônico
v = int(input('Qual é a velocidade do carro? '))
if v > 80:
    multa = 7 * (v - 80)
    print('O carro foi multado em R${:.2f}!'.format(multa))
else:
    print('O carro não foi multado.')
