#---CONTROL AVANZADO DE TEXTO---

from reportlab.pdfgen import canvas

# Tupla que guarda texto que mostrará
texto = ('Este texto é para exemplo',
         'da utilización de canvas',
         'para usar con texto.',
         'Alongo o texto',
         'para ter mais frases',
         ' e notar a diferencia')

# Objeto canvas que genera el pdf
obxCanvas = canvas.Canvas("3ºtextoCanvas.pdf")

#Crea un objeto de texto que permite configuraciones complejas
obxTexto = obxCanvas.beginText()

#setTextOrigin(x,y) Controla la posición inicial del texto
obxTexto.setTextOrigin(100,500)

#Cambia la tipografía
obxTexto.setFont("Courier",16)

# Para añadir el texto en el pdf ordenado
for linha in texto:
    #Mueve el cursor relativamente a su posición actual
    obxTexto.moveCursor(20,15)
    #Escribe una línea de texto y avanza el cursor
    obxTexto.textLine(linha)
    #Color mediante valores decimales
    obxTexto.setFillColorRGB(0.2,0,0.6)

# Añade otro texto de un color mas claro
#Añade otra escala de grises
obxTexto.setFillGray(0.5)
textoLongo = """Outro texto con varias
                liñas incorporadas,
                con retornos de carro \nincluidos."""
#Escribe un bloque de texto que puede tener saltos de línea
obxTexto.textLines(textoLongo)

# Modifica la posición del nuevo texto introducido sin modificar las del anterior
obxTexto.setTextOrigin(20,300)

# Modifica el tipo de letra del texto según las que la importación canvas incluye
for tipo_letra in obxCanvas.getAvailableFonts():
    obxTexto.setFont(tipo_letra,16)
    obxTexto.textLine("Texto de exemplo coa fonte: "+ tipo_letra)
    # Coloca el texto de manera escalonada
    obxTexto.moveCursor(20,15)

# Añade otro texto con sus configuraciones
obxTexto.setTextOrigin(20,800)
#Color por nombre
obxTexto.setFillColor('pink',1) # En vez de poner color con números se pone con nombre
obxTexto.setFont('Helvetica-BoldOblique',12)
for linha in texto:
    obxTexto.moveCursor(20,15)
    #Escribe el texto pero NO salta de línea
    obxTexto.textOut(linha)

obxTexto.moveCursor(-60 , 15)
espazoCaracteres = 0
for linha in texto:
    #Ajusta el espacio entre letras
    obxTexto.setCharSpace(espazoCaracteres)
    obxTexto.textLine("Espazo %s: %s:" % (espazoCaracteres,linha))
    espazoCaracteres += 1

obxTexto.setTextOrigin(20, 550)
obxTexto.setCharSpace(1)
#Ajusta el espacio entre palabras
obxTexto.setWordSpace(8)
obxTexto.textLines(textoLongo)

#Dibuja el objeto de texto en el canvas
obxCanvas.drawText(obxTexto)

obxCanvas.showPage()
obxCanvas.save()