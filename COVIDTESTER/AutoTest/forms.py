from django import forms

# Formulario principal para AutoTest
#
# Campos: 
#   - Código postal (Text, máximo de longitud 5)
#   - Edad (Number)
#   - Sexo (Select, tres opciones: Hombre, Mujer, Otro)
#   - Síntomas: (Booleanos, no requerido)
#       · Fiebre
#       · Tos seca
#       · Asfixia
#       · Perdida de sentidos
#   - Si los sintomas han sido repentinos (Booleano, no requerido)
#
class Formulario_AutoTest(forms.Form):
    cp = forms.CharField(
        max_length=5, 
        widget=forms.TextInput({"placeholder":"Código postal con formato '00000'"}))
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(("H","Hombre"),("M","Mujer"),("O","Otro")))
    fiebre = forms.BooleanField(required=False)
    tos_seca = forms.BooleanField(required=False)
    asfixia = forms.BooleanField(required=False)
    perdida_sentidos = forms.BooleanField(required=False)
    repentino = forms.BooleanField(required=False)

# Formulario secundario, por si es positivo
#
# Campos:
#   - Si se quiere contactar (Select, dos opciones: Si, No)
#   - Telefono (Text, no requerido)
#
class Formulario_Positivo(forms.Form):
    contactar = forms.ChoiceField(
        choices=[("Si","Si"),("No","No")], 
        widget=forms.RadioSelect)
    telefono = forms.CharField(
        required=False, 
        widget=forms.TextInput({"placeholder":"Teléfono con formato '000000000'"}))

# Formulario de contacto
#
# Campos: 
#   - Asunto (Text, máximo ed longitud 200)
#   - Código postal (Text, máximo de longitud 5)
#   - Edad (Number)
#   - Sexo (Select, tres opciones: Hombre, Mujer, Otro)
#   - Email (Text)
#   - Teléfono (Text, no requerido)
#
class Formulario_Contacto(forms.Form):
    asunto = forms.CharField(
        max_length=200, 
        widget=forms.TextInput({"placeholder":"Asunto"}))
    cp = forms.CharField(
        max_length=5, 
        widget=forms.TextInput({"placeholder":"Código postal con formato '00000'"})) 
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(("H","Hombre"),("M","Mujer"),("O","Otro")))
    email = forms.EmailField()
    telefono = forms.CharField(
        required=False, 
        widget=forms.TextInput({"placeholder":"Teléfono con formato '000000000'"}))