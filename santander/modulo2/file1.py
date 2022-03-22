# Métodos de Lista

nomes_paises = ["Brasil", "Argentina", "Japão", "China", "Canadá"]

print("Tamanho da lista:", len(nomes_paises))

print(nomes_paises[1:2])

lista_capitais = []

lista_capitais.append("Brasilia")
lista_capitais.append("Buenos Aires")
lista_capitais.append("Pequim")
lista_capitais.append("Bogotá")

print(lista_capitais)

lista_capitais.insert(2, "Paris")
print(lista_capitais)

lista_capitais.remove("Buenos Aires")
print(lista_capitais)

removido = lista_capitais.pop(2)
print(lista_capitais, " - ", removido)

jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)

jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)

rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)

digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)


# Métodos de Tupla

nomes_paises = ("Brasil", "Argentina", "China", "Canadá", "Japão")
print(nomes_paises, type(nomes_paises))

nomes_paises = "Brasil", "Argentina", "China", "Canadá", "Japão"
print(nomes_paises, type(nomes_paises))

nomes_estado = "São Paulo",
print(nomes_estado, type(nomes_estado))

print(nomes_paises[0])

b, a, c, ca, j = nomes_paises

print(a,b,c)

print(*nomes_paises)