# Analisando Triângulos v2.0

# Este é o código que eu fiz antes da correção
# r1 = float(input('Digita o comprimento da primeira reta: '))
# r2 = float(input('Digite o comprimento da segunda reta: '))
# r3 = float(input('Digite o comprimento da terceira reta: '))
# retasmenores = (r1 + r2 + r3) - max(r1, r2, r3)
# retasmaiores = max(r1, r2, r3)
# if retasmenores > retasmaiores and r1==r2==r3:
#     print('As retas apresentadas podem formar um triângulo equilátero.')
# elif retasmenores > retasmaiores and (r1==r2 or r1==r3 or r2==r3):
#     print('As retas apresentadas podem formar um triângulo isósceles.')
# elif retasmenores > retasmaiores and r1!=r2 or r1!=r3 or r2!=r3:
#     print('As retas apresentadas podem formar um triângulo escaleno.')
# else:
#     print('As retas apresentadas não podem formar um triângulo.')

r1 = float(input('Digita o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
retasmenores = (r1 + r2 + r3) - max(r1, r2, r3)
retasmaiores = max(r1, r2, r3)
if retasmenores > retasmaiores:
    if r1 == r2 == r3:
        print('As retas apresentadas podem formar um triângulo equilátero.')
    elif r1 != r2 != r3 != r1:
        print('As retas apresentadas podem formar um triângulo escaleno.')
    else:
        print('As retas apresentadas podem formar um triângulo isósceles.')
else:
    print('As retas apresentadas não podem formar um triângulo.')
