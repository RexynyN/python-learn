import os
from tkinter.filedialog import askdirectory
from shutil import move as replace_file

original = askdirectory()
target = askdirectory()

if not os.path.isdir(f"{target}\\copies"):
    os.mkdir(f"{target}\\copies") 

for compare in os.listdir(target):
    for file in os.listdir(original):
        if compare == file:
            replace_file(f"{target}\\{file}", f"{target}\\copies\\{file}")

