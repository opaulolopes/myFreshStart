# Aumentos múltiplos
sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250:
    print('Com o aumento, o salário de R${:.2f} passa a ser de R${:.2f}.'.format(sal, 1.1 * sal))
else:
    print('Com o aumento, o salário de R${:.2f} passa a ser de R${:.2f}.'.format(sal, 1.15 * sal))
