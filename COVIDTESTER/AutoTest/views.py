from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

from AutoTest.models import Formulario, Usuario

from AutoTest.forms import Formulario_AutoTest

# Create your views here.

### Vista index
### Vista formulario AutoTest
### Vista positivo
### Vista negativo

def index(request):
    return render(request, "index.html", {"title":"Inicio"})

def auto_Test(request):

    if request.method=="POST":

        formulario = Formulario_AutoTest(request.POST)

        if formulario.is_valid():
            infForm = formulario.cleaned_data
            cp = infForm['cp']
            edad = infForm['edad']
            sexo = infForm['sexo']
            fiebre = infForm['fiebre']
            tos_seca = infForm['tos_seca']
            asfixia = infForm['asfixia']
            perdida_sentidos = infForm['perdida_sentidos']
            repentino = infForm['repentino']

            print(formulario.cleaned_data)

            #############

            # AQUÍ DECIDIMOS A DONDE REDIRIGIR, SI ES POSITIVO O NEGATIVO
            #por ahora te redirije a un prueba.html porque aun no dispongo de los html de positivo y negativo (pendiente de cambio) Javi
            #la condicion es verdadera si cualquiera de las variables del parentesis es true y si repentino es true, 
            #si no se cumple te envia al index.html (pendiente de cambio cuando este el archivo negativo) Javi
            if (perdida_sentidos or fiebre or tos_seca or asfixia) and repentino :
                return render(request, "prueba.html", {"title": "infectado"})
            else:
                return render(request, "index.html", {"title": "no infectado"})
            #return render(request, "index.html", {"title":"FORMULARIO ENVIADO"}) # Esta linea es para comprobar que funciona, pero sobra
    else:
        formulario = Formulario_AutoTest()

    return render(request, "AutoTest.html", {"title":"AutoTest", "form":formulario})

def condiciones (request):
    return render(request, "condiciones.html", {"title":"Condiciones y políticas"})
