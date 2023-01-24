import os
import sys
from reportlab.pdfgen.canvas import Canvas
from PIL.Image import open as img_open
from base64 import b64decode
from json import load as json_load
import re
from shutil import rmtree
import requests
import shutil
# from PyPDF2 import PdfFileReader

def get_images(src, max):
    img_path = os.getcwd() + "\\__img_data__\\"

    if not os.path.isdir(img_path):
        os.mkdir(img_path)

    for i in range(1, max + 1):
        image_url = src.replace("??", str(i))
        filename = str(i) + ".jpg"
        
        print("Baixei " + filename)
        r = requests.get(image_url, stream = True)
        r.raw.decode_content = True

        with open(img_path + filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    
    return img_path

def natural_sort(l):
    print("Ordenando os arquivos do diretório...")
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def print_help():
    print("\nComo usar:")
    print("python imgpdf.py -folder <caminho da pasta> <nome arquivo (opcional)>")
    print("python imgpdf.py -dataurl <caminho do arquivo json>  <nome arquivo (opcional)>")
    print("*para usar a funcionalidade de dataurl, o arquivo json deve ser o gerador pelo dataurl.py\n")


def dataurl_to_image(path):
    try:
        print("Lendo arquivo...")
        with open(path, "r") as read_file:
            data = json_load(read_file)
    except FileNotFoundError:
        print("\nO arquivo não existe, tente novamente")
        exit()
    except Exception as e:
        print("\nAlgo deu errado na leitura do arquivo, certifique-se que o arquivo é um json válido")
        exit()

    os.mkdir(os.getcwd() + "\\__img_data__")

    print("Criando diretório auxiliar de imagens...")
    for file in data:
        if(file['link'].find(",") != -1):
            link = file['link'].split(",")[-1]

            binary_data = b64decode(link)
            with open(os.getcwd() + "\\__img_data__\\" + file['file'], 'wb') as f:
                f.write(binary_data)

    return os.getcwd() + "\\__img_data__"

def img_to_pdf(files, path, name):
    print("Criando arquivo...")
    doc = Canvas(name)

    print("Adicionando imagens ao arquivo...")
    for img in files:
        if(os.path.isdir(path + "\\" +  img) == False):
            file_path = path + "\\" + img 

            try:
                image = img_open(file_path)
            except Exception:
                print("*** Tentamos abrir o arquivo \"" + img + "\", e não foi possível. Pulando... ***")
                continue

            doc.setPageSize(image.size)
            doc.drawImage(file_path, 0, 0, image.size[0], image.size[1], mask="auto")
            doc.showPage()

    print("Imagens adicionadas")
    image = ""
    
    print("Salvando PDF...")
    doc.save()

    if(os.path.isdir(os.getcwd() + "\\__img_data__")):
        print("Apagando diretório auxiliar...")
        rmtree(os.getcwd() + "\\__img_data__")
    print("Processo terminado!\n\nO PDF está salvo na mesma pasta onde o script está armazenado.")


# ==============
# Main Program 
# ==============

args = sys.argv

if("-h" in args or "-help" in args):
    print_help()
    exit()

if("-folder" in args  and "-dataurl" in args):
    print("Escolha entre o modo '-folder' e o '-dataurl', não é possível escolher os dois")
    exit()

if("-folder" in args):
    try:
        print("Listando diretório...")
        dir_files = os.listdir(args[2])
    except FileNotFoundError:
        print("\nDiretório não existe ou está em formato incorreto, tente novamente")
        exit()
    except IndexError:
        print_help()
        exit()

    dir_files = natural_sort(dir_files)

    # Checks if the name of file is given in the args list
    if(3 < len(args)):
        name_file = args[3].split(".")[-1] + ".pdf"
    else:
        name_file = "output.pdf"

    img_to_pdf(dir_files, args[2], name_file)

elif("-dataurl" in args):
    try:
        path = dataurl_to_image(args[2])
    except IndexError:
        print_help()
        exit()
    
    print("Listando diretório...")
    dir_files = os.listdir(path)
    dir_files = natural_sort(dir_files)

    # # Checks if the name of file is given in the args list
    # if(3 < len(args)):
    #     name_file = args[3] + ".pdf"
    # else:
    name_file = "output.pdf"
    img_to_pdf(dir_files, path, name_file)
elif("-web" in args):
    try:
        path = get_images(args[2], int(args[3]))
    except IndexError:
        print_help()
        exit()
    
    print("Listando diretório...")
    dir_files = os.listdir(path)
    dir_files = natural_sort(dir_files)

    # Checks if the name of file is given in the args list
    if(len(args) > 3):
        name_file = args[4] + ".pdf"
    else:
        name_file = "output.pdf"

    img_to_pdf(dir_files, path, name_file)
else:
    print_help()

# pdf = PdfFileReader("purple.pdf")

# print(str(pdf.getNumPages()) + "\n\n")
# print(pdf.getPage(8).extractText())
