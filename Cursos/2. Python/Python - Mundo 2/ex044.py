# Gerenciador de Pagamentos
preco = float(input('Qual é o valor do produto? R$'))
pag = int(input('''Escolha a forma de pagamento:
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
>>> '''))
if pag == 1:
    print('Pagando à vista no dinheiro ou no cheque, seu produto tem um desconto de 10% e sai por R${:.2f}.'.format(
        preco * (1 - 0.1)))
elif pag == 2:
    print('Pagando à vista no cartão, seu produto tem um desconto de 5% e sai por R${:.2f}.'.format(preco * (1 - 0.05)))
elif pag == 3:
    print('Parcelando em 2x de R${:.2f} no cartão sem juros, seu produto sai pelo valor original de R${:.2f}.'.format(
            preco/2, preco))
elif pag == 4:
    totalparc = int(input('Quantas parcelas? '))
    parc = 1.2 * preco / totalparc
    print('Parcelando em {}x de R${:.2f} no cartão com 20% de juros, seu produto sai por R${:.2f}.'.format(totalparc,
            parc, 1.2 * preco))
else:
    print('Opção inválida. Tente novamente!')
