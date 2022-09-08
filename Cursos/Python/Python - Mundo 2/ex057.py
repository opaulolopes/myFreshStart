# Validação de Dados
genero = str(input('Digite seu gênero [M/F/Outro]: ')).strip().upper()
while genero not in 'MFO':
    genero = str(input('Dados inválidos. Por favor, informe seu gênero: ')).strip().upper()
if 'O' in genero:
    genero = 'Outro'
print(f'Sexo {genero} registrado com sucesso.')
