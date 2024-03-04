from PIL import Image
import PIL
import os
import glob
import sys

def compress_images(directory=False, quality=30, prefix=""):
    # 1. If there is a directory then change into it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print("Esse diretório não existe, tente novamente com um válido!")
            return

    if not os.path.isdir(directory + "/new"):
        os.mkdir(directory + "/new")

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save(f"{directory}/new/{prefix}{image}", optimize=True, quality=quality)


if __name__ == "__main__":
    # args = sys.argv
    # path = args[1]

    # try:
    #     compression = int(args[2])
    # except IndexError:
    #     compression = 65

    # try:
    #     prefix = args[3]
    # except IndexError:
    #     prefix = ""
         
    # compress_images(path, compression, prefix)

    path = "C:/Users/Admin/Desktop/dawg"
    compression = 5

    while compression <= 100:
        compress_images(path, compression, f"{compression}-")
        compression += 5