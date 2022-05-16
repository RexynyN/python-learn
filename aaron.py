from PIL import Image

# We'll be cropping the image to a 300x300 dimensions
img = Image.open(f"__img_data__\\sexo.jpg")
print(img.size)

width, height = img.size   # Get dimensions

offset = 350
if height < offset:
    offset = height

left = (width - offset)/2
top = (height - offset)/2
right = (width + offset)/2
bottom = (height + offset)/2

# Crop the center of the image
img = img.crop((left, top, right, bottom))

img.save(f"__img_data__\\sexo.jpg")

