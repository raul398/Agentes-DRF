'''from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination'''

from apps.base.api.views.tools import *

from apps.base.api.validations.authentication_mixins import Authentication
#from rest_framework.decorators import api_view

class GeneralPagination(PageNumberPagination):
    page_size = None

# Esta es la view general que identifica el metodo utilizado 
# permite realizar las diferentes acciones.
# Ademas hereda de Authentication para la validacion del token.
class GeneralViewSet(Authentication, viewsets.ModelViewSet):
    # Se ingresa si se requiere un serializer de verifcacion
    serializer_test = None
    # Cantidad de registros por request
    pagination_class = None
    # Este es el atributo que se va a pasar en cada llamada a esta clase
    serializer_class = None

    def get_queryset(self, pk=None):
        # Se toma el modelo desde la clase Meta del serializador
        model = self.get_serializer().Meta.model
        # Se hace la consulta en base a model para que sea generico y se retorna
        if pk:
            return model.objects.filter(id = pk).first()
        return model.objects.all()

    '''
    def list(self, request):
        model_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(model_serializer.data, status = status.HTTP_200_OK)

    NOTA: si se redefine list(), rest_framework.pagination no podra hacer la paginacion de la api

    '''

    def create(self, request):
        if self.serializer_test:
            tes_data = self.serializer_test(data= request.data)
            if not tes_data.is_valid():
                return Response(tes_data.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Record created successfully'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error' : 'Record not found'}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_queryset(pk)
        if instance:
            instance.state = False
            instance.save()
            return Response({'message' : 'Record deleted successfully'}, status = status.HTTP_200_OK)
        return Response({'error' : 'Record not found'}, status = status.HTTP_400_BAD_REQUEST)