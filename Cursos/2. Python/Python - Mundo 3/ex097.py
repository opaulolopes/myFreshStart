# Um print especial
def escreva(texto):
    espac = len(texto) + 5
    print('*' * espac)
    print(f'{texto:^{espac}}')
    print('*' * espac)


# Programa Principal
escreva('Paulo Lopes')
escreva('Curso em Vídeo - Python (Mundo 3)')
escreva('Marília Mendonça')
