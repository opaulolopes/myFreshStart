# Analisando Triângulo v1.0
r1 = float(input('Digita o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
retasmenores = (r1 + r2 + r3) - max(r1, r2, r3)
retamaior = max(r1, r2, r3)
if retasmenores > retamaior:
    print('As retas apresentadas podem formar um triângulo.')
else:
    print('As retas apresentadas não podem formar um triângulo.')
