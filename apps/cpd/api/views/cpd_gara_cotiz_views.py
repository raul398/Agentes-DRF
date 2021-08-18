from apps.base.api.views.general_api_view import GeneralViewSet, GeneralPagination
from apps.base.api.views.export_file_xlsx import GeneralExportViewSet
from apps.cpd.api.serializers.cpd_gara_cotiz_serializers import Cpd_Gara_CotizSerializers

'''
class Cpd_Gara_CotizListCreateAPIView(GeneralListCeateAPIView):
    #indicamos el serielizador al cual va a tomar la referencia
    serializer_class = Cpd_Gara_CotizSerializers

class Cpd_Gara_CotizRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = Cpd_Gara_CotizSerializers

'''

# Clase general que da el rango de paginacion por request
class Cpd_Gara_CotizPagination(GeneralPagination):
    page_size = 3

class Cpd_Gara_CotizViewSet(GeneralViewSet):
    serializer_class = Cpd_Gara_CotizSerializers
    pagination_class = Cpd_Gara_CotizPagination

class Cpd_Gara_Cotiz_Export_xlsx(GeneralExportViewSet):
    serializer_class = Cpd_Gara_CotizSerializers