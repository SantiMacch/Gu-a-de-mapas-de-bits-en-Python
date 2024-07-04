from PIL import Image
import os

direct = input("ingrese la ruta de la imagen:")

img = Image.open(direct)

if img.mode != 'RGB':
    img = img.convert('RGB')

imagenbn = Image.new("RGB", img.size)

pixelesoriginales = img.load()
pixelesbn = imagenbn.load()

for y in range(img.height):
  for x in range(img.width):
    r, g, b = pixelesoriginales[x, y]
    gris = int((r + g + b) / 3)
    pixelesbn[x, y] = (gris, gris, gris)

if not os.path.exists('ImagenesFiltradas') :
    os.makedirs('ImagenesFiltradas')

nombre, extension = os.path.splitext(os.path.basename(direct))
print(nombre)
print(extension)

nuevonombre = 'ImagenesFiltradas/' + nombre + 'BN' + extension
print(nuevonombre)


imagenbn.save(nuevonombre)

pixelesbn.show

