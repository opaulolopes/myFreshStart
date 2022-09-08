# Índice de Massa Corporal
import time

print('=' * 35)
peso = float(input('Para calcular o IMC, digite seu peso (em kg): '))
alt = float(input('Digite sua altura (em m): '))
print('=' * 35)
print('Analisando seu peso e sua altura...')
imc = peso / alt ** 2
time.sleep(1)
print('O IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso!')
elif imc < 25:
    print('Você está dentro do Peso Ideal.')
elif imc < 30:
    print('Você está no Sobrepeso.')
elif imc < 40:
    print('Você está na Obesidade.')
else:
    print('Cuidado! Você está na Obesidade mórbida.')
