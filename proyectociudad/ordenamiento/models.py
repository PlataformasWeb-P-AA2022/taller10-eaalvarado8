from django.db import models

# Create your models here.

class Parroquia(models.Model):
    opciones_tipo_parroquia = (
        ('urbana', 'URBANA'),
        ('rural', 'RURAL'),
        )

    nombre = models.CharField(max_length=50)
    tipo_parroquia = models.CharField(max_length=30, \
            choices=opciones_tipo_parroquia) 
    
    def __str__(self):
        return "Parroquia: %s Tipo: %s" % (self.nombre, 
                self.tipo_parroquia,
        )

class Barrio(models.Model):
    opciones_numero_parques = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    nombre = models.CharField(max_length=50)
    num_viviendas = models.IntegerField("número de viviendas")
    num_parques = models.IntegerField("número de parques", \
        choices=opciones_numero_parques)
    num_edificios = models.IntegerField("número de edificios")
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
            related_name="losbarrios")
    
    def __str__(self):
        return "Barrio: %s | Viviendas: %d | Parques: %d | Edificios: %d | %s" % (self.nombre, 
                self.num_viviendas,
                self.num_parques,
                self.num_edificios,
                self.parroquia
        )
