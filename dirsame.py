import os

path_1 = r"C:\Users\Admin\Downloads\crcos\save"

path_2 = r"C:\Users\Admin\Downloads\crcos\save\compressed"

extension = "0a--"

files_1 = os.listdir(path_1)
files_2 = os.listdir(path_2)

for i in files_1:
    if extension + i in files_2:
        print(extension + i) 


        
