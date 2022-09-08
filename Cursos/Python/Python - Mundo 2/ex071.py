# Simulador de Caixa Eletrônico
print('''==============\nBANCO LOPINHO\n==============''')
saque = int(input('Qual é o valor a ser sacado? R$'))
c50 = saque//50
c20 = (saque-c50*50)//20
c10 = (saque-c50*50-c20*20)//10
c1 = (saque-c50*50-c20*20-c10*10)//1
print(f'Total de {c50} cédulas de R$50')
print(f'Total de {c20} cédulas de R$20')
print(f'Total de {c10} cédulas de R$10')
print(f'Total de {c1} cédulas de R$1')
print(f'==============\nVolte sempre ao BANCO LOPINHO! Tenha um bom dia!')

# CÓDIGO DO COLEGA
# saque = int(input('Qual é o valor a ser sacado? R$'))
# for nota in [50, 20, 10, 1]:
#     print(f'Total de {saque // nota} cédulas de R${nota}')
#     saque %= nota
