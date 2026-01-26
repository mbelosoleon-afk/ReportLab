import sqlite3

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph

from Interfaces.Interfaz2 import guion

def obter_clientes_maior_facturacion(limite=10):
    conn = sqlite3.connect('bdTendaOrdeadoresBig.bd')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT
            c.nome,
            COUNT(DISTINCT f.id_factura) as num_facturas,
            SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100) * (1 + p.iva/100)) as
            facturacion_total
            FROM clientes c
            JOIN facturas f ON c.id_cliente = f.id_cliente
            JOIN linhas_factura lf ON f.id_factura = lf.id_factura
            JOIN produtos p ON lf.id_produto = p.id_produto
            GROUP BY c.id_cliente, c.nome
            ORDER BY facturacion_total DESC
            LIMIT ?
            """, (limite,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados



guion = []
hoja = getSampleStyleSheet()

cabecera = hoja["Heading1"]
cabecera.fontSize=25
cabecera.alignment=0
cabecera.textColor = colors.black

titulo = Paragraph("Informe Facturación",cabecera)

cabecera2 = hoja["Heading1"]
cabecera.fontSize=15
cabecera.alignment=0
cabecera.textColor = colors.red

subtituloTorta = Paragraph("Gráfico Torta",cabecera2)
subtituloTaboa = Paragraph("Tabla de datos",cabecera2)
analise = Paragraph("Análise dos datos",cabecera2)

d = Drawing()
tarta = Pie()


tarta.x = 65
tarta.y = 15
tarta.height = 170
tarta.width = 170

factura1 = obter_clientes_maior_facturacion()[0][2]
factura2 = obter_clientes_maior_facturacion()[1][2]
factura3 = obter_clientes_maior_facturacion()[2][2]
factura4 = obter_clientes_maior_facturacion()[3][2]
factura5 = obter_clientes_maior_facturacion()[4][2]

tarta.data = [factura1,factura2,factura3,factura4,factura5]

nombre1 = obter_clientes_maior_facturacion()[0][0]
nombre2 = obter_clientes_maior_facturacion()[2][0]
nombre3 = obter_clientes_maior_facturacion()[3][0]
nombre4 = obter_clientes_maior_facturacion()[4][0]
nombre5 = obter_clientes_maior_facturacion()[5][0]

tarta.labels = [nombre1, nombre2, nombre3, nombre4, nombre5]
tarta.slices.strokeWidth = 0.5
tarta.slices[3].labelRadius = 1.75
tarta.sideLabels = 1



colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.orange]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color

d.add(tarta)

numeroF1 = obter_clientes_maior_facturacion()[0][1]
numeroF2 = obter_clientes_maior_facturacion()[1][1]
numeroF3 = obter_clientes_maior_facturacion()[2][1]
numeroF4 = obter_clientes_maior_facturacion()[3][1]
numeroF5 = obter_clientes_maior_facturacion()[4][1]

l1 = ["Pos.", "Cliente","Nª Facturas", "Facturación Total"]
l2 = ["1",nombre1,numeroF1,factura1]
l3 = ["2",nombre2,numeroF2,factura2]
l4 = ["3",nombre3,numeroF3,factura3]
l5 = ["4",nombre4,numeroF4,factura4]
l6 = ["5",nombre5,numeroF5,factura5]

taboa = Table([l1,l2,l3,l4,l5,l6])

taboa.setStyle([
    ('INNERGRID', (0, 0), (5, 6), 0.5, colors.lightgrey),
    ('RIGHTPADDING', (0, 0), (0, 4), 35),
    ('LEFTPADDING', (1, 0), (1, 4), 35),
    ('BACKGROUND', (0, 0), (5, 0), colors.red),
    ('BACKGROUND',(0,2),(5,2), colors.gray),
    ('BACKGROUND',(0,4),(5,4), colors.gray),
    ('FONTSIZE', (1, 0), (1, 0), 12),
])


textoAnalisis = hoja["Heading1"]
cabecera.fontSize=10
cabecera.alignment=0
cabecera.textColor = colors.black

analisis = Paragraph("O cliente con maior facturación é Solucións TIC Nordés SL con 5036.42$."
                     "Os 5 principais clientes representan unha facturación total de 11852.18$"
                     "A media de facturas por cliente dos primeiros 5 clientes"
                     "é de 2.2 facturas",textoAnalisis)

sp = Spacer(50,50)

doc = SimpleDocTemplate("ExamenPDF.pdf", pagesize=A4)
doc.build([titulo,sp,subtituloTorta,sp,d,sp,subtituloTaboa,sp,taboa,sp,sp,analise,sp,analisis])

print(obter_clientes_maior_facturacion())