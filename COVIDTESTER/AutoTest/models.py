from django.db import models

# Create your models here.

### Modelo Usuario
# Contiene edad, sexo, código postal y (opcionalmente) nº de teléfono
class Usuario(models.Model):
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cp = models.CharField(max_length=5)
    telefono = models.CharField(max_length=9, null=True, blank=True, default="") # min_lenght????
    
    # Método para convertirlo en String
    def __str__(self):
        return "Edad: " + str(self.edad) + ", Sexo: " + str(self.sexo) + ", CP:" + str(self.cp) + ", Teléfono: " + str(self.telefono)

### Modelo Formulario
# Contiene los síntomas en campos booleanos
class Test(models.Model):
    usuario = models.ForeignKey(Usuario, default=None, on_delete=models.CASCADE)
    fiebre = models.BooleanField()
    tos_seca = models.BooleanField()
    asfixia = models.BooleanField()
    perdida_sentidos = models.BooleanField()
    repentino = models.BooleanField()
    resultado = models.BooleanField()
    
    # Método para convertirlo en String
    def __str__(self):
        return "Fiebre: " + str(self.fiebre) + ", Tos seca: " + str(self.tos_seca) + ", Asfixia: " + str(self.asfixia) + ", Perdida sentidos: " + str(self.perdida_sentidos) + ", Repentino: " + str(self.repentino) + ", Resultado: " + str(self.resultado)