from PIL import Image
import os

direct = input("ingrese la ruta de la imagen:")

img = Image.open(direct)

img.show

width, height = img.size
nombre, extension = os.path.splitext(os.path.basename(direct))
#nombre = img.name
ruta = img.filename
extencion = img.format
resolucion = width + 'x' + height

print('nombre        ', nombre)
print('ruta     ', ruta)
print('width     ', width)
print('height     ', height)
print('extencion    ', extencion)
print('resolucion    ', resolucion)

