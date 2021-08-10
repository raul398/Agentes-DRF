from apps.base.api.views.general_api_view import GeneralViewSet, GeneralPagination
from apps.agentes.api.serializers.agente_serializers import AgenteSerializers, TestAgenteSerializers


# Clase general que da el rango de paginacion por request
class AgentePagination(GeneralPagination):
    page_size = 10

class AgenteViewSet(GeneralViewSet):
    serializer_test = TestAgenteSerializers
    serializer_class = AgenteSerializers
    pagination_class = AgentePagination
