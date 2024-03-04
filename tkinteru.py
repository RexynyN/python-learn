import os
import imagehash
import tkinter as tk
from os.path import join
from shutil import move as replace_file
from tkinter.ttk import Style
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image

# =================================================================================================
# ======================================== FUNCTION ===============================================
# =================================================================================================

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
            if not os.path.isdir(join(compare_dir, image_dir)):
                os.mkdir(join(compare_dir, image_dir))

            replace_file(join(path, copy), join(compare_dir, image_dir, copy))
            dict["file"].remove(copy)
            dict["hash"].remove(dict["hash"][i])

        nob += 1

    dict["file"].remove(file)
    dict["hash"].remove(hash)

    return dict

def render_images(compare_dir):
    pass

def get_path():
    global path
    try:
        path = askdirectory()
        dir_files = os.listdir(path)
    except FileNotFoundError:
        return
    
    compare_dir = join(path, "compare")
    if not os.path.isdir(compare_dir):
        os.mkdir(compare_dir)

    img_hash = get_hashes(path, dir_files)

    aux = img_hash.copy()
    total = len(img_hash["file"])
    now = 1
    for i in range(total):
        try:
            file = img_hash["file"][i]
        except IndexError:
            now += 1
            continue

        if file not in aux["file"]:
            now += 1
            continue

        aux = compare_iterator(path, file, img_hash["hash"][i], aux, compare_dir, stats=(
            now, total), cutoff=int(5))

        image_dir = file.split(".")[0]
        if os.path.isdir(join(compare_dir, image_dir)):
            replace_file(join(path, file), join(compare_dir, image_dir, file))

        now += 1

    render_images(compare_dir)

# =================================================================================================
# ========================================= TKINTER ===============================================
# =================================================================================================

def botao1_click():
    print("Bingus")

def botao2_click():
    print("Floppa")


path = ""
# Cria a janela
janela = tk.Tk()
janela.title("Floppa and Bingus")

# Define o estilo
estilo = Style()
estilo.configure("TFrame", background="#f0f0f0", relief="solid", borderwidth=1)
estilo.configure("TLabel", background="#f0f0f0", padding=10)
estilo.configure("TButton", background="#dddddd", padding=5)

# Define as margens da janela
margem_superior = 20
margem_inferior = 20
margem_esquerda = 20
margem_direita = 20
janela.geometry(f"+{margem_esquerda}+{margem_superior}")

# Carrega as imagens
imagem1 = Image.open("notebooks/bingus.jpg")
imagem1 = imagem1.resize((300, 300))  # Redimensiona a imagem se necessário
imagem1 = ImageTk.PhotoImage(imagem1)

imagem2 = Image.open("notebooks/floppa.jpg")
imagem2 = imagem2.resize((300, 300))  # Redimensiona a imagem se necessário
imagem2 = ImageTk.PhotoImage(imagem2)

# Cria os widgets
botaopath = tk.Button(janela, text="Processar", command=get_path)
botaopath.pack()

container1 = tk.Frame(janela)
container1.pack(side="left", padx=10, pady=10)

label1 = tk.Label(container1, image=imagem1)
label1.pack()

botao1 = tk.Button(container1, text="Bingus", command=botao1_click)
botao1.pack(pady=10)

container2 = tk.Frame(janela)
container2.pack(side="left", padx=10, pady=10)

label2 = tk.Label(container2, image=imagem2)
label2.pack()

botao2 = tk.Button(container2, text="Floppa", command=botao2_click)
botao2.pack(pady=10)

# Inicia o loop da janela
janela.mainloop()
