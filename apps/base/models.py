from django.db import models

#Clase base que contiene los campos que heredaran el resto de los modelos
class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    create_date = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'