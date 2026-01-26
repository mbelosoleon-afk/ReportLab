#---USO DE DRAWING---

from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF #Renderiza un objeto Drawing en un PDF
from reportlab.lib.pagesizes import A4

# Los objetos a introducir, se introducen en una lista
guion = []

#Image(x,y,ancho,alto,"imagen.png") Crea un objeto de tipo Imagen
imaxe = Image(20,100,32,32,"box-pixilart(1).png")
imaxe2 = Image(60,100,32,32,"box-pixilart(1).png")

#Drawing(ancho,alto) Crea un dibujo o lienzo gráfico
debuxo = Drawing(300,32)
debuxo2 = Drawing(300,102)
debuxo3 = Drawing()
debuxo4 = Drawing()

#Añade la imagen al cuadro
#Se añaden las imágenes a un objeto Drawing con debuxo.add()
debuxo.add(imaxe)

debuxo2.add(imaxe2)

#translate(dx,dy) Mueve el lienzo completo
debuxo.translate(150,350)

debuxo3.add(imaxe)
#Rota el lienzo
debuxo3.rotate(33)
debuxo3.translate(200,200)

debuxo4.add(imaxe)
debuxo4.translate(400, 400)
#scale(sx,sy) Escala el lienzo
debuxo4.scale(0.5,0.5)

#Se añade al contenedor de objetos
guion.append(debuxo)
guion.append(debuxo2)
guion.append(debuxo3)
guion.append(debuxo4)

#Representa el tamaño de una hoja formato A4
folla = Drawing(A4[0], A4[1])
print(A4)

for elemento in guion:
    folla.add(elemento)
    #Dibuja el contenido de un Drawing en un fichero PDF
    renderPDF.drawToFile(folla,"2ºexemploDrawing.pdf")