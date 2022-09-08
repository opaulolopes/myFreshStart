# Tratando vários valores v1.0
cont = soma = 0
num = int(input('Digite um número inteiro [Digite 999 para sair]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro [Digite 999 para sair]: '))
print(f'Foram digitados {cont} números e a soma entre eles é igual a {soma}.')
