import os
import re
import shutil
import inquirer
import requests
from random import randint
from reportlab.pdfgen.canvas import Canvas
from PIL.Image import open as img_open
from base64 import b64decode
from json import load as json_load
# from ebooklib import epub
from shutil import rmtree
# from PyPDF2 import PdfFileReader


class ImageUtils:
    # def __init__(self, *kwargs):
    #     self.path = kwargs["path"]
    #     self.url = kwargs["url"] 

    def get_images(self, path):
        "Lorem Ipsum"

    def get_web_images(self, src, shift):
        img_path = os.getcwd() + "\\__img_data__\\"

        if(not os.path.isdir(img_path)):
            os.mkdir(img_path)

        if isinstance(shift, (int, str)):
            shift = range(1, int(shift) + 1)

        for i in shift:
            image_url = src.replace("??", str(i))

            sheesh = image_url.split(".")
            shoosh = sheesh[-2].split("/")[-1]

            filename = f"{shoosh}.{sheesh[-1]}"

            self.request_image(image_url, img_path + filename)

            print("Baixei " + filename)

        return img_path


    def request_image(self, image_url, img_path):
        while True:
            try:
                r = requests.get(image_url, stream=True)
                r.raise_for_status()
                r.raw.decode_content = True

                with open(img_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

            except Exception as e:
                print(e.__cause__)
                image_url = inquirer.text(
                    f"Não conseguimos baixar {image_url}. Verifique a URL ou digite \"q\" para pular a imagem")
                if image_url == "q":
                    break
            else:
                break


    def natural_sort(self, l):
        print("Ordenando os arquivos do diretório...")
        def convert(text): return int(text) if text.isdigit() else text.lower()
        def alphanum_key(key): return [convert(c)
                                    for c in re.split('([0-9]+)', key)]
        return sorted(l, key=alphanum_key)


    def print_help(self):
        print("\nComo usar:")
        print("python imgpdf.py -folder <caminho da pasta> <nome arquivo (opcional)>")
        print("python imgpdf.py -dataurl <caminho do arquivo json>  <nome arquivo (opcional)>")
        print("*para usar a funcionalidade de dataurl, o arquivo json deve ser o gerador pelo dataurl.py\n")


    def dataurl_to_image(self, path):
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


    def img_to_pdf(self, files, path, name, keep=False):
        print("Criando arquivo...")
        doc = Canvas(name)

        print("Adicionando imagens ao arquivo...")
        for img in files:
            if(os.path.isdir(f"{path}\\{img}") == False):
                file_path = f"{path}\\{img}"

                try:
                    image = img_open(file_path)
                except Exception:
                    print("*** Tentamos abrir o arquivo \"" + img +
                        "\", e não foi possível. Pulando... ***")
                    continue

                doc.setPageSize(image.size)
                doc.drawImage(file_path, 0, 0,
                            image.size[0], image.size[1], mask="auto")
                doc.showPage()

        print("Imagens adicionadas")
        image = ""

        print("Salvando PDF...")
        doc.save()

        if keep:
            os.rename(f"{os.getcwd()}\\__img_data__", f"{os.getcwd()}\\{name}")
        else:
            if(os.path.isdir(f"{os.getcwd()}\\__img_data__")):
                print("Apagando diretório auxiliar...")
                rmtree(os.getcwd() + "\\__img_data__")

        print("Processo terminado!\n\nO PDF está salvo na mesma pasta onde o script está armazenado.")


    def img_to_epub(self, files, path, name):
        print("Criando arquivo...")
        book = epub.EpubBook()

        book.set_identifier(str(randint(100000000, 100000000000)))
        book.set_title(name)
        book.set_language("pt-br")

        book.add_author("Author")

        book.set_cover(files[0], open(f"{path}\\{files[0]}", 'rb').read())

        print("Adicionando imagens ao arquivo...")
        count = 1
        content = ""
        for img in files:
            if os.path.isdir(f"{path}\\{img}") == False:
                file_path = f"{path}\\{img}"

                try:
                    image = open(file_path, "rb").read()
                except Exception:
                    print("*** Tentamos abrir o arquivo \"" + img +
                        "\", e não foi possível. Pulando... ***")
                    continue

                p = epub.EpubItem(file_name=img, content=image,
                                media_type=f'image/{img.split(".")[-1]}')
                book.add_item(p)

                content += f"<img src=\"{img}\" alt=\"Image {count}\"/>"
                count += 1

        c = epub.EpubHtml(title=name,
                        file_name=f'{name}.xhtml',
                        lang="pt-br")

        c.set_content(content)
        book.add_item(c)
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        print("Salvando Epub...")
        print(name)
        book.spine = ["cover", c]
        epub.write_epub(f"{str(name)}.epub", book)

        if(os.path.isdir(os.getcwd() + "\\__img_data__")):
            print("Apagando diretório auxiliar...")
            rmtree(os.getcwd() + "\\__img_data__")

        print("Processo terminado!\n\nO Epub está salvo na mesma pasta onde o script está armazenado.")


# ==============
# Main Program
# ==============

def main(action):
    helper = ImageUtils()
    if(action == "folder"):
        dir = inquirer.text(
            message="Digite o diretório das imagens (a ordem do nome das imagens será mantido)")
        name_file = inquirer.text(
            message="Digite o nome do arquivo final (ENTER para padrão)", default="")

        try:
            print("Listando diretório...")
            dir_files = os.listdir(dir)
        except FileNotFoundError:
            print("\nDiretório não existe ou está em formato incorreto, tente novamente")
            exit()
        except IndexError:
            helper.print_help()
            exit()

        dir_files = helper.natural_sort(dir_files)

        # Checks if the name of file is given in the args list
        if(name_file == None or name_file == ""):
            name_file = "output"

        helper.img_to_pdf(dir_files, dir, f"{name_file}.pdf")

    elif(action == "dataurl"):
        dir = inquirer.text(
            message="Digite o caminho com .json com as dataurls")
        name_file = inquirer.text(
            message="Digite o nome do arquivo final (ENTER para padrão)", default="")

        try:
            path = helper.dataurl_to_image(dir)
        except IndexError:
            helper.print_help()
            exit()

        print("Listando diretório...")
        dir_files = os.listdir(path)
        dir_files = helper.natural_sort(dir_files)

        if(name_file == None or name_file == ""):
            name_file = "output"

        helper.img_to_pdf(dir_files, path, f"{name_file}.pdf")

    elif(action == "web"):
        url = inquirer.text(
            message="Digite a url (coloque ?? onde tiver que substituir a variação)")

        shift = inquirer.text(
            message="Coloque o que substituir (um número de 1 a N ou uma lista de valores separados por vírgula)")

        if shift.find(",") != -1:
            shift = shift.split(",")

        name_file = inquirer.text(
            message="Digite o nome do arquivo final (ENTER para padrão)", default="")
        keep = inquirer.list_input(message="Manter as imagens baixadas?", choices=[
            ("Descartar", False),
            ("Manter", True),
        ])

        try:
            # Cuidado aqui, se for usar a função de range, precisa mudar o input para um int()
            path = helper.get_images(url, int(shift))
        except IndexError:
            helper.print_help()
            exit()

        print("Listando diretório...")
        dir_files = os.listdir(path)
        dir_files = helper.natural_sort(dir_files)

        # Checks if the name of file is given in the args list
        if(name_file == None or name_file == ""):
            name_file = "output"

        helper.img_to_pdf(dir_files, path, f"{name_file}.pdf", keep)

    elif(action == "epub"):
        dir = inquirer.text(
            message="Digite o diretório das imagens (a ordem do nome das imagens será mantido)")
        name_file = inquirer.text(
            message="Digite o nome do arquivo final (ENTER para padrão)", default="")

        try:
            print("Listando diretório...")
            dir_files = os.listdir(dir)
        except FileNotFoundError:
            print("\nDiretório não existe ou está em formato incorreto, tente novamente")
            exit()
        except IndexError:
            helper.print_help()
            exit()

        dir_files = helper.natural_sort(dir_files)

        # Checks if the name of file is given in the args list
        if(name_file == None or name_file == ""):
            name_file = "output"

        helper.img_to_epub(dir_files, dir, f"{name_file}.epub")
    else:
        helper.print_help()

    # pdf = PdfFileReader("purple.pdf")

    # print(str(pdf.getNumPages()) + "\n\n")
    # print(pdf.getPage(8).extractText())



def todo():
    util = ImageUtils()

    # 

    # Converter
    util.pdf_from_files()

    util.pdf_from_dataurl()

    util.pdf_from_web()

    util.epub_from_files()

    util.epub_from_web()

    util.epub_from_dataurl()

    util.dataurl_from_img()

    util.img_from_dataurl()


if __name__ == "__main__":

    # get_images("https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.jpg", 1)
    action = inquirer.list_input(message="Qual módulo quer utilizar?", choices=[
        ("PDF com imagens do computador", "folder"),
        ("PDF com imagens de dataurl", "dataurl"),
        ("PDF com imagens da web", "web"),
        ("Epub com imagens do computador", "epub"),
    ])

    main(action)
