from PIL import Image
import os

directdeimg = input('ingrese la ruta de la imagen:')
direcdema = input('ingrese la ruta de  la marca de agua: ')

img = Image.open(directdeimg)
imgma = Image.open(direcdema)

ancho, alto = img.size
anchoma, altoma = imgma.size

margen = 50

print(f'el ancho es: {ancho} y el alto es: {alto}')

print('1: Superior izquierda, 2: Superior derecha, 3: Inferior izquierda, 4: Inferior derecha')
ubicacion = input('eliga ubicacion marca de agua 1, 2, 3 o  4:')

if ubicacion == '1' :
  img.paste(imgma, (margen, margen))
elif ubicacion == '2' :
  img.paste(imgma, (ancho - anchoma - margen, margen))
elif ubicacion == '3' :
  img.paste(imgma, (margen, alto - altoma - margen))
elif ubicacion == '4' :
  img.paste(imgma, (ancho - anchoma - margen, alto - altoma - margen))
else :
  print('error')

img.save('pasted.png')
img.show
