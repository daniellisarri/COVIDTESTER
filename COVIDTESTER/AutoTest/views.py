from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

from AutoTest.models import Formulario, Usuario

# Create your views here.

### Vista index
### Vista formulario AutoTest
### Vista positivo
### Vista negativo

def index(request):
    return render(request, "index.html", {"title":"Inicio"})

def auto_Test(request):
    return render(request, "AutoTest.html", {"title":"Autotest"})


