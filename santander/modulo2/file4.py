cidades = ["São Paulo", "Londres", "Tóquio", "Paris"]

for nome in cidades:
    print(nome)

cidades = ("São Paulo", "Londres", "Tóquio", "Paris")

for nome in cidades:
    print(nome)


cidade = {
    "nome": "São Paulo",
    "estado": "São Paulo",
    "area_km2": 1512,
    "populacao_milhoes": 12.18
}

for chave in cidade:
    print(f'{chave} : {cidade[chave]}')

cidades = ["São Paulo", "Londres", "Tóquio", "Paris"]

for pos in range(len(cidades)):
    cidades[pos] = 'Rio de Janeiro'

print(cidades)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))


# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
    print(numero)
    # este exemplo imprime os números de 0 a 9, de um em um

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
    print(numero)
    # este exemplo imprime os números de 1 a 10, de um em um

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
    print(numero)
    # este exemplo imprime os ímpares positivos menores do que 20
    # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20

# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
    print(numero)
    #Imprimindo os números de 1 a 10 em ordem decrescente