from django import forms

class Formulario_AutoTest(forms.Forms):
    cp = forms.CharField()
    edad = forms.IntegerField()
    sexo = forms.CharField()