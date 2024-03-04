class PdfTools:
    def __init__(self) -> None:
        pass

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
    

    def img_to_pdf(self, files, path, name, keep=True):
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
