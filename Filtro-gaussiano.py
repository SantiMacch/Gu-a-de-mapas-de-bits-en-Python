from PIL import Image
import os

direct = input("ingrese la ruta de la imagen:")

img = Image.open(direct)



#no se como aplicar el filtro


if not os.path.exists('ImagenesFiltradas') :
    os.makedirs('ImagenesFiltradas')

nombre, extension = os.path.splitext(os.path.basename(direct))
print(nombre)
print(extension)

nuevonombre = 'ImagenesFiltradas/' + nombre + 'Gaussian' + extension
print(nuevonombre)

