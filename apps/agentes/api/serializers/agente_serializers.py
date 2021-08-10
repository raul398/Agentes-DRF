from rest_framework import serializers
from apps.base.api.validations.set_validations import Verify_Cuit
from apps.agentes.models import Agente



class AgenteSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Agente
        exclude = ('state', 'create_date', 'modified_date',)

class TestAgenteSerializers(serializers.Serializer):

    cuit = serializers.CharField(max_length=13)

    def validate_cuit(self, value):
        Result = Verify_Cuit(value)
        if not Result:
            raise serializers.ValidationError('Error, el CUIT ingresado es incorrecto')
        return value

    def validate(self, data):
        return data