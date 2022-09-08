# Lista de Preços com Tupla
total = 0
produtos = ('Ovo', 14.99, 'Pimentão', 2.42, 'Banana prata', 3.84, 'Abacate', 9.18, 'Leite', 6.49, 'Creme de leite',
            3.29, 'Queijo Mussarela', 8.49, 'Apresuntado', 6.99, 'Linguiça', 15.99, 'TOTAL')
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-'*38)
for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R$ {produtos[item]:5.2f}')
        total += produtos[item]
print(f'R$ {total:5.2f}')
print('-'*38)
