from PIL import Image

img = Image.open("img.png")
img.save("img_compresed.jpg", "JPEG", optimize=True, quality=10)