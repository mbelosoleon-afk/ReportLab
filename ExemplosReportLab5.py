from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

d = Drawing(400, 200)

titulo = Label()
titulo.setOrigin(200,190)
titulo.setText("Porcentaxe contratados/aprobados")
d.add(titulo)

lendaLateral = Label()
lendaLateral.setOrigin(10,100)
lendaLateral.angle = 90
lendaLateral.setText("Lenda lateral")
d.add(lendaLateral)

datos = [(13.3, 8, 14.4, 25, 33.3, 37.5,21.1, 28.6, 45.5, 38.1, 54.6, 36.0, 42.3), (67,69,68,81,92,90,87,82,77,86,78,97,67)]
lendaDatos = ['11/12', '12/13', '13/14', '14/15', '15/16', '16/17', '17/18', '18/19', '19/20', '20/21', '21/22', '22/23', '23/24', '24/25']

graficoBarras = VerticalBarChart()


graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 100
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -5
graficoBarras.categoryAxis.labels.angle = 15
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.barSpacing = 5

d.add(graficoBarras)

doc = SimpleDocTemplate("exemploGraficos.pdf", pagesize = A4)

doc.build([d])

