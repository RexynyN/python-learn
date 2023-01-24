
import os
from tkinter.filedialog import askdirectory
from shutil import move as replace_file

path = askdirectory()
fix = "0a--"

for file in os.listdir(path):
    new = file.replace(fix, "").trim()
    if new != file:
        replace_file(f"{path}\\{file}", f"{path}\\copies\\{file}")

