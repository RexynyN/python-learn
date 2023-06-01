import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk

root = tk.Tk()
root.state('zoomed')
root.title("Floppa Time")
root.update()

width  = root.winfo_width()
height = root.winfo_height()

raw_img = Image.open("notebooks/floppa.jpg")
print(raw_img.size)
if raw_img.size[0] > width:
    basewidth = width - 10
    wpercent = (basewidth/float(raw_img.size[0]))
    hsize = int((float(raw_img.size[1])*float(wpercent)))
    
    new_width  = 680
    new_height = new_width * height / width 
    
    raw_img = raw_img.resize((basewidth, hsize), Image.Resampling.LANCZOS)

if raw_img.size[1] > height:
    baseheight = height - 10
    wpercent = (baseheight/float(raw_img.size[1]))
    hsize = int((float(raw_img.size[0])*float(wpercent)))    
    raw_img = raw_img.resize((hsize, baseheight), Image.Resampling.LANCZOS)

print(raw_img.size)

img = ImageTk.PhotoImage(raw_img)


canvas = tk.Canvas(root, width=img.width(), height=img.height())
canvas.pack()
canvas.create_image(0,10, anchor=tk.NW, image=img)  

tk.mainloop()