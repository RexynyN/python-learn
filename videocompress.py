import os
from shutil import move as replace_file
from tkinter.filedialog import askdirectory

path = askdirectory()
# Filters out all videos that has not been compressed
files = []
for x in os.listdir(path):
    if x.startswith("0a--") or os.path.isdir(x):
        continue
    files.append(x)

# print(files)
sizes = [os.path.getsize(f"{path}\\{file}") for file in files]
# print(sizes)

info = [{"name":file, "size":size} for size, file in zip(sizes, files)]

# Compress first the bigger files
info.sort(reverse=True, key=lambda e: e["size"])

result = f"{path}\\compressed"
original = f"{path}\\original"

if not os.path.isdir(result):
    os.mkdir(result) 

for video in info:
    name = video["name"]
    pathsu = f"{path}\\{name}"

    status = os.system(f"ffmpeg -i \"{pathsu}\" -vcodec libx264 -crf 24 \"{result}\\0a--{name}\"")
    if status == 0:
        os.remove(pathsu)
