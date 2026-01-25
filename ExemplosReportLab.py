#---CONCEPTO BÁSICOS DE CANVAS---

from reportlab.pdfgen import canvas #Importa el objeto principal para crear el lienzo del PDF

#Crea un objeto Canvas, que representa un documento PDF.
#Es la variable principal sobre la que se trabaja
folla = canvas.Canvas("1ºprimeiroDocumento.pdf")

# Las coordenadas en las que se empieza a pintar en roportlab es en la esquina inferior izquierda (0,0)
# En reportlab se "pintan" no se "añaden"

#drawString(x,y,texto) Escribe un texto en las coordenadas x, y
folla.drawString(0,0,"Posición inicial (x,y) = (0,0)")
folla.drawString(50,750,"Posición (x,y) = (50,750)")
folla.drawString(150,20, "Posición (x,y) = (150,20)")

#drawImage("imagen.png",x,y) Dibuja una imagen en las coordenadas x, y
folla.drawImage("box-pixilart(1).png",50,700)
folla.drawImage("equis23x23.jpg",50,650)

#Guarda la página actual y prepara una nueva
folla.showPage()
#Guarda el archivo PDF y lo cierra
folla.save()