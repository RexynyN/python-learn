

dados_cidade = {
    "nome": "São Paulo",
    "estado": "São Paulo",
    "area_km2": 1512,
    "populacao_milhoes": 12.18
}

print(dados_cidade, type(dados_cidade))

dados_cidade["pais"] = "Brasil"
print(dados_cidade)

print(dados_cidade["nome"])

dados_cidade2 = dados_cidade
dados_cidade2["nome"] = "Santos"
print(dados_cidade)

dados_cidade2 = dados_cidade.copy()
dados_cidade2["nome"] = "Rio de Janeiro"
print(dados_cidade)

novos_dados = {
    "populacao_milhoes": 15,
    "fundacao": "15/01/1554"
}

dados_cidade.update(novos_dados) 
print(dados_cidade)

print(dados_cidade.get("prefeito"))


# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))

'''
Saída:
{'cat': 'gato', 'dog': 'cachorro', 'mouse': 'rato'}
<class 'dict'>
'''

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não

'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
# Saída:dict_values(['gato', 'cão', 'rato'])

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário

itens = dicionario.items()
print(itens)
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])