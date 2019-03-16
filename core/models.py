

from django.db import models


# Create your models here.
class Usuarios(models.Model):
    
    PrimerApellido =models.CharField(max_length=35)
    SegundoApellido =models.CharField(max_length=35)
    Nombres =models.CharField(max_length=35)
    FechaNacimiento =models.DataField()
    Sexos =(('F')('Femenino')('M')('Masculino'))
    Sexo=models.CharField(max_length=1, choices='sexos', defaul='M')
     
    def nombreCompleto(self):
        cadena ="{0}, {1}, {2}"
        return cadena.format(self.PrimerApellido, self.SegundoApellido, self.Nombres)
    
    def __str__(self):
        return self.nombreCompleto()

    class Noticia(models.Model):
        Titulo = models.charField(max_length=20)
        Direccion = models.charField(max_length=35)
        Especificacion = models.charField(max_length=35)
        FechadeInicio = models.DateTimeField(auto_now_add=False)

    class IngresaInfo(models.Model):
            Usuarios = models.ForeiKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
            Noticia = models.ForeiKey(Noticia, null=False, blank=False, on_delete=models.CASCADE)
            FechaInfoEvento = models.DateTimeField(auto_now_add=True)

        


