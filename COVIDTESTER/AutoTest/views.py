from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

# Importación de formularios de la API forms
from AutoTest.forms import Formulario_AutoTest, Formulario_Positivo, Formulario_Contacto

# Importación de módulo externo recogida_datos para utilizar la API de datos
from AutoTest import recogida_datos

# Importación de módulo externo para comprobar códigos postales
from AutoTest import codigos_postales

# Importación de los modelos para inserción en base de datos
from AutoTest.models import Test, Usuario

# Importación del módulo externo para gestionar la base de datos
from AutoTest import gestorBD

# Vista de inicio
#
# Sólo renderiza el archivo "index.html" y le pasa el título mediante el contexto
#
# Vista usual, recibe request y devuelve response, renderizado
def index(request):
    datos = recogida_datos.recoger_datos()
    datos["title"] = "AutoTest"
    return render(request, "index.html", datos)

# Vista antetrior al formulario AutoTest
#
# Sólo renderiza el archivo preAutoTest.html y le pása el titulo mediante el conexto
# 
# Vista usuarl, recibe request y devuelve response, renderizado
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
# Vista usual, recibe request y devuelve response, renderizado o llamada a pseudovista "resultado"
def auto_Test(request):
    # Comprueba si ha llegado mediante POST (Si ha llegado mediante GET, todavía no ha enviado el formulario)
    if request.method=="POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_autotest = Formulario_AutoTest(request.POST)

        # Comprueba que el formulario sea válido
        if formulario_autotest.is_valid():
            # Si el formulario es válido, recoge los datos
            infForm_autotest = formulario_autotest.cleaned_data

            # Datos de USUARIO
            cp = infForm_autotest['cp']
            edad = infForm_autotest['edad']
            sexo = infForm_autotest['sexo']
            
            # Datos de TEST
            fiebre = infForm_autotest['fiebre']
            tos_seca = infForm_autotest['tos_seca']
            asfixia = infForm_autotest['asfixia']
            perdida_sentidos = infForm_autotest['perdida_sentidos']
            repentino = infForm_autotest['repentino']

            # Comprueba que el código posta es correcto, utilizando el módulo externo de apoyo
            cp_correcto = codigos_postales.es_valido(cp)

            # Si el código postal no es válido, recarga el formulario sacando un mensaje de error
            if not cp_correcto:
                return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Código postal no válido. Ese código postal no existe en el territorio español.", "form":formulario_autotest})

            # Determina Positivo/Negativo
            if (perdida_sentidos or fiebre or tos_seca or asfixia) and repentino:
                res = True
            else:
                res = False
            
            # Crea los STRING con los datos para introducción en base de datos más adelante
            usu = str(edad) + "#" + str(sexo) + "#" + str(cp)
            test = str(fiebre) + "#" + str(tos_seca) + "#" + str(asfixia) + "#" + str(perdida_sentidos) + "#" + str(repentino) + "#" + str(res)

            # Pasa a la vista resultado, pasando datos de usuario, test y resultado
            return resultado(request, usu, test, res)
        
        else:
            # Si el formulario no es válido, regresa a AutoTest con un mensaje de error
            return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Se ha producido un error desconocido.", "form":formulario_autotest})
        
    else:
        # Si ha llegado mediante GET, recarga el formulario de cero
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
# Pseudovista, recibe datos del formulario principal y devuelve response
def resultado(request, usu, test, resultado):
    # Comprueba si el resultado es positivo/negativo
    if resultado == True:
        # Si es positivo, crea el formulario secundario y contexto correspondiente
        formulario_positivo = Formulario_Positivo()
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
# Vista usual, recibe request y devuelve response
def posible_positivo(request):
    # Comprueba si ha llegado mediante POST (Si ha llegado mediante GET, todavía no ha enviado el formulario)
    if request.method == "POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_positivo = Formulario_Positivo(request.POST)
        
        # Comprueba que el formulario sea válido
        if formulario_positivo.is_valid():
            # Si el formulario es válido, recoge los datos
            infForm_positivo = formulario_positivo.cleaned_data
            contactar = infForm_positivo['contactar']
            telefono = infForm_positivo['telefono']

            #
            # Recibe STRINGS
            # Hay que introducir el teléfono en el usuario (si quiere ser contactad@),
            # transformarlo a los objetos del models.py,
            # y finalmente introducirlos en la base de datos utilizando el módulo gestor externo
            #
            usu = str(request.COOKIES['usuario'])
            sexo = usu.split("#", 2)[1]
            edad = usu.split("#", 1)[0]
            cp = usu.split("#", 3)[2]
            usu_final = Usuario(0, edad, sexo, cp, telefono)
            gestorBD.insertar_Usuario(usu_final)

            test = str(request.COOKIES['test'])
            fiebre = test.split("#", 1)[0]
            tos_seca = test.split("#", 2)[1]
            asfixia = test.split("#", 3)[2]
            perdida_sentidos = test.split("#", 4)[3]
            repentino = test.split("#", 5)[4]
            res = test.split("#", 6)[5]
            test_final = Test(0, 0, fiebre, tos_seca, asfixia, perdida_sentidos, repentino, res)
            gestorBD.insertar_Test(test_final)

            # Comprueba si el usuario quiere ser contactado
            if contactar == "Si" and telefono != "":
                contacto = True
            else:
                contacto = False

            # Renderiza la página index.html pasándole, además de los datos de la API, si quiere ser contactad@o no 
            datos = recogida_datos.recoger_datos()
            datos["title"] = "AutoTest"
            datos["resultado"] = "positivo"
            datos["contacto"] = contacto
            return render(request, "index.html", datos)

        else:
            # Si el formulario no es válido, regresa a AutoTest con un mensaje de error
            return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Se ha producido un error desconocido.", "form":formulario_positivo})
    else:
        # Si ha llegado mediante GET, recarga el formulario de cero
        formulario_positivo = Formulario_Positivo()

    # Retorna el renderizado básico de resultado
    return render(request, "resultado.html", {"title":"Resultado del AutoTest", "form":formulario_positivo})

