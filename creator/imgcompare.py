from PIL import Image
import os
import imagehash
import inquirer
from shutil import move as replace_file


# Deprecated, uses too many memory and time to loop over, but hey, you can quickly use it in a small pool of images
def img_compare(path, img1, img2, cutoff=5):
    if img1 == img2:
        return False

    try:
        hash0 = imagehash.average_hash(Image.open(f"{path}\\{img1}"))
        hash1 = imagehash.average_hash(Image.open(f"{path}\\{img2}"))
    except Exception:
        print(
            f"*** Tentamos abrir o arquivo para comparar \"{img2}\", e não foi possível. Pulando... ***")
        return False

    if hash0 - hash1 < cutoff:
        return True
    else:
        return False

        

# Could probably use some threading, but i'm too lazy/stupid to do it myself ;)
def get_hashes(path, files):
    hash_dict = {"hash": [], "file": []}
    for file in files:
        try:
            hashed = imagehash.average_hash(Image.open(f"{path}/{file}"))
            print(hashed)
            hash_dict["hash"].append(hashed)
            hash_dict["file"].append(file)

        except Exception:
            continue

    return hash_dict


def compare_iterator(path, file, hash, dict, compare_dir=None, stats=(0, 0), cutoff=3):
    nob = 1
    clotal = len(dict["file"])
    for i in range(clotal):
        # C:\Users\Admin\Desktop\Movie Scripts\teste
        try:
            copy = dict["file"][i]
        except IndexError:
            break

        copy = dict["file"][i]
        print(f"Imagem {stats[0]}/{stats[1]} -> Comparação {nob}/{clotal}")

        sentinel = hash - dict["hash"][i]  < cutoff

        # The image is close to being the same, allocate to another folder
        if sentinel and file != copy:
            image_dir = file.split(".")[0]
            if not os.path.isdir(f"{compare_dir}\\{image_dir}"):
                os.mkdir(f"{compare_dir}\\{image_dir}")

            replace_file(f"{path}\\{copy}",
                         f"{compare_dir}\\{image_dir}\\{copy}")
            dict["file"].remove(copy)
            dict["hash"].remove(dict["hash"][i])

        nob += 1

    dict["file"].remove(file)
    dict["hash"].remove(hash)

    return dict


def main(action):
    if action == "compare":
        
        questions = [inquirer.Path("dir", message="Diretório das imagens a serem comparadas", normalize_to_absolute_path=True, exists=True, path_type=inquirer.Path.DIRECTORY),
                  inquirer.Text(
                      "cutoff", message="Margem de Comparação (quanto menor, mais estrita vai ser a comparação)", default=5)
                  ]

        config = inquirer.prompt(questions)

        dir = config["dir"]

        try:
            print("Listando diretório...")
            dir_files = os.listdir(dir)
        except Exception:
            print("\nDiretório não existe ou está em formato incorreto, tente novamente")
            exit()

        compare_dir = f"{dir}\\compare"
        if not os.path.isdir(compare_dir):
            os.mkdir(compare_dir)

        img_hash = get_hashes(dir, dir_files)

        aux = img_hash.copy()
        total = len(img_hash["file"])
        now = 1
        for i in range(total):
            try:
                file = img_hash["file"][i]
            except IndexError:
                now += 1
                continue

            if(file not in aux["file"]):
                now += 1
                continue

            aux = compare_iterator(config["dir"], file, img_hash["hash"][i], aux, compare_dir, stats=(
                now, total), cutoff=int(config["cutoff"]))

            image_dir = file.split(".")[0]
            if(os.path.isdir(f"{compare_dir}\\{image_dir}")):
                replace_file(f"{dir}\\{file}",
                             f"{compare_dir}\\{image_dir}\\{file}")

            now += 1

    elif action == "restore":
        # dir = "C:\\Users\Admin\\Desktop\\Movie Scripts\\teste"
        questions = [inquirer.Path("dir", message="Diretório das imagens a serem restauradas (sem a pasta \"compare\")", normalize_to_absolute_path=True, exists=True, path_type=inquirer.Path.DIRECTORY)]

        config = inquirer.prompt(questions)
        dir = config["dir"]

        compare_dir = f"{dir}\\compare"
        for folder in os.listdir(compare_dir):
            new_dir = f"{compare_dir}\\{folder}"
            if not os.path.isdir(new_dir):
                continue

            for file in os.listdir(new_dir):
                replace_file(f"{new_dir}\\{file}", f"{dir}\\{file}")

if __name__ == '__main__':

    action = inquirer.list_input(message="Qual módulo quer utilizar?", choices=[
        ("Comparar Imagens", "compare"),
        ("Restaurar pasta \"compare\"", "restore"),
    ])

    main(action)
