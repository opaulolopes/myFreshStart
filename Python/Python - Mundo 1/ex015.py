# Aluguel de Carros
km = float(input('Digite a quantidade de km percorridos pelo carro alugado: '))
tempo = int(input('Por quantos dias este carro foi alugado? '))
total = 60 * tempo + 0.15 * km
print(f'O preço total a ser pago para {km}km rodados em {tempo} dias é R${total:.2f}.')
