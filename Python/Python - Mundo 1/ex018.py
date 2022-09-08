# Seno, Cosseno e Tangente
from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo {ang} possui seno igual a {sen:.2f}.')
print(f'O ângulo {ang} possui cosseno igual a {sen:.2f}.')
print(f'O ângulo {ang} possui tangente igual a {sen:.2f}.')
