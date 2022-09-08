# Vários números com flag
cont = soma = 0
while True:
    num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')
