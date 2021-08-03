#IMPORT SPACE
from django.http import HttpResponse 
import datetime
from django.template import Template,Context

class persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
#OPEN the Template
    Pl_Saludo = open("C:/Users/Sebastian/Documents/GitHub/Python/Waypoint/Django/dummy1/dummy1/plantillas/saludo.html")
    plt=Template(Pl_Saludo.read())
    Pl_Saludo.close()
#CONTEXT the template    
    p1=persona('Pepito','Perez')
    ctx=Context({"nombre":p1.nombre, "apellido":p1.apellido,"temas":['plantillas',"Modelos","Formularios","Vistas","Despliegue de la app"]})
#RENDER the template
    documento=plt.render(ctx)
    return HttpResponse(documento)


def despedida(request):    
    return HttpResponse('Hasta luego anacronicos')

def fecha(request):
#OPEN the Template

    Pl_Fecha = open("C:/Users/Sebastian/Documents/GitHub/Python/Waypoint/Django/dummy1/dummy1/plantillas/Fecha.html")
    plt=Template(Pl_Fecha.read())
    Pl_Fecha.close()
#CONTEXT the template    
    ctx=Context({"fecha":datetime.datetime.now()})
#RENDER the template
    documento=plt.render(ctx)
    return HttpResponse(documento)

def calculaEdad(request,edad,futuro):
    periodo = futuro - datetime.datetime.now().year
    final = periodo + edad
    documento= '''
    <html>
    <body>
    <h1> en el año %s tendras %s años 
    </body>
    </html>
    ''' %(futuro,final)

    if periodo <=0:
        return HttpResponse ('<html><body><h1>escribe un valor futuro</h1></body></html>')
    else:
        return HttpResponse (documento)