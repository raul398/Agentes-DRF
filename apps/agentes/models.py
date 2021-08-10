from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel 

# Create your models here.
class Agente(BaseModel):
    cod_op = models.IntegerField('Codigo de Operador', unique = True, blank=False)
    razon = models.CharField('Razon Social', max_length=250, blank=False, null=True)
    cuit = models.CharField('CUIT',max_length=13, blank=True, null=True)
    cat_iva = models.IntegerField('Categoria IVA',blank=True, null=True)
    domicilio = models.CharField('Domicilio',max_length=100, blank=True, null=True)
    telefono = models.CharField('Teléfono',max_length=100, blank=True, null=True)
    email_dif_pub = models.CharField('Email de Difusión Pública', max_length=100, blank=True, null=True)
    email_institucional = models.CharField('Email Institucional', max_length=100, blank=True, null=True)
    sitioweb = models.URLField('Sitio WEB',max_length=100, blank=True, null=True)
    provincia = models.CharField('Provincia',max_length=90, blank=True, null=True)
    localidad = models.CharField('Localidad', max_length=90, blank=True, null=True)
    cnv_categ = models.CharField('Categoria de Agente', max_length=5, blank=True, null=True)
    cod_caja_cpd = models.IntegerField('Codigo de CPD CVSA', blank=True, null=True)
    fec_ing_acc = models.DateField('Fecha Ingreso Accionista', blank=True, null=True)
    fec_creacion = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"
        ordering = ['cod_op']

    def __str__(self):
        return f'{self.cod_op} {self.razon}'