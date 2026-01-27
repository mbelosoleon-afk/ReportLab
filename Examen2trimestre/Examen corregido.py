import sqlite3
from pydoc import pager

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph


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

def xerar_factura_pdf():
    datos = obter_clientes_maior_facturacion(10)
    cabeceira = ['Pos','Cliente','Nª Facturas','Facturación Total']
    datosTaboa = []
    datosTaboa.append(cabeceira)
    for orde, linha in enumerate (datos):
        datosTaboa.append([orde + 1, linha[0], linha[1], linha[2]])
    print(datosTaboa)

    t = Table(datosTaboa)

    estilo = [
        ('INNERGRID', (0, 0), (5, 6), 0.5, colors.lightgrey),
        ('RIGHTPADDING', (0, 0), (0, 4), 35),
        ('LEFTPADDING', (1, 0), (1, 4), 35),
        ('BACKGROUND', (0, 0), (5, 0), colors.red),
        ('BACKGROUND', (0, 2), (5, 2), colors.gray),
        ('BACKGROUND', (0, 4), (5, 4), colors.gray),
        ('FONTSIZE', (1, 0), (1, 0), 12),
    ]

    t.setStyle(estilo)

    for i in range(2,len(datosTaboa),2):
        estilo.append(('BACKGROUND',(0,i),(i,-1),colors.lightgrey))

    doc = SimpleDocTemplate("InformoeClientes.pdf", pagesize=A4)
    doc.build([t])

def xerar_tarta_pdf(datos):

    facturacion = []
    etiqueta = []
    for linha in datos:
        facturacion.append(linha[-1])
        etiqueta.append(linha[0])

    ancho = 400
    alto = 350
    debuxo = Drawing(ancho,alto)
    tarta = Pie()

    tarta.x = ancho/2-50
    tarta.y = alto/2-50
    tarta.width = 200
    tarta.height = 200
    tarta.data = facturacion
    tarta.labels = etiqueta

    guion = []
    debuxo.add(tarta)

    guion.append(debuxo)

    doc = SimpleDocTemplate("TartaClientes.pdf", pagesize=A4)
    doc.build([guion])

xerar_tarta_pdf()
xerar_factura_pdf()
