from django.db import models

# Create your models here.

### Modelo Usuario
# Contiene edad, sexo, código postal y (opcionalmente) nº de teléfono
class Usuario(models.Model):
    id = models.IntegerField(primary_key='true')
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cp = models.CharField(max_length=5)
    telefono = models.CharField(max_length=9, null=True, blank=True) # min_lenght????
    
    # Método constructor. Sin teléfono
    def __init__(self, id, edad, sexo, cp):
        self.id = id
        self.edad = edad
        self.sexo = sexo
        self.cp = cp
        self.telefono = "__" # IS NONE #################################################################

    # Método para convertirlo en String
    def __str__(self):
        return "ID del usuario: " + str(self.id) + "Edad: " + str(self.edad) + ", Sexo: " + self.sexo + ", CP:" + self.cp + ", Teléfono: " + self.telefono

### Modelo Formulario
# Contiene los síntomas en campos booleanos
class Test(models.Model):
    id = models.IntegerField(primary_key='true')
    idUsuario = models.IntegerField()
    fiebre = models.BooleanField()
    tos_seca = models.BooleanField()
    asfixia = models.BooleanField()
    perdida_sentidos = models.BooleanField()
    repentino = models.BooleanField()
    # resultado = models.BooleanField() # Positivo = True
    # id_usuario
    
    # Método constructor
    def __init__(self, id, idUsuario, fiebre, tos_seca, asfixia, perdida_sentidos, repentino):
        self.id = id
        self.idUsuario = idUsuario
        self.fiebre = fiebre
        self.tos_seca = tos_seca
        self.asfixia = asfixia
        self.perdida_sentidos = perdida_sentidos
        self.repentino = repentino
    
    # Método para convertirlo en String
    def __str__(self):
        return "ID del test: " + self.id + "ID del usuario: " + str(self.idUsuario) + "Fiebre: " + str(self.fiebre) + ", Tos seca: " + str(self.tos_seca) + ", Asfixia: " + str(self.asfixia) + ", Perdida sentidos: " + str(self.perdida_sentidos) + ", Repentino: " + str(self.repentino)