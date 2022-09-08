lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.count(9))
print(c.index(8))
print(c.index(4))
print(c.index(2))  # Pega a primeira ocorrência
print(c.index(5, 2))
print(c.index(4))
del a
print(a)
