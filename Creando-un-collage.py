from PIL import Image
import os

ruta_carpeta = input("Ingrese la ruta de la carpeta que contiene al menos 9 imágenes: ")
rutacollague = input('ruta donde deseas mostrar el collague:')
resolucion_ancho = int(input("Ingrese el ancho del collage: "))
resolucion_alto = int(input("Ingrese el alto del collage: "))
    
rutas_imagenes = []
for nombre in os.listdir(ruta_carpeta):
    if nombre.endswith(('.png', '.jpg', '.jpeg', '.webp')):
        rutas_imagenes.append(os.path.join(ruta_carpeta, nombre))
        if len(rutas_imagenes) >= 9:
            break
    
if len(rutas_imagenes) < 9:
    print("La carpeta debe contener al menos 9 imágenes.")
    
collage = Image.new('RGB', (resolucion_ancho, resolucion_alto))
    
miniatura_ancho = resolucion_ancho // 3
miniatura_alto = resolucion_alto // 3
    
i = 0
    
for i, ruta_imagen in rutas_imagenes[:9]:  
    imagen = Image.open(ruta_imagen)
    miniatura = imagen.resize((miniatura_ancho, miniatura_alto))
        
    x = (i % 3) * miniatura_ancho
    y = (i // 3) * miniatura_alto
        
    collage.paste(miniatura, (x, y))
        
    i = i + 1

collage.save(os.path.join(rutacollague, "collage.png"))
collage.show()

