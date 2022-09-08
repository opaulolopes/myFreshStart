# Analisador completo
soma = maiorIdade = totMul = 0
homemMaisVelho = ''
for contador in range (1, 5):
    print(f'----- {contador}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero [M/F]: ')).strip().upper()
    soma += idade
    if genero == 'M' and idade > maiorIdade:
        maiorIdade = idade
        homemMaisVelho = nome
    if genero == 'F' and idade < 20:
        totMul += 1
media = soma / 4
print('- '* 16)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {homemMaisVelho}.')
print(f'Ao todo são {totMul} mulheres com menos de 20 anos.')
