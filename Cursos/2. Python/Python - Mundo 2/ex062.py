# Super Progressão Aritmética v3.0
continuar = 10
total = 0
contador = 1
an = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('-' * 13)
while continuar != 0:
    total += continuar
    while contador <= total:
        print(f'{contador:2}º termo: {an}')
        an += r
        contador += 1
    continuar = int(input('Quantos termos você quer mostrar a mais? [0 para sair] '))
