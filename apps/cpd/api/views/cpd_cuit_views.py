from apps.base.api.views.general_api_view import GeneralViewSet, GeneralPagination
from apps.cpd.api.serializers.cpd_cuit_serializers import Cpd_CuitSerializers


# Clase general que da el rango de paginacion por request
class Cpd_CuitPagination(GeneralPagination):
    page_size = 3

class Cpd_CuitViewSet(GeneralViewSet):
    serializer_class = Cpd_CuitSerializers
    pagination_class = Cpd_CuitPagination