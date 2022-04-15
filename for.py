

image = GExiv2.Metadata('sample.jpg')
image.clear_exif()
image.clear_xmp()
image.save_file()

# from PIL import Image

# image = Image.open('E:\Mídia\igor.jpg')



# # next 3 lines strip exif
# data = list(image.getdata())
# image_without_exif = Image.new(image.mode, image.size)
# image_without_exif.putdata(data)

# image_without_exif.save('reacao_reacionada.jpg')