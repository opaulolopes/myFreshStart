# Cadastro de Trabalhador em Python
from datetime import date

resultado = {}
resultado['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
resultado['idade'] = date.today().year - nasc
resultado['cart'] = int(input('Nº Carteira de Trabalho: '))
if resultado['cart'] != 0:
    resultado['cont'] = int(input('Ano de contratação: '))
    tempo= date.today().year - resultado['cont']
    resultado['sal']= float(input('Salário: R$'))
    resultado['aposent'] = (resultado['cont'] + 35) - nasc
print('-'*30)
print(f'{resultado["nome"]} tem {resultado["idade"]} anos.')
if resultado['cart'] != 0:
    print(f'CTPS (0 se não tiver): {resultado["cart"]} / Contratação: {resultado["cont"]} / Salário: R${resultado["sal"]:.2f}')
    print(f'Idade de aposentadoria: {resultado["aposent"]} anos')
