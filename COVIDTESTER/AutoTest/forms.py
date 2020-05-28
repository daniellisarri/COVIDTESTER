from django import forms

# Formulario principal para AutoTest
class Formulario_AutoTest(forms.Form):
    cp = forms.CharField(
        max_length=5, 
        widget=forms.TextInput({"placeholder":"Código postal con formato '00000'"})) # validators="(?:0[1-9]|[1-4]\d|5[0-2])r\d{3}") # validators=["(?:0[1-9]|[1-4]\d|5[0-2])\d{3}"]
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(("H","Hombre"),("M","Mujer"),("O","Otro")))
    fiebre = forms.BooleanField(required=False)
    tos_seca = forms.BooleanField(required=False)
    asfixia = forms.BooleanField(required=False)
    perdida_sentidos = forms.BooleanField(required=False)
    repentino = forms.BooleanField(required=False)

# Formulario secundario, por si es positivo
class Formulario_Positivo(forms.Form):
    contactar = forms.ChoiceField(
        choices=[("Si","Si"),("No","No")], 
        widget=forms.RadioSelect)
    telefono = forms.CharField(
        required=False, 
        widget=forms.TextInput({"placeholder":"Teléfono con formato '000000000'"}))

# Formulario de contacto
class Formulario_Contacto(forms.Form):
    cp = forms.CharField(
        max_length=5, 
        widget=forms.TextInput({"placeholder":"Código postal con formato '00000'"})) 
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(("H","Hombre"),("M","Mujer"),("O","Otro")))
    email = forms.EmailField()
    telefono = forms.CharField(
        required=False, 
        widget=forms.TextInput({"placeholder":"Teléfono con formato '000000000'"}))