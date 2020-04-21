from django.urls import path, include
from rest_framework import routers
from .views import HamburguesaViewSet, IngredienteViewSet


router = routers.DefaultRouter()
router.register('hamburguesa', HamburguesaViewSet, 'api_nps')
router.register('ingrediente', IngredienteViewSet, 'api_nps_response')

urlpatterns = [
    path('', include(router.urls)),
]



