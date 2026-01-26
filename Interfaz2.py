from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from ExemplosReportLab3 import obxTexto

#Creaci
folla = canvas.Canvas("Interfaz2.pdf",pagesize=A4)
width, height = A4

#--ENCABEZADO (uso de drawString())
folla.setFont("Helvetica-Bold",22)
folla.drawString(40,height -60, "FACTURA Proforma")

#--Simulación de logo con texto (puedes usar drawImage() si tienes el archivo)ç
folla.setFillColor(colors.lightgrey)
folla.setFont("Helvetica-Bold",18)
folla.drawString(width - 140, height - 60,"sevDesk")
folla.setFillColor(colors.black)

#--BLOQUE DE DATOS DEL CLIENTE (Control de texto avanzado)--
obxTexto = folla.beginText()
obxTexto.setTextOrigin(40, height - 100)
obxTexto.setFont("Helvetica-Bold", 10)
obxTexto.textLine("FACTURAR A:")

obxTexto.setFont("Helvetica", 10)
#Movemos el cursor para dejar espacio tras el título
obxTexto.moveCursor(0,5)
datos_cliente = ["Cliente", "Domicilio", "Código postal / ciudad", "(NIF)"]
for linea in datos_cliente:
    obxTexto.textLine(linea)

#Dibujamos el bloque de texto del cliente
folla.drawText(obxTexto)

#Datos de la factura (Derecha)
obxTextoDer = folla.beginText(width -220, height - 90)
obxTextoDer.setFont("Helvetica-Bold", 14)
obxTextoDer.textLine("Nª DE FACTURA")
obxTextoDer.setFont("Helvetica", 10)
obxTexto.moveCursor(0,5)

lineas_factura = ["Fecha", "Nª de pedido", "Fecha de vencimiento", "Condiciones de pago"]
for linea in lineas_factura:
    obxTextoDer.textLine(linea)

folla.drawText(obxTextoDer)

#--TABLA DE CONCEPTOS (Tablas con Platypus)--
#Definimos los datos (cabecera + filas vacías para completar)
encabezado_tabla = ['Pos.', 'Concepto/Descripción', 'Cantidad', 'Unidad', 'Precio unit.', 'Importe']
fila_vacia1 = ['1', '', '', '', '', '']
fila_vacia2 = ['2', '', '', '', '', '']

datos_taboa = [encabezado_tabla, fila_vacia1, fila_vacia2, ['', '', '', '', '' ,'']]

#Creamos la tabla
taboa = Table(datos_taboa)

taboa.setStyle([
    ('BACKGROUND',(0,0),(-1,0), colors.lightgrey),
    ('GRID', (0,0),(-1,-1),0.5, colors.grey),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('FONTNAME',(0,0),(-1,0),"Helvetica-Bold"),
    ('ALIGN',(0,0),(0,-1),"CENTER")
])

#Como estamos usando Canvas, usamos wrapOn y drawOn para la tabla
taboa.wrapOn(folla,width,height)
taboa.drawOn(folla,40,height-320)

#--SECCIÓN INFERIOR: MÉTODOS Y TOTALES--

#Cuadro de método de pago (Dibujo con rect)
folla.rect(40,height-420,250,60)
folla.setFont("Helvetica",9)
folla.drawString(45,height-375,"Método de pago:")

#Tabla de totales
datos_totales = [
    ['Importe neto', ''],
    ['+ IVA de   %', ''],
    ['- IRPF de   %', ''],
    ['IMPORTE BRUTO', '']
]

taboa_totales = Table(datos_totales)
taboa_totales.setStyle([
    ('GRID',(0,0),(-1,-2),0.5,colors.grey),
    ('BOX',(0,3),(1,3),1,colors.black),
    ('BACKGROUND',(0,3),(1,3),colors.lightgrey),
    ('FONTNAME',(0,3),(0,3),"Helvetica-Bold"),
    ('ALIGN',(1,0),(1,-1),'RIGHT'),
])

taboa_totales.wrapOn(folla,width,height)
taboa_totales.drawOn(folla,width-240,height-440)

#Pie de págoina final
folla.setFont("Helvetica",10)
folla.drawString(40,height-500,"Gracias por su confianza")
folla.drawString(40,height-540,"Atentamente,")

folla.showPage()
folla.save()