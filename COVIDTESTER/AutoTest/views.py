from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.contrib import messages

from AutoTest.models import Test, Usuario

from AutoTest.forms import Formulario_AutoTest, Formulario_Positivo

from AutoTest import recogida_datos

from django.core.files import File

import os

# Create your views here.

# Vista de inicio
#
# Sólo renderiza el archivo "index.html" y le pasa el título mediante el contexto
#
# Vista usual, recibe request
def index(request):
    datos = recogida_datos.recoger_datos()
    datos["title"] = "AutoTest"

    return render(request, "index.html", datos)

#
#
#
def pre_auto_Test(request):
    return render(request, "preAutoTest.html", {"title":"AutoTest"})

# Vista para formulario AutoTest
#
# 1. Renderiza el archivo "AutoTest.html", pasando el formulario principal, título y un
#   mensaje de error en caso necesario mediante contexto. 
# 2. Si se ha completado el formulario sin problemas, determina si es positivo/negativo
# 3. Una vez determinado el resultado redirige a la vista "resultado" pasando 
#   usuario, formulario y resultado (información del test) como parámetros
#
# Vista usual, recibe request
def auto_Test(request):
    # Comprueba si ha llegado mediante POST
    if request.method=="POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_autotest = Formulario_AutoTest(request.POST)

        # Comprueba que el formulario sea válido
        if formulario_autotest.is_valid():
            # Si el formulario es válido comprueba resultado y se pasa a la vista resultado
            infForm_autotest = formulario_autotest.cleaned_data

            cp = infForm_autotest['cp']
            edad = infForm_autotest['edad']
            sexo = infForm_autotest['sexo']

            fiebre = infForm_autotest['fiebre']
            tos_seca = infForm_autotest['tos_seca']
            asfixia = infForm_autotest['asfixia']
            perdida_sentidos = infForm_autotest['perdida_sentidos']
            repentino = infForm_autotest['repentino']

            ###
            ###
            ###
            cp_correcto = False
            fichero_cp = open(os.getcwd()+"\AutoTest\static\CP", "r")
            while not cp_correcto:
                linea = fichero_cp.readline().rstrip("\n")
                if linea==cp:
                    cp_correcto = True
                    break
                if not linea:
                    break
            fichero_cp.close()

            if not cp_correcto:
                return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Se ha producido un error", "form":formulario_autotest})
            ###
            ###
            ###

            usu = Usuario(edad, sexo, cp)
            test = Test(fiebre, tos_seca, asfixia, perdida_sentidos, repentino)

            # Determina Positivo/Negativo
            if (perdida_sentidos or fiebre or tos_seca or asfixia) and repentino:
                res = True
            else:
                res = False

            # Pasa a la vista resultado, pasando datos de usuario, test y resultado
            return resultado(request, usu, test, res)
        
        else:
            # Si el formulario no es válido, regresa a AutoTest con un mensaje de error
            return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Se ha producido un error", "form":formulario_autotest})
        
    else:
        # Si ha llegado mediante GET, crea el formulario de cero
        formulario_autotest = Formulario_AutoTest()

    # Retorna el renderizado básico de AutoTest
    return render(request, "AutoTest.html", {"title":"AutoTest", "form":formulario_autotest})

# Vista de "Redirección" según positivo/negativo
#
# 1. Comprueba si el resultado ha sido positivo
# 2. Crea el contexto para "resultado.html", pasando el titulo, resultado y formulario secundario
#   en caso POSITIVO. Sólo título y resultado en caso NEGATIVO.
# 3. Crea/Superpone las cookies con usuario y test completo
# 4. Renderiza el archivo "resultado.html" y lo devuelve como response
#
# Pseudovista, recibe datos del formulario principal
def resultado(request, usu, test, resultado):
    # Comprueba si el resultado es positivo/negativo
    if resultado == True:
        # Si es positivo, crea el formulario secundario y contexto correspondiente
        formulario_positivo = Formulario_Positivo()
        # AUTOPOSTBACK
        contexto = {"title":"Resultado del AutoTest", "resultado":resultado, "form":formulario_positivo}
    else:
        # Si es negativo, crea el contexto correspondiente
        contexto = {"title":"Resultado del AutoTest", "resultado":resultado}
    
    # Crea o sustituye las cookies con el usuario y el test
    response = render(request, "resultado.html", contexto)
    response.set_cookie(key="usuario", value=usu)
    response.set_cookie(key="test", value=test)

    # Retorna el renderizado de resultado
    return response

# Vista para recibir el formulario secundario (positivo)
#
# 1. Renderiza el archivo "resultado.html", pasando el formulario secundario y título
# 2. Si se ha completado el formulario sin problemas, determina si se quiere contactar
# 3. Una vez determinado si se quiere contactar, redirige a la página correspondiente
#
# Vista usual, recibe request
def posible_positivo(request):
    # Comprueba si ha llegado mediante POST
    if request.method == "POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_positivo = Formulario_Positivo(request.POST)
        
        # Comprueba que el formulario sea válido
        if formulario_positivo.is_valid():
            # Si el formulario es válido comprueba resultado y se pasa a la página correspondiente
            infForm_positivo = formulario_positivo.cleaned_data
            contactar = infForm_positivo['contactar']
            telefono = infForm_positivo['telefono']

            usu = request.COOKIES['usuario']
            test = request.COOKIES['test']

            #
            # GUARDAR LOS DATOS
            #

            if contactar == "Si" and telefono != "":
                # messages.info(request, "Se le contactará......")
                contacto = True
            else:
                # messages.info(request, "No se le contactará pero......")
                contacto = False

            datos = recogida_datos.recoger_datos()
            datos["title"] = "AutoTest"
            datos["resultado"] = "positivo"
            datos["contacto"] = contacto
            return render(request, "index.html", datos)

        else:
            return render(request, "index.html", {"title":"LLEGA, NO VALIDO"})
    else:
        formulario_positivo = Formulario_Positivo()

    return render(request, "resultado.html", {"title":"Resultado del AutoTest", "form":formulario_positivo})

def negativo(request):
    datos = recogida_datos.recoger_datos()
    datos["title"] = "AutoTest"
    datos["resultado"] = "negativo"
    return render(request, "index.html", datos)

def condiciones(request):
    return render(request, "condiciones.html", {"title":"Condiciones y políticas"})

