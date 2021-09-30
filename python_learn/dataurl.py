import base64
import json
import os
from binascii import a2b_base64


def image_to_data_url(filename):
    ext = filename.split('.')[-1]
    prefix = f'data:image/{ext};base64,'
    with open(filename, 'rb') as f:
        img = f.read()
    return prefix + base64.b64encode(img).decode('utf-8')

def data_url_to_image(data, filename):
    if(data.find(",") != -1):
        data = data.split(",")[-1]
        
        if(not os.path.isdir(os.getcwd() + "\\output")):
            os.mkdir(os.getcwd() + "\\output")
            
        binary_data = a2b_base64(data)
        with open(os.getcwd() + "\\output\\" + filename, 'wb') as f:
            f.write(binary_data)


with open("megafon.json", "r") as read_file:
    data = json.load(read_file)

for data in data:
    data_url_to_image(data['link'], data['file'])


# print (data[0]["file"])
# print (data[0]["extension"])
# print (data[0]["link"])

# action = input("(1) Escrever DataURL\n(2) Ler Json de DataURL\nEscolha: ")
# print (image_to_data_url("koto.mp3"))
# data_url_to_image(input("Coloca essa merda: "))

# from argparse import ArgumentParser

# parser = ArgumentParser()
# parser.add_argument("-f", "--file", dest="filename",
#                     help="write report to FILE", metavar="FILE")
# parser.add_argument("-q", "--quiet",
#                     action="store_false", dest="verbose", default=True,
#                     help="don't print status messages to stdout")

# args = parser.parse_args()