# Vista para mostrar resultado negativo y datos en index.html
#
# Sólo renderiza el archivo index.html y le pása el titulo mediante el conexto, así como los datos recogidos
# 
# Vista usuarl, recibe request
def negativo(request):
    #
    # Recibe STRINGS
    # Hay que transformarlo a los objetos del models.py,
    # y finalmente introducirlos en la base de datos utilizando el módulo gestor externo
    #
    usu = str(request.COOKIES['usuario'])
    cp = usu.split("#", 3)[2]
    edad = usu.split("#", 1)[0]
    sexo = usu.split("#", 2)[1]
    usu_final = Usuario(0, edad, sexo, cp, "")
    gestorBD.insertar_Usuario(usu_final)

    test = str(request.COOKIES['test'])
    fiebre = test.split("#", 1)[0]
    tos_seca = test.split("#", 2)[1]
    asfixia = test.split("#", 3)[2]
    perdida_sentidos = test.split("#", 4)[3]
    repentino = test.split("#", 5)[4]
    res = test.split("#", 6)[5]
    test_final = Test(0, 0, fiebre, tos_seca, asfixia, perdida_sentidos, repentino, res)
    gestorBD.insertar_Test(test_final)

    # Renderiza la página index.html pasándole, además de los datos de la API, que el resultado es negativo
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
    # Comprueba si ha llegado mediante POST (Si ha llegado mediante GET, todavía no ha enviado el formulario)
    if request.method=="POST":
        # Si he llegado mediante POST (tras hacer el formulario), recoge el formulario 
        formulario_contacto = Formulario_Contacto(request.POST)

        # Comprueba que el formulario sea válido
        if formulario_contacto.is_valid():
            # Si el formulario es válido, recoge los datos
            infForm_contacto = formulario_contacto.cleaned_data

            asunto = infForm_contacto['asunto']
            cp = infForm_contacto['cp']
            edad = infForm_contacto['edad']
            sexo = infForm_contacto['sexo']
            email = infForm_contacto['email']
            telefono = infForm_contacto['telefono']

            # Comprueba que el código posta es correcto, utilizando el módulo externo de apoyo
            cp_correcto = codigos_postales.es_valido(cp)

            # Si el código postal no es válido, recarga el formulario sacando un mensaje de error
            if not cp_correcto:
                return render(request, "contacto.html", {"title":"Contactar", "error":"Se ha producido un error", "form":formulario_contacto})
            
            # Creación del cuerpo del email
            mensaje = "Una persona con los siguientes datos quiere ponerse en contacto con profesionales sanitarios: \n" \
                        "Código postal: " + str(cp) + "\n" \
                        "Edad: " + str(edad) + "\n" \
                        "Sexo: " + str(sexo) + "\n" \
                        "Email: " + str(email) + "\n" \
                        "Teléfono: " + str(telefono) + "\n\n" \
                       "Conforme al siguiente asunto: \n" \
                        "Asunto: " + str(asunto)
            
            # Parámetros para envío de mail
            email_from = settings.EMAIL_HOST_USER
            lista_destinatarios = ["COVIDTESTER.0@gmail.com"]

            # Envío del mail
            send_mail(asunto, mensaje, email_from, lista_destinatarios) # , fail_silently=False

            # Pasa a la vista index pasando mensaje
            datos = recogida_datos.recoger_datos()
            datos["title"] = "AutoTest"
            datos["contactar_enviado"] = True
            return render(request, "index.html", datos)
        
        else:
            # Si el formulario no es válido, regresa a contacto.html con un mensaje de error
            return render(request, "contacto.html", {"title":"Contactar", "error":"Se ha producido un error desconocido.", "form":formulario_contacto})
        
    else:
        # Si ha llegado mediante GET, crea el formulario de cero
        formulario_contacto = Formulario_Contacto()

    # Retorna el renderizado básico de contacto.html
    return render(request, "contacto.html", {"title":"Contactar", "form":formulario_contacto})