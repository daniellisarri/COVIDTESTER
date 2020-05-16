from django import forms

class Formulario_AutoTest(forms.Form):
    cp = forms.CharField(
        max_length=5, 
        widget = forms.TextInput({"placeholder":"Código postal"}))
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(("Hombre","Hombre"),("Mujer","Mujer")))
    fiebre = forms.BooleanField(required=False)
    tos_seca = forms.BooleanField(required=False)
    asfixia = forms.BooleanField(required=False)
    perdida_sentidos = forms.BooleanField(required=False)
    repentino = forms.BooleanField(required=False)