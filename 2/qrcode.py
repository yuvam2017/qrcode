import pyqrcode
import png
import os
from PIL import Image
from pyqrcode import QRCode
s = input("Enter the Text to be converted to QR : ")
url = pyqrcode.create(s)
os.mkdir("Generated_qrcodes")
os.chdir("Generated_qrcodes")
path = f'{s.split()[0]}.png'
url.png(path,scale=16)
img = Image.open(path)
img.show()

