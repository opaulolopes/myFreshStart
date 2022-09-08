def leiaDinheiro(n):
    valido = False
    while not valido:
        entrada = str(input(n)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[0:31mERRO: Preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(numero):
    ok = False
    while True:
        n = (str(input(numero))).strip()
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Tente novamente.\033[m')
        if ok:
            break
    return n
