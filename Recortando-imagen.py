from PIL import Image
import os

x = 1
while True :

  direct = input('ingrese la ruta de la imagen:')

  img = Image.open(direct)

  width, height = img.size

  print(f'el ancho es: {width} y el alto es: {height}')

  while True :
    cordinicialx = int(input('ingrese la cordenada inicial de x:'))
    cordinicialy = int(input('ingrese la cordenada inicial de y:'))
    valoresanchocort = int(input('ingrese los valor de ancho para cortar:'))
    valoralturacort = int(input('ingrese el valor de altura para cortar:'))

    if cordinicialx > width or cordinicialy > height :
      print('cordenada inicial igresada no es valida')
    elif cordinicialx + valoresanchocort > width :
      print('valor de ancho para cortar igresado no es valida')
    elif cordinicialy + valoralturacort > height :
      print('valor de altura para cortar igresado no es valida')
    else :
      break

  imgcortada = img.crop((cordinicialx, cordinicialy, cordinicialx + valoresanchocort, cordinicialy + valoralturacort))

  if not os.path.exists('recortes') :
    os.makedirs('recortes')

  nombre = f'recortes/recorte{x}.png'
  imgcortada.save(nombre)
  x = x + 1

  sigue = input('continua S/n :')
  if sigue != 'S' :
    break