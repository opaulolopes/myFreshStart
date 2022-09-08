# Lista ordenada com repetições
lista = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    # Abaixo, lê-se: se for o primeiro valor digitado ou se o valor digitado for o último da lista.
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        posicao = 0
        # Abaixo, lê-se: enquanto a posição for menor do que a quantidade de posições da lista.
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} na lista.')
                break
            posicao += 1
print('--' * 20)
print(f'Os valores digitados em ordem foram {lista}.')
