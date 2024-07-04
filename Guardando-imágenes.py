from PIL import Image

direct = input("ingrese la ruta de la imagen:")

img = Image.open(direct)

img.show

img.save('copia de imagen2.png')