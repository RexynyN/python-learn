# arquivo = open('santander/modulo3/dom_casmurro.txt', 'r', encoding='utf-8')
# texto = arquivo.read()
# print(texto)
# arquivo.close()


# arquivo = open('santander/modulo3/dom_casmurro.txt', 'r', encoding='utf-8')
# linha = arquivo.readline()

# while linha != '':
#     print(linha, end='')
#     linha = arquivo.readline()

# arquivo.close()

# arquivo = open('santander/modulo3/dom_casmurro.txt', 'r', encoding='utf-8')
# linha = arquivo.readline()

# for linha in arquivo:
#     print(linha, end='')
# arquivo.close()

# with open('santander/modulo3/dom_casmurro.txt', 'r', encoding='utf-8') as arquivo:
#     texto = arquivo.read()
#     print(texto)

with open('arquivo.txt', "w", encoding='utf-8') as arquivo:
    arquivo.write("Boa noite a todos!\n")
    arquivo.write("Eu sou maravilhoso!\n")
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)
with open('arquivo.txt', "a", encoding='utf-8') as arquivo:
    arquivo.write("Sério mesmo!\n")
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)