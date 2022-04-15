import os
from shutil import move as replace_file
from tkinter.filedialog import askdirectory

path = askdirectory()
result = f"{path}\\compressed"
original = f"{path}\\original"

if not os.path.isdir(result):
    os.mkdir(result) 

if not os.path.isdir(original):
    os.mkdir(original) 

for video in os.listdir(path):
    pathsu = f"{path}\\{video}"

    if video.startswith("0a--") or os.path.isdir(pathsu):
        continue
    
    status = os.system(f"ffmpeg -i \"{pathsu}\" -vcodec libx264 -crf 24 \"{result}\\0a--{video}\"")
    if status == 0:
        replace_file(pathsu, f"{original}\\{video}")

# video = "2bb08fa64a603d93849e6c1e5980ec243a7ac707.mp4"
# path = "E:\\Mídia\\musictest\\Notmusic"
# pathsu = f"{path}\\{video}"
# print(os.system(f"ffmpeg -i \"{pathsu}\" -vcodec libx264 -crf 24 \"{path}\\0a--{video}\""))
