# Custo da Viagem
dist = float(input('Digite a distância da viagem: '))
if dist <= 200:
    print('Para {}km de viagem, o preço da passagem é de R${:.2f}.'.format(dist, 0.5*dist))
else:
    print('Para {}km de viagem, o preço da passagem é de R${:.2f}.'.format(dist, 0.45*dist))
