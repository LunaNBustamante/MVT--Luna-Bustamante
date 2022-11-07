from django.shortcuts import render
from django.http import HttpResponse
from appfamilia.models import Familia
from django.template import loader

# Create your views here.


#Creamos la funcion de view

def familia_acceso(request):

    lista_familia = Familia.objects.all()

    datos = {'lista_familia': lista_familia}

#Obtengo el template
    plantilla = loader.get_template('templates.html')


    #Renderizacion de datos

    doc = plantilla.render(datos)

    return HttpResponse(doc)


