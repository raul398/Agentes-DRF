from rest_framework import serializers
from apps.cpd.models import Cpd_Cuit


class Cpd_CuitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cpd_Cuit
        exclude = ('state', 'create_date', 'modified_date',)