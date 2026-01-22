from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

#---PDFS CON SHAPES---

# Los objetos a introducir, se introducen en una lista
guion = []

# Posicionamiento de una imagen y tamaño
#Image(x,y,ancho,alto,ruta)
#x y relativas al Drawing dnd se meta, no necesariamente a la página total
imaxe = Image(20,100,32,32,"box-pixilart(1).png")
imaxe2 = Image(60,100,32,32,"box-pixilart(1).png")

# Marco o caja invisible que agrupa elementos
debuxo = Drawing(300,32)
debuxo2 = Drawing(300,102)
debuxo3 = Drawing()
debuxo4 = Drawing()

# Añade la imagen al cuadro
debuxo.add(imaxe)

debuxo2.add(imaxe2)
#Transalate mueve el dibujo a una nueva posición en el pdf
debuxo.translate(150,350)

debuxo3.add(imaxe)
#Rotate gira el contenido del dibujo los grados indicados
debuxo3.rotate(33)
debuxo3.translate(200,200)

debuxo4.add(imaxe)
debuxo4.translate(400, 400)
#Scale cambia el tamaño escala
debuxo4.scale(0.5,0.5)

# Se añade al contenedor de objetos
guion.append(debuxo)
guion.append(debuxo2)
guion.append(debuxo3)
guion.append(debuxo4)

# Representa el tamaño de una hoja formato A4
folla = Drawing(A4[0], A4[1])
print(A4)

for elemento in guion:
    folla.add(elemento)
    renderPDF.drawToFile(folla,"2ºexemploDrawing.pdf")