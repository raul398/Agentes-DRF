from datetime import date
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer



class GeneralExportViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    serializer_class = None
    renderer_classes = (XLSXRenderer,)
    filename = '%s_file_export.xlsx' %(date.today())

    def get_queryset(self, pk=None):
        # Se toma el modelo desde la clase Meta del serializador
        model = self.get_serializer().Meta.model
        queryset = model.objects.all()
        return queryset
