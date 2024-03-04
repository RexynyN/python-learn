import os
import re
import random as rand

# TODO
# -Iteration of subfolders
# -Letter Iterations
# -Datetime Iterations

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def expressionParser (expression, count, name, extension):
    expression = str(expression)
    if(expression.find("*") != -1 or expression.find("%") != -1):
        print("Merda")
        expression = expression.replace("*", count)
        expression = expression.replace("%", name)
        return expression + extension
    else:
        return expression + count + extension

def renameDir (type, directory, expression):
    count = 0
    files = []
    try: 
        dir_files = os.listdir(directory)
    except FileNotFoundError:
        print("\nDiretório não existe, tente novamente ;)")
        return 0

    if(type == "1"):
        dir_files = natural_sort(dir_files)
    elif (type == "2"):
        rand.shuffle(dir_files)

    for entry in dir_files:
        if (os.path.isdir(directory + "\\" +  entry) == False):
            newName = expressionParser(expression, str(count + 1), entry.split('.')[0], "." + entry.split('.')[-1])
            files.append({
                'file': entry,
                'newName': newName,
                })
            count += 1
        else:
            continue

    for file in files:
        name = file['file']
        newName = file['newName']
        try:
            os.rename(directory + fr'\{name}', directory + fr'\{newName}')
            print("\"" + name + "\" renomeado para \"" + newName + "\"")
        except FileExistsError: 
            print("O arquivo \"" + newName + "\" já existe, pulando...")
            continue
        except: 
            print("Houve algum erro ao renomear o(s) arquivo(s), verifique as informações e tente novamente")

def renameFolderDir (type, directory, expression):
    print(type, directory, expression)


# ==============
# Main Program 
# ==============


directory = input("Diretório da Pasta: ")
type = input("\n(1) Alfabética \n(2) Aleatória\nTipo de iteração: ")

while type not in ["1", "2"]:
    print("\nOpção inválida, tente novamente")
    type = input("(1) Alfabética \n(2) Aleatória\nTipo de iteração: ")


guard = True
errors = 0
chars = ["<", ">", ":", "\"", "/", "\\", "|", "?"]
while guard:
    expression = input("\n(\"*\" = Substitui por um número de 1 até o máximo de arquivos)\n(% = Substitui pelo nome original do arquivo)\n(Nome não pode conter: <, >, :, \", /, \\, |, ?)\nNome constante para os arquivos: ")
    for x in expression:
        if(x in chars):
            errors += 1
    if(errors == 0):
        guard = False
    else:
        print("\nNome inválido!")

renameDir(type, directory, expression)


