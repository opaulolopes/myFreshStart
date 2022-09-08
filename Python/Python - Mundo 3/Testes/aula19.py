# Dicionários
pessoas = {'nome': 'Paulo', 'sexo': 'M', 'idade': '24'}
# Como o dicionário está dentro de aspas simples, devem ser usadas aspas duplas:
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# keys se refere ao cabeçalho:
print(pessoas.keys())
# values se refere aos dados de cada cabeçalho:
print(pessoas.values())
# items se refere a tudo:
print(pessoas.items())
# Acessar chaves, valores e itens por laços:
# Para cada uma das chaves:
for k in pessoas.keys():
    print(k)
# Para cada chave e valor dos itens. Em tuplas e listas, utilizamos enumerate:
for k, v in pessoas.items():
    print(f'{k} = {v}')
# Para apagar um item:
del pessoas['sexo']
print(pessoas)
# Para modificar um valor:
pessoas['nome'] = 'Sérgio'
pessoas['peso'] = 70
print(pessoas)
print('-'*50)
# Criar um dicionário dentro de uma lista:
brasil = []
# Criar dois dicionários, um para cada estado:
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# Adicionar os dicionários à lista:
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
# Coordenada do valor de um dicionário:
print(brasil[0]['uf'])
print('-'*50)
# As listas são ligadas para sempre. Para fazer a cópia do elemento, o comando [:] não funciona:
estado = dict()
brasil2 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(estado.copy())
print(brasil2)
# Para cada estado:
for e in brasil2:
    print(e)
    # A mesma coisa, mais bonitinho:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()
