# Estatísticas em produtos
print('-----------------\nLOJA DO PAULOPES\n-----------------')
cont = total = caros = menor = 0
lista = []
barato = ''
while True:
    continua = ' '
    prod = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        caros += 1
    if cont == 1 or menor > preco:
        menor = preco
        barato = prod
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-'*17)
print(f'''O total a pagar é R${total:.2f}
{caros} produtos custam mais de R$1000,00.
O produto mais barato foi {barato} que custa R${menor:.2f}.''')
