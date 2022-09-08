# Catetos e Hipotenusa
from math import hypot

co = float(input('Digite a medida do cateto oposto do triângulo retângulo: '))
ca = float(input('Digite a medida do cateto adjacente do triângulo retângulo: '))
hi = hypot(co, ca)
print(f'A hipotenusa do triângulo retângulo de lados {co:.2f} e {ca:.2f} equivale a {hi:.2f}.')
