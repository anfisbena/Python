#IMPORT SPACE
from django.http import HttpResponse 
import datetime

def saludo(request):

    documento = '''
    <html>
    <body>
    <h1> Hola Mundo </h1>
    </body>
    </html>
'''

    return HttpResponse(documento)

def despedida(request):
    
    return HttpResponse('Hasta luego anacronicos')

def fecha(request):
    
    fecha = datetime.datetime.now()
    
    documento = '''
    <html>
    <body>
    <h1> fecha actual </h1> %s 
    </body>
    </html>''' %fecha
    # el % es un marcador que ayuda a colocar cosas en sitios y luego definirlas
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