from django.db import models

# Create your models here.

### Modelo Usuario
# Contiene edad, sexo, código postal y (opcionalmente) nº de teléfono
class Usuario(models.Model):
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cp = models.CharField(max_length=5)
    telefono = models.CharField(max_length=7, null=True, blank=True)

### Modelo Formulario
# Contiene los síntomas en campos booleanos
class Formulario(models.Model):
    fiebre = models.BooleanField()
    tos_seca = models.BooleanField()
    axfixia = models.BooleanField()
    perdida_sentidos = models.BooleanField()
    repentino = models.BooleanField()