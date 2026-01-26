import os

from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []
hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo["Heading2"]
cabecera.fontSize=18
cabecera.alignment=2
cabecera.textColor = colors.darkseagreen

blanc = ['', '', '', '']
tit = ['Nombre de tu empresa', '', '', 'Logo de la Empresa']
inf1 = ['Dirección', '', '', '']
inf2 = ['Ciudad y País', '', '', '']
inf3 = ['CIF/NIF', '', 'Fecha Emisión', 'DD/MM/AAA']
inf4 = ['Teléfono', '', 'Número de Factura', 'A0001']
inf5 = ['Mail', '', '', '']

tab = ['Descripción', 'Importe', 'Cantidad', 'Total']
pr1 = ['Producto 1', '3,2', '5', '16,00']
pr2 = ['Producto 2', '2,1', '3', '6,30']
pr3 = ['Producto 3', '2,9', '76', '220,40']
pr4 = ['Producto 4', '5', '23', '115,00']
pr5 = ['Producto 5', '4,95', '3', '14,85']
pr6 = ['Producto 6', '6', '2', '12']
total = ['', '', 'TOTAL', '385€']
tabla = Table ([blanc, tit, inf1, inf2, inf3, inf4, inf5, blanc, tab, pr1, pr2, pr3, pr4, pr5, pr6, total])

tabla.setStyle([('FONTSIZE', (0,0),(0,1), 18),
                ('FONTSIZE', (3,1),(3,1), 15),
                ('BOTTOMPADDING' , (0,1), (3,1), 11),
                ('ALIGN', (2,4), (2,5), 'RIGHT'),
                ('ALIGN', (3, 4), (3, 5), 'CENTER'),
                #('BACKGROUND', (0,9), (3,14), colors.cyan),
                ('BACKGROUND', (0,9), (3,14), colors.palegreen),
                ('BACKGROUND', (0,8), (3,8), colors.green),
                ('ALIGN', (0,8), (2,15), 'CENTER'),
                ('ALIGN', (3,8), (3,8), 'CENTER'),
                ('ALIGN', (3,9), (3,14), 'RIGHT'),
                ('ALIGN', (3,15), (3,15), 'CENTER'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
                ('TOPPADDING', (2, 15), (3, 15), 11),
                ('BOTTOMPADDING', (2, 15), (3, 15), 11),
                ('BACKGROUND', (2, 15), (3, 15), colors.green),
                ('TEXTCOLOR' ,(0,8),(3,8), colors.white),
                ('TEXTCOLOR', (2, 15), (3, 15), colors.white),
                ('TEXTCOLOR', (0, 1), (3,7), colors.darkolivegreen ),
                ])


titulo=Paragraph("FACTURA SIMPLIFICADA", cabecera)
guion.append(titulo)

guion.append(tabla)

doc = SimpleDocTemplate("Factura1.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)