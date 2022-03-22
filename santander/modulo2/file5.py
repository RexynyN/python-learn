
# def hello ():
#     print("Hello, world!")

# def calcula_media (valor1, valor2, valor3):
#     return (valor1 + valor2 + valor3)/3

# def calcula_media (valor1=0, valor2=0, valor3=0):
#     return (valor1 + valor2 + valor3)/3

# hello()
# print(calcula_media(5, 10, 7))

# print("Olá", end=" ")
# print("; Breno!")

# print(calcula_media())


# def somatorio(lista):
#     soma = 0
#     for item in lista:
#         soma = soma + item
#     return soma

# numeros = [1, 2, 3, 4, 5]
# soma_dos_numeros = somatorio(numeros)
# print("A soma dos elementos da lista vale: ", soma_dos_numeros)

# if somatorio(numeros) > 50:
#     print("Que soma grande!")
# else:
#     print("Que soma pequena!")


def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem


print(calcula_media(10, 9, 8, margem=0.3))

def print_info (**kwargs):
    print(kwargs, type(kwargs))

print_info(nome="Breno", sobrenome="Nogueira")