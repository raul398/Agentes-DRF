'''from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view'''

from apps.base.api.views.tools import *

from apps.cpd.api.serializers.cpd_cuit_serializers import Cpd_CuitSerializers


'''
formate de la api data

{
    'Nro_esp': 91705, 
    'Cod_esp': 'PUY23', 
    'Nom_tipo': 'PUBLICOS', 
    'Cod_plazo': 48, 
    'Fecha': datetime.date(2018, 6, 14), 
    'Precio_por': Decimal('100.0000'), 
    'Aforo': Decimal('70.0000'), 
    'Cierre_anterior': Decimal('185.1290'), 
    'Precio_aforado': Decimal('138.0195'), 
    'is_active': True}
'''


@api_view(['POST'])
def cpd_cuit_import_file_api_view(request):

    def getValidateData(value, is_date=False):
        value = value.decode('utf-8').strip().replace(',', '.')
        if is_date:
            value = "%s-%s-01" %(value[:4], value[-2:])
        return value

    if request.method == 'POST':
        file = request.data['files']
        #file = open(data, 'r')
        fileinline = file.readlines()

        file.close()
        d = dict()
        lista = list()
        for line in fileinline:
            dic = dict()
            dic["cogidoDeEntidad"] = str(getValidateData(line[0:5]))
            dic["fechaDeInformacion"] = str(getValidateData(line[5:11], True))
            dic["tipoDeIdentificacion"] = str(getValidateData(line[11:13]))
            dic["nroDeIdentificacion"] = str(getValidateData(line[13:24]))
            dic["actividad"] = str(getValidateData(line[24:27]))
            dic["situacion"] = str(getValidateData(line[27:29]))
            dic["prestamosTotalDeGarantiasAfrontadas"] = float(getValidateData(line[29:41]))
            dic["participaciones"] = float(getValidateData(line[41:53]))
            dic["garantiasOtorgadas"] = float(getValidateData(line[53:65]))
            dic["otrosConceptos"] = float(getValidateData(line[65:77]))
            dic["garantiasPreferidasA"] = float(getValidateData(line[77:89]))
            dic["garantiasPreferidasB"] = float(getValidateData(line[89:101]))
            dic["sinGarantíasPreferidas"] = float(getValidateData(line[101:113]))
            dic["contragarantiasPreferidasA"] = float(getValidateData(line[113:125]))
            dic["contragarantiasPreferidasB"] = float(getValidateData(line[125:137]))
            dic["sinContragarantiasPreferidas"] = float(getValidateData(line[137:149]))
            dic["previsiones"] = float(getValidateData(line[149:161]))
            dic["deudaCubierta"] = int(getValidateData(line[161:162]))
            dic["procesoJudicialRevision"] = int(getValidateData(line[162:163]))
            dic["refinanciaciones"] = int(getValidateData(line[163:164]))
            dic["recategorizacionObligatoria"] = int(getValidateData(line[164:165]))
            dic["situaciónJuridica"] = int(getValidateData(line[165:166]))
            dic["irrecuperablesPorDisposicionTecnica"] = int(getValidateData(line[166:167]))
            dic["diasDeAtraso"] = int(getValidateData(line[167:171]))
            serializer = Cpd_CuitSerializers(data = dic)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Record successfully'}, status = status.HTTP_200_OK)