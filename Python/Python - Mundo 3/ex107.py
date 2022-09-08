# Módulos e Pacotes
from moeda import metade, dobro, aumentar, diminuir
num = float(input('Digite um valor: R$'))
print(f'A metade de {num:.2f} é {metade(num):.2f}.')
print(f'O dobro de {num:.2f} é {dobro(num):.2f}.')
print(f'Aumentando 10%, temos {aumentar(num, 10):.2f}.')
print(f'Reduzindo 13%, temos {diminuir(num, 13):.2f}.')
