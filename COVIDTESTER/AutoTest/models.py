from django.db import models

# Create your models here.

### Crear clase Formulario
### Crear clase Usuario

class Formulario(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre

class Usuario(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
