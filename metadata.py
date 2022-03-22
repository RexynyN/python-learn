

import win32com.client as win32com    

path = r'C:\\Users\\Admin\\Desktop\\teste\\FFDKOicXIAECitH.jfif'
sh = win32com.gencache.EnsureDispatch('Shell.Application', 0)
# mid = sh.NameSpace(path)

wb = sh.Workbooks.Open(path, Local=True)

wb.RemovePersonalInformation = True
wb.Close(SaveChanges=1)
sh.Quit()

# import win32com.client

# def get_file_metadata(path, filename, metadata):
#     # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
#     # filename must include extension, i.e. "PID manual.pdf"
#     # Returns dictionary containing all file metadata.
#     sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
#     ns = sh.NameSpace(path)

#     # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
#     file_metadata = dict()
#     item = ns.ParseName(str(filename))
#     print()
#     for ind, attribute in enumerate(metadata):
#         attr_value = ns.GetDetailsOf(item, ind)
#         if attr_value:
#             file_metadata[attribute] = attr_value

#     return file_metadata

# # *Note: you must know the total path to the file.*
# # Example usage:
# if __name__ == '__main__':
#     folder = 'C:\\Users\\Admin\\Desktop\\teste'
#     filename = 'FFDKOicXIAECitH.jfif'
#     metadata = ['Name', 'Size', 'Item type', 'Date modified', 'Date created']
#     print(get_file_metadata(folder, filename, metadata))


# import PIL
# from PIL import Image
# import os
# import sys

# def main(args):
#     print("Listando diretório...")
#     dir_files = os.listdir(args[1])
#     size = len(dir_files)
#     remain = 1

#     for file in dir_files:
#         try:
#             image = Image.open(args[1] + "\\" + file)
#             data = list(image.getdata())
#             image_without_exif = Image.new(image.mode, image.size)
#             image_without_exif.putdata(data)
#             image_without_exif.save(args[1] + "\\" + file)
#         except Exception:
#             print(file + " não foi possível tirar a metadata")
#         except PIL.UnidentifiedImageError:
#             print(file + " não foi possível tirar a metadata")

#         print(str(remain) + "/" + str(size))
#         remain += 1

#     print("Terminado")
# if __name__ == '__main__':
#     main(sys.argv)
