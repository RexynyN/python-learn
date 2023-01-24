import pyqrcode
import png 
from pyqrcode import QRCode

# Link/Texto
conteudo = "https://google.com/"

qr = pyqrcode.create(conteudo)

qr.png(r"qrcode.png", scale=1000)