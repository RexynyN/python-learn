# ===============================================
# extract text

import re
from pdfminer.high_level import extract_pages, extract_text

# All elements
for page_layout in extract_pages("<>.pdf"):
    for element in page_layout:
        print(element)


text = extract_text("<>.pdf")
print(text)

# Starts with lowercase or upper case, followed by a single comma
# and a single space
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
names = [n[:2] for n in matches]

print(names)


# ===============================================
# extract images

import fitz # pip install PyMuPDF
import io
from PIL import Image

pdf = fitz.open("<>.pdf")
counter = 1

for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in page.get_images():
        base_img = pdf.extract_image(image[0])
        image_data = base_img['image']
        img = Image.open(io.BytesIO(image_data))
        extension = base_img['ext']
        img.save(open(f"img{counter}.{extension}", "wb"))


# ===============================================
# extract tables

import tabula 

tables = tabula.read_pdf("<>.pdf", pages="all")
df = tables[0]
print(df)