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
            #
            #
            #
            return render(request, "index.html", {"title":"FORMULARIO ENVIADO"}) # Esta linea es para comprobar que funciona, pero sobra
    else:
        formulario = Formulario_AutoTest()

    return render(request, "AutoTest.html", {"title":"AutoTest", "form":formulario})

def condiciones (request):
    return render(request, "condiciones.html", {"title":"Condiciones y políticas"})