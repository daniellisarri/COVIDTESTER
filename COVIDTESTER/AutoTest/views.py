from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from AutoTest.models import Test, Usuario

from AutoTest.forms import Formulario_AutoTest, Formulario_Positivo

# Create your views here.

# Vista de inicio
def index(request):
    return render(request, "index.html", {"title":"Inicio"})

# Vista para formulario AutoTest
def auto_Test(request):
    # Si ha llegado mediante POST (tras hacer el formulario) se pasa a la vista resultado
    if request.method=="POST":
        formulario_autotest = Formulario_AutoTest(request.POST)

        # Si el formulario es válido se pasa a la vista resultado
        if formulario_autotest.is_valid():
            infForm_autotest = formulario_autotest.cleaned_data
            cp = infForm_autotest['cp']
            edad = infForm_autotest['edad']
            sexo = infForm_autotest['sexo']
            fiebre = infForm_autotest['fiebre']
            tos_seca = infForm_autotest['tos_seca']
            asfixia = infForm_autotest['asfixia']
            perdida_sentidos = infForm_autotest['perdida_sentidos']
            repentino = infForm_autotest['repentino']

            usu = Usuario(edad, sexo, cp)
            test = Test(fiebre, tos_seca, asfixia, perdida_sentidos, repentino)

            # Determina Positivo/Negativo
            if (perdida_sentidos or fiebre or tos_seca or asfixia) and repentino:
                res = True
            else:
                res = False

            # Pasa a la vista resultado, pasando datos de usuario y test
            return resultado(request, usu, test, res)
        
        # Si el formulario no es válido, regresa a AutoTest con un mensaje de error
        else:
            return render(request, "AutoTest.html", {"title":"AutoTest", "error":"Se ha producido un error", "form":formulario_autotest})

    # Si ha llegado mediante GET, va a AutoTest
    else:
        formulario_autotest = Formulario_AutoTest()

    return render(request, "AutoTest.html", {"title":"AutoTest", "form":formulario_autotest})

# Vista de "Redirección" según positivo/negativo
def resultado(request, usu, test, resultado):
    
    if resultado == True:
        formulario_positivo = Formulario_Positivo()
        contexto = {"title":"Resultado del AutoTest", "resultado":resultado, "form":formulario_positivo}
    else:
        contexto = {"title":"Resultado del AutoTest", "resultado":resultado}
    
    # Crea o substituye las cookies con el usuario y el test
    response = render(request, "resultado.html", contexto)
    response.set_cookie(key="usuario", value=usu)
    response.set_cookie(key="test", value=test)

    return response

# Vista para el formulario secundario, si es positivo
def positivo(request):

    if request.method == "POST":
        formulario_positivo = Formulario_Positivo(request.POST)

        if formulario_positivo.is_valid():
            infForm_positivo = formulario_positivo.cleaned_data
            contactar = infForm_positivo['contactar']
            telefono = infForm_positivo['telefono']

            print(telefono)

            if contactar == "Si" and telefono != "":
                print("QUIERE CONTACTAR")
                #
                #
                #
            else:
                print("NO QUIERE CONTACTAR")
                #
                #
                #

            return render(request, "index.html", {"title":"LLEGA, VALIDO"})
        else:
            return render(request, "index.html", {"title":"LLEGA, NO VALIDO"})
        
    else:
        formulario_positivo = Formulario_Positivo()

    return render(request, "resultado.html", {"title":"Resultado del AutoTest", "form":formulario_positivo})
    

def condiciones(request):
    return render(request, "condiciones.html", {"title":"Condiciones y políticas"})
