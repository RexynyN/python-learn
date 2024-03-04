import base64
from math import ceil
import json
import os
from binascii import a2b_base64
import sys
import re


def print_help():
    print("\nComo usar:")
    print("python dataurl.py convert <caminho da pasta> <nome arquivo (opcional)>")
    print("python dataurl.py revert <caminho do arquivo json>")


def natural_sort(l):
    print("Ordenando os arquivos do diretório...")
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def read_dir(path):
    try:
        print("Listando diretório...")
        dir_files = os.listdir(path)
    except FileNotFoundError:
        print("\nDiretório não existe ou está em formato incorreto, tente novamente")
        exit()
    except IndexError:
        print_help()
        exit()

    return natural_sort(dir_files)


def image_to_data_url(path, filename):
    item = {}
    ext = filename.split('.')[-1]
    prefix = f'data:image/{ext};base64,'
    with open(path + "\\" + filename, 'rb') as f:
        img = f.read()

    item['link'] = prefix + base64.b64encode(img).decode('utf-8')
    item['file'] = filename

    return item


def data_url_to_image(data, filename):
    if(data.find(",") != -1):
        data = data.split(",")[-1]
        if(not os.path.isdir(os.getcwd() + "\\output")):
            os.mkdir(os.getcwd() + "\\output")

        binary_data = a2b_base64(data)
        with open(os.getcwd() + "\\output\\" + filename, 'wb') as f:
            f.write(binary_data)
    else:
        print("Opa, deu algo de errado.")


def main():
    args = sys.argv

    if(args[1] == "convert"):
        path = args[2]
        data = read_dir(path)
        json_data = []

        for file in data:
            json_data.append(image_to_data_url(path, file))

        if(3 < len(args)):
            name_file = args[3].split(".")[-1]
        else:
            name_file = "output"

        output_path = f"{path}\\imgdata"
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        limit = 100
        # Mostra em quantos arquivos de numero "limit" de imagens vai caber
        threshold = ceil(len(json_data) / limit)
        start = 0
        for i in range(0, threshold):
            end = limit * (i + 1)
            aux = json_data[start : end]
            print(f"Criando arquivo com imagens de {start + 1} até {end}")
            with open(f"{output_path}\\{name_file} - {i + 1}.json", 'w', encoding='utf-8') as f:
                json.dump(aux, f, ensure_ascii=False, indent=4)
                
            start = end
        
        print(f"Os arquivos estão no caminho: {path}/imgdata")

    elif(args[1] == "revert"):
        with open(args[2], "r") as read_file:
            data = json.load(read_file)
            for data in data:
                data_url_to_image(data['link'], data['file'])
    else:
        print_help()


if __name__ == "__main__":
    main()
