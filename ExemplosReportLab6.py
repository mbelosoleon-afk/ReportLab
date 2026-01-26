#---TABLAS CON PLATYPUS---

from reportlab.lib.colors import Color
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary
from reportlab.platypus import Table

imaxe = Image("box-pixilart(1).png",width=23,height=23)
texto = Paragraph("Libre")
h = ['HORARIO']
cab = ['-','Luns','Martes','Mercores','Xoves','Venres','Sabado','Domingo']
actM = ['Mañán',"Cole","Correr",[imaxe,texto],'-','-','Estudar','Traballar']
actT =['Tarde','Traballar','Clases','Clases','Clases','Traballar','Traballar','Ler']
actN = ['Noite','-','Traballar','Traballar','Traballar','-','-','-']

#Crea el objeto Table
taboa = Table([h,cab,actM,actT,actN])

#Permite aplicar una lista de comandos de estilo para dar formato a la tabla
taboa.setStyle([

    #Texto en rojo desde la columna 1 a la 7, especificamente la cuarta fila conatndo desde abajo
    ('TEXTCOLOR',(1,-4),(7,-4),colors.red),

    #Texto en azul en la primera columna, desde la fila 0 hasta la 3
    ('TEXTCOLOR',(0,0),(0,3),colors.blue),

    #Texto azul para la fila -4, desde la columna 1 hasta el final
    ('BACKGROUND',(1,-4),(-1,-4), colors.lightblue),

    #Borde exterior grueso azul alrededor de toda la tabla
    ('BOX',(0,0),(-1,-1),1,colors.blue),

    #Cuadrícula interna en color azul, excluyendo la primera fila y columna
    ('INNERGRID',(1,1),(-1,-1),0.25,colors.blue),

    #Línea verde debajo de la primera fila, de la columna 1 a la 7
    ('LINEBELOW',(1,0),(7,0),0.25, colors.lightgreen),

    #Línea vertical verde después de la primera columna
    ('LINEAFTER', (0, 1), (0, -1), 0.25, colors.lightgreen),

    #Combina (une) todas las celdas de la primera fila en una sola celda
    ('SPAN', (0, 0), (-1, 0)),

    #Centra el texto en esa primera fila combinada
    ('ALIGN',(0,0),(-1,0),'CENTER')
    ])


guion = []
guion.append(taboa)

doc = SimpleDocTemplate("5º ExemplosPlatypusTablas.pdf", pagesize = A4,showBoundary = 1)
doc.build(guion)