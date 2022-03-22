import csv

# with open("brasil_covid.csv", "r", encoding="utf-8") as arquivo:
#     leitor = csv.reader(arquivo)
#     header = next(leitor)
#     for line in leitor:
#         if(float(line[2]) > 1): 
#             print(line)

with open("users.csv", "w", encoding="utf-8", newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Breno', 'Nogueira', 'breno@hotmail.com', 'Masculino'])
with open("users.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for line in leitor:
        print(line) 



with open('tabelaExemplo.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo, delimiter = ';', lineterminator = '\n') #criando um escritor
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escritor.writerows(lista) # writerows escreve cada "sublista" da lista como uma linha
with open('tabelaExemplo.csv', "r") as arquivo:
    leitor = csv.reader(arquivo, delimiter = ';', lineterminator = '\n') #criando um leitor
    print("O conteúdo do arquivo é:")
    print(leitor)
    for linha in leitor:
        print(linha)


# Podemos também trabalhar com dicionários, nos quais a primeira linha é lida como a chave e as demais são os respectivos valores:

with open('email.csv', 'r') as emails:
    leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
    for linha in leitor:
        print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho
with open('names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name'] # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho

    writer.writeheader() # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})
