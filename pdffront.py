import tkinter as tk 
import tkinter.filedialog as fd 

root = tk.Tk()
filez = fd.askopenfilenames(parent=root, title='Choose a file')
direc = fd.askdirectory()
print(filez)
print(direc)