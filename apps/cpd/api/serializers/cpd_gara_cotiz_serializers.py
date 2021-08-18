from rest_framework import serializers
from apps.cpd.models import Cpd_Gara_Cotiz

'''
        Este serializador contine en Meta el modelo a serializar y los campos
    que se excluiran de la serializacion.
        Ademas, se redefine los metodos Create() y Update() para realizar el calculo corresoondiente
    para el valor de Precio_aforado.

        En create() se recibe el paremetro instance, que no es mas que un Json que hace referencia
    a la instancia del modelo que se intenta crear. De este Json se toman los valores necesarios
    para el calculo del valor para Precio_aforado. 
        Luego de esto se retorna self.model.objects.create(**instance) con la instancia a crear como paremetro. 
    NOTA: No me funcionó con 'self.model' por lo tanto, directamente llame al modelo.
        
        En update() se recibe dos parametros. El primero es instance que hace referencia a la instancia
    que se quiere modificar y data que hace referencia al Json enviado por metodo PUT.
        De este Json se tomaran los valores necesarios para el calculo de Precio_aforado. Luego de esto, 
    se hace un save() sobre la instancia --> instance.save() y se retorna la instancia --> return instance 

'''

class Cpd_Gara_CotizSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Cpd_Gara_Cotiz
        exclude = ('state', 'create_date', 'modified_date',)

    def create(self, instance):
        #precio_aforado: cierre_anterior * aforo / 100 / precio_por
        Cierre_anterior = float(instance['Cierre_anterior'])
        Aforo = float(instance['Aforo'])
        Precio_por = float(instance['Precio_por'])

        instance['Precio_aforado'] = float(Cierre_anterior * Aforo / 100 / Precio_por)
        return Cpd_Gara_Cotiz.objects.create(**instance)

    def update(self, instance, data):
        #precio_aforado: cierre_anterior * aforo / 100 / precio_por
        Cierre_anterior = float(data.get('Cierre_anterior', instance.Cierre_anterior))
        Aforo = float(data.get('Aforo', instance.Aforo))
        Precio_por = float(data.get('Precio_por', instance.Precio_por))

        #instance.Precio_aforado = float(Cierre_anterior * Aforo / 100 / Precio_por)
        #instance.save()
        instance.Nro_esp = data.get('Nro_esp')
        instance.Cod_esp = data.get('Cod_esp')
        instance.Nom_tipo = data.get('Nom_tipo')
        instance.Cod_plazo = data.get('Cod_plazo')
        instance.Fecha = data.get('Fecha')
        instance.Precio_por = data.get('Precio_por')
        instance.Aforo = data.get('Aforo')
        instance.Cierre_anterior = data.get('Cierre_anterior')
        instance.Precio_aforado = data.get('Precio_aforado')
        instance.is_active = data.get('is_active')
        instance.Precio_aforado = float(Cierre_anterior * Aforo / 100 / Precio_por)
        instance.save()
        return instance