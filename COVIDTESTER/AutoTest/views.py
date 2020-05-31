from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.contrib import messages

from AutoTest.models import Test, Usuario

from AutoTest.forms import Formulario_AutoTest, Formulario_Positivo, Formulario_Contacto

from AutoTest import recogida_datos

from django.core.files import File

import os

from django.core.mail import send_mail
from django.conf import settings

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

# Vista antetrior al formulario AutoTest
#
# Sólo renderiza el archivo preAutoTest.html y le pása el titulo mediante el conexto
# 
# Vista usuarl, recibe request
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

            # Comprueba que el código posta es correcto comparandolo con una lista
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

            # Determina Positivo/Negativo
            if (perdida_sentidos or fiebre or tos_seca or asfixia) and repentino:
                res = True
            else:
                res = False
            
            # Crea los objetos para introducción en base de datos más adelante
            #usu = Usuario(edad, sexo, cp)
            #test = Test(fiebre, tos_seca, asfixia, perdida_sentidos, repentino, res)
            usu = {
                "edad":edad,
                "sexo":sexo,
                "cp":cp
            }
            test = {
                "fiebre":fiebre,
                "tos_seca":tos_seca,
                "asfixia":asfixia,
                "perdida_sentidos":perdida_sentidos,
                "repentino":repentino,
                "res":res
            }

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

            #
            # Objetos JSON
            # Hay que introducir el teléfono en el usuario (si quiere ser contactad@),
            # transformarlo a los objetos del models.py,
            # y finalmente introducirlos en la base de datos
            #
            usu = request.COOKIES['usuario']
            test = request.COOKIES['test']

            print("USUARIO------->" + usu)
            print("TEST---------->" + test)

            #
            # GUARDAR LOS OBJETOS EN BBDD
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

# Vista para mostrar resultado negativo y datos en index.html
#
# Sólo renderiza el archivo index.html y le pása el titulo mediante el conexto, así como los datos recogidos
# 
# Vista usuarl, recibe request
def negativo(request):

    #
    # Objetos JSON
    # Hay que transformarlo a los objetos del models.py,
    # y finalmente introducirlos en la base de datos
    #
    usu = request.COOKIES['usuario']
    test = request.COOKIES['test']

    print("USUARIO------->" + usu)
    print("TEST---------->" + test)

    #
    # GUARDAR LOS OBJETOS EN BBDD
    #

    datos = recogida_datos.recoger_datos()
    datos["title"] = "AutoTest"
    datos["resultado"] = "negativo"
    return render(request, "index.html", datos)

# Vista para mostrar documento de condiciones y políticas.
#
# Sólo renderiza el archivo condiciones.html y le pása el titulo mediante el conexto
# 
# Vista usuarl, recibe request
def condiciones(request):
    return render(request, "condiciones.html", {"title":"Condiciones y políticas"})

# Vista para formulario de contacto
#
# 1. Renderiza el archivo "contacto.html", pasando el formulario de contacto, título y un
#   mensaje de error en caso necesario mediante contexto. 
# 2. Si se ha completado el formulario sin problemas, envía un email
# 3. Regresa a index.html pasando un mensaje
#
# Vista usual, recibe request
def contacto(request):
    # Comprueba si ha llegado mediante POST
    if request.method=="POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_contacto = Formulario_Contacto(request.POST)

        # Comprueba que el formulario sea válido
        if formulario_contacto.is_valid():
            # Si el formulario es válido comprueba resultado y se pasa a la vista resultado
            infForm_contacto = formulario_contacto.cleaned_data

            #print(infForm_contacto)

            asunto = infForm_contacto['asunto']
            cp = infForm_contacto['cp']
            edad = infForm_contacto['edad']
            sexo = infForm_contacto['sexo']
            email = infForm_contacto['email']
            telefono = infForm_contacto['telefono']

            # Comprueba que el código posta es correcto comparandolo con una lista
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
                return render(request, "contacto.html", {"title":"Contactar", "error":"Se ha producido un error", "form":formulario_contacto})
            
            # ENVIAR EMAIL
            # asunto 
            mensaje = "Una persona con los siguientes datos quiere ponerse en contacto con profesionales sanitarios: \n" \
                        "Código postal: " + str(cp) + "\n" \
                        "Edad: " + str(edad) + "\n" \
                        "Sexo: " + str(sexo) + "\n" \
                        "Email: " + str(email) + "\n" \
                        "Teléfono: " + str(telefono) + "\n\n" \
                       "Conforme al siguiente asunto: \n" \
                        "Asunto: " + str(asunto)
            
            email_from = settings.EMAIL_HOST_USER
            lista_destinatarios = ["COVIDTESTER.0@gmail.com"]
            send_mail(asunto, mensaje, email_from, lista_destinatarios) # , fail_silently=False

            # Pasa a la vista index pasando mensaje
            datos = recogida_datos.recoger_datos()
            datos["title"] = "AutoTest"
            datos["contactar_enviado"] = True
            return render(request, "index.html", datos)
        
        else:
            # Si el formulario no es válido, regresa a AutoTest con un mensaje de error
            return render(request, "contacto.html", {"title":"Contactar", "error":"Se ha producido un error", "form":formulario_contacto})
        
    else:
        # Si ha llegado mediante GET, crea el formulario de cero
        formulario_contacto = Formulario_Contacto()

    # Retorna el renderizado básico de AutoTest
    return render(request, "contacto.html", {"title":"Contactar", "form":formulario_contacto})