# Maior e Menor valores na Lista
lista = []
maior = []
menor = []
for posicao in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {posicao}: ')))
print('--' * 20)
print(f'Você digitou os valores {lista}.')
for c, v in enumerate(lista):
    if v == max(lista):
        maior.append(c)
        print(f'O maior valor digitado foi {max(lista)} na(s) posição(ões) {maior}.')
    elif v == min(lista):
        menor.append(c)
        print(f'O menor valor digitado foi {min(lista)} na(s) posição(ões) {menor}.')
