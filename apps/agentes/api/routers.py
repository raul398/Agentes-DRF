from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from apps.agentes.api.views.agente_view import AgenteViewSet

router = DefaultRouter()

router.register(r'Agentes', AgenteViewSet, basename='Agentes')

urlpatterns = router.urls