from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()

class Formulario_AutoTest(forms.Form):
    edad = forms.IntegerField()
    sexo = forms.CharField(max_length=1)
    cp = forms.CharField(max_length=5)
    fiebre = forms.BooleanField()
    tos_seca = forms.BooleanField()
    axfixia = forms.BooleanField()
    perdida_sentidos = forms.BooleanField()
    repentino = forms.BooleanField()