from PIL import Image
import os

direct = input('ingrese la ruta de la imagen:')
rotacion = int(input('ingrese el angulo de rotacion:'))

img = Image.open(direct)

imgrotada = img.rotate(rotacion)

imgrotada.show

# nombre = img.filename
nombre, extension = os.path.splitext(os.path.basename(direct))
extencion = img.format
print(nombre)
print(extencion)

nuevonombre = nombre + 'Rot.' + extencion

print(nuevonombre)


imgrotada.save(nuevonombre)
