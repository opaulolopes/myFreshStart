# Dicionário em Python
from math import ceil

resultado = dict()
resultado['nome'] = str(input('Nome: ')).strip().capitalize()
resultado['media'] = ceil(float(input(f'Média de {resultado["nome"]}: ')))
# Para arredondar a nota para cima (por exemplo: 6.95):
if resultado['media'] >= 7:
    resultado['situacao'] = 'APROVADO'
elif 5 <= resultado['media'] < 7:
    resultado['situacao'] = 'RECUPERAÇÃO'
else:
    resultado['situacao'] = 'REPROVADO'
print(f'A média de {resultado["nome"]} é {resultado["media"]:.1f}.')
print(f'Situação: {resultado["situacao"]}')
