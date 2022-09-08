# Soma ímpares múltiplos de três
soma = 0
for contador in range (0, 501):
    if contador % 3 == 0:
        soma += contador
print(soma)
