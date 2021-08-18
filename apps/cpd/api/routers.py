from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.cpd.api.views.cpd_gara_cotiz_views import Cpd_Gara_CotizViewSet, Cpd_Gara_Cotiz_Export_xlsx
from apps.cpd.api.views.cpd_cuit_import_file_view import cpd_cuit_import_file_api_view
from apps.cpd.api.views.cpd_cuit_views import Cpd_CuitViewSet


url = [
    path('cpd_ciut_import_file/', cpd_cuit_import_file_api_view, name='cpd_ciut_import_file'),
]

router = DefaultRouter()

router.register(r'cpd_gara_cotiz', Cpd_Gara_CotizViewSet, basename = 'cpd_gara_cotiz')
router.register(r'cpd_gara_cotiz_export_xlsx', Cpd_Gara_Cotiz_Export_xlsx, basename = 'cpd_gara_cotiz_export_xlsx')
router.register(r'cpd_cuit', Cpd_CuitViewSet, basename = 'cpd_cuit')

urlpatterns = router.urls + url


