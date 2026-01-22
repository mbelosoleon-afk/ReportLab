from reportlab.pdfgen import canvas
import os

#---PDFS CON CANVAS---

# Usamos la ruta absoluta para evitar errores de ubicación
guia_carpetas = os.path.dirname(os.path.abspath(__file__))

# NOMBRES CORREGIDOS (según tu listado de archivos)
ruta_box = os.path.join(guia_carpetas, "box-pixilart(1).png")
ruta_equis = os.path.join(guia_carpetas, "equis23x23.jpg")

# Crea el objeto canvas
#Lienzo donde ocurre todo, si el archivo yaa existe, lo sobreescribe
folla = canvas.Canvas("1ºprimeiroDocumento.pdf")

# Las coordenadas (0,0) están en la esquina inferior izquierda
#drawString pinta una sola línea de texto
#drawString(x,y,texto)
folla.drawString(0,0,"Posición inicial (x,y) = (0,0)")
folla.drawString(50,750,"Posición (x,y) = (50,750)")
folla.drawString(150,20, "Posición (x,y) = (150,20)")

# Dibujamos las imágenes con los nombres reales
# He añadido width y height para que no salgan gigantescas
#drawImage(ruta,x,y,width,height,preserveAspectRatio)
folla.drawImage(ruta_box, 50, 700, width=50, height=50)
folla.drawImage(ruta_equis, 50, 600, width=50, height=50)

# Finalizar y guardar
#Indica que has terminado de pintar la página actual.
#Si quieres hacer un PDF de dos páginas,
# llamarías a showPage() y seguirías pintando antes del save()
folla.showPage()
#Save es esencial, no lo llamas el archivo no se generará
folla.save()

print("PDF generado con éxito usando los nombres de archivo correctos.")

#---MÉTODOS DE CONFIG ANTES DE PINTAR---

#setFont("Nombre",tamaño) -> Fuente letra y tamaño
#setFillColor(color) -> Cambia el color del texto o del relleno de las figuras
#setStrokeColor(color) -> Cambia el color de las líneas