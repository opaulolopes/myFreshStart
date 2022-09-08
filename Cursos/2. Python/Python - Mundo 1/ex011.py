# Pintando Parede
largura = float(input('Digite a largura da parede, em metros: '))
altura = float(input('Digite a altura da parede, em metros: '))
area = largura * altura
tinta = area / 2
print(f'Para pintar a parede, cuja área mede {area}m², são necessários {tinta}L de tinta.')
