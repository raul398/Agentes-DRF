from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel 


class Cpd_Cuit(BaseModel):
    cogidoDeEntidad = models.CharField('cogidoDeEntidad', max_length=5)
    fechaDeInformacion = models.DateField('fechaDeInformacion', max_length=6, default='1970/01/01')
    tipoDeIdentificacion = models.CharField('tipoDeIdentificacion', max_length=2)
    nroDeIdentificacion = models.CharField('nroDeIdentificacion', max_length=11)
    actividad = models.CharField('actividad', max_length=3)
    situacion = models.CharField('situacion', max_length=2)
    prestamosTotalDeGarantiasAfrontadas = models.DecimalField('prestamosTotalDeGarantiasAfrontadas', max_digits=11, decimal_places=2)
    participaciones = models.DecimalField('participaciones', max_digits=11, decimal_places=2)
    garantiasOtorgadas = models.DecimalField('garantiasOtorgadas', max_digits=11, decimal_places=2)
    otrosConceptos = models.DecimalField('otrosConceptos', max_digits=11, decimal_places=2)
    garantiasPreferidasA = models.DecimalField('garantiasPreferidasA', max_digits=11, decimal_places=2)
    garantiasPreferidasB = models.DecimalField('garantiasPreferidasB', max_digits=11, decimal_places=2)
    sinGarantíasPreferidas = models.DecimalField('sinGarantíasPreferidas', max_digits=11, decimal_places=2)
    contragarantiasPreferidasA = models.DecimalField('contragarantiasPreferidasA', max_digits=11, decimal_places=2)
    contragarantiasPreferidasB = models.DecimalField('contragarantiasPreferidasB', max_digits=11, decimal_places=2)
    sinContragarantiasPreferidas = models.DecimalField('sinContragarantiasPreferidas', max_digits=11, decimal_places=2)
    previsiones = models.DecimalField('previsiones', max_digits=11, decimal_places=2)
    deudaCubierta = models.IntegerField('deudaCubierta')
    procesoJudicialRevision = models.IntegerField('procesoJudicialRevision')
    refinanciaciones = models.IntegerField('refinanciaciones')
    recategorizacionObligatoria = models.IntegerField('recategorizacionObligatoria')
    situaciónJuridica = models.IntegerField('situaciónJuridica')
    irrecuperablesPorDisposicionTecnica = models.IntegerField('irrecuperablesPorDisposicionTecnica')
    diasDeAtraso = models.IntegerField('diasDeAtraso')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Cpd_Cuit'
        verbose_name_plural = 'Cpd_Cuit_Group'

    def __str__(self):
        return f'{self.cogidoDeEntidad}'


class Cpd_Gara_Cotiz(BaseModel):
    Nro_esp = models.PositiveIntegerField('Nro_esp') # Numero identificatorio de la especie
    Cod_esp = models.CharField('Cod_esp', max_length = 255, unique=True) # Nombre de la especie
    Nom_tipo = models.CharField('Nom_tipo', max_length = 255) #  Tipo de la especie
    Cod_plazo = models.PositiveIntegerField('Cod_plazo') # Plazo de negociación.
    Fecha = models.DateField('Fecha', blank = True, null = True) # Ultima fecha de cotización del titulo.
    Precio_por = models.DecimalField('Precio_por', max_digits=10, decimal_places=4)
    Aforo = models.DecimalField('Aforo', max_digits=10, decimal_places=4)
    Cierre_anterior = models.DecimalField('Cierre_anterior', max_digits=10, decimal_places=4)
    Precio_aforado = models.DecimalField('Precio_aforado', max_digits=10, decimal_places=4, blank = True, null = True)
    is_active = models.BooleanField('is_active', default = True, blank = True, null = True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Cpd_Gara_Cotiz'
        verbose_name_plural = 'Cpd_Gara_Cotiz_Group'

    def __str__(self):
        return f'{self.Nro_esp} {self.Nom_tipo}'