from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.rl_settings import strikeWidth

#Contenedor del gráfico y sus etiquetas
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

#Datos del gráfico como una lisa de tuplas
datos = [(13.3, 8, 14.4, 25, 33.3, 37.5,21.1, 28.6, 45.5, 38.1, 54.6, 36.0, 42.3), (67,69,68,81,92,90,87,82,77,86,78,97,67)]
lendaDatos = ['11/12', '12/13', '13/14', '14/15', '15/16', '16/17', '17/18', '18/19', '19/20', '20/21', '21/22', '22/23', '23/24', '24/25']

#El objeto gráfico
graficoBarras = VerticalBarChart()


graficoBarras.x = 50 #Desplazamiento horizontal
graficoBarras.y = 50 #Desplazamiento vertical
graficoBarras.height = 125 #Altura
graficoBarras.width = 300 #Ancho
graficoBarras.data = datos #Asigna la lista de tuplas que se convenrtirán en barras
graficoBarras.valueAxis.valueMin = 0 #Valor min Y
graficoBarras.valueAxis.valueMax = 70 #Valor max X
graficoBarras.valueAxis.valueStep = 10 #Indica cada cuanto se dibuja una marca o número en el eje
graficoBarras.categoryAxis.labels.boxAnchor = 'ne' #Punto de anclaje de la etiqueta, puntos cardinales
graficoBarras.categoryAxis.labels.dx = 8 #Desplazamiento X
graficoBarras.categoryAxis.labels.dy = -10 #Desplazamiento Y
graficoBarras.categoryAxis.labels.angle = 30 #Rota el texto
graficoBarras.categoryAxis.categoryNames = lendaDatos #Asigna los nombres de las categorías a cada grupo de barras
graficoBarras.groupSpacing = 10 #Espacio entre puntos

d.add(graficoBarras)

d2 = Drawing(400, 200)

graficoLinhas = HorizontalLineChart()

graficoLinhas.x = 30
graficoLinhas.y = 100
graficoLinhas.height = 125
graficoLinhas.width = 350
graficoLinhas.data = datos
graficoLinhas.categoryAxis.categoryNames = lendaDatos
graficoLinhas.categoryAxis.labels.boxAnchor = 'n' #Puntos cardinales
graficoLinhas.valueAxis.valueMin = 0 #Valor min Y
graficoLinhas.valueAxis.valueMax = 100 #Valor max Y
graficoLinhas.valueAxis.valueStep = 20
graficoLinhas.lines[0].strokeWidth = 2 #La línea 0 es más gruesa
graficoLinhas.lines[0].symbol = makeMarker('FilledCircle') #Añade un círculo en cada puntos de datos
graficoLinhas.lines[1].strokeWidth = 1.5

d2.add(graficoLinhas)

d3 = Drawing(400,200)

#Gráfico circular
tarta = Pie()

tarta.x = 65
tarta.y = 15
tarta.height = 170
tarta.width = 170
tarta.data = [10,20,30,40,50]
tarta.labels = ['Oppo', 'Pixel', 'Galaxy', 'Iphone', 'Xiaomi']
tarta.slices.strokeWidth = 0.5
tarta.slices[3].popout = 10 #Saca el cuarto sector [3] hacia afuera 10 puntos
tarta.slices[3].strokeDashArray = [2,2] #Línea a trazos [longitud trazo, longitud espacio en blanco
tarta.slices[3].labelRadius = 1.75 #A q distancia del centro se pone la etiqueta
tarta.slices[3].fontColor = colors.red
tarta.sideLabels = 1


colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.orange]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color

lenda = Legend()

lenda.colorNamePairs = [(tarta.slices[i].fillColor, (tarta.labels[i][0:20],
                        '%0.2f' % tarta.data[i]))
                        for i in range (len(tarta.data))]

lenda.x = 370
lenda.y = 5
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 3
lenda.strokeWidth = 1 #Borde de un punto de grosor
lenda.strokeColor = colors.black #El borde es de color negro
lenda.deltax = 75 #Distancia horizontal entre el inicio de una columna y la siguiente
lenda.deltay = 10 #Distancia vertical entre cada fila
lenda.autoXPadding = 5 #Espacio de seguridad horizontal automático
lenda.yGap = 0 #Espacio extra entre las muestras de color
lenda.dxTextSpace = 5 #Espacio que hay entre el cuadrado de color y el texto que lo acompaña
lenda.alignment = 'right' #Texto a la derecha respecto al punto de referencia
lenda.dividerLines = 1|2|4
lenda.dividerOffsY = 5.5
lenda.subCols.rpad = 30 #Añade un relleno a la derecha de las subcolumnas

d3.add(lenda)


d3.add(tarta)
doc = SimpleDocTemplate("exemploGraficos.pdf", pagesize = A4)

doc.build([d, Spacer(20,20),d2, Spacer(20,20), d3])

