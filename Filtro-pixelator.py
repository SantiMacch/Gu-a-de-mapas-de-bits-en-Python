from PIL import Image
import numpy as np
import os

direct = input("ingrese la ruta de la imagen:")

img = Image.open(direct)

tamanopixel = 20
imagen = img.convert('RGB')
pixeles = np.array(imagen)

resultado = np.zeros_like(pixeles)

for y in range(0, pixeles.shape[0], tamanopixel):
    for x in range(0, pixeles.shape[1], tamanopixel):
        
        #no se como se deberia aplicar el filtro 

if not os.path.exists('ImagenesFiltradas') :
    os.makedirs('ImagenesFiltradas')

nombre, extension = os.path.splitext(os.path.basename(direct))
print(nombre)
print(extension)

nuevonombre = 'ImagenesFiltradas/' + nombre + 'Pixelator' + extension
print(nuevonombre)


img.save(nuevonombre)

img.show