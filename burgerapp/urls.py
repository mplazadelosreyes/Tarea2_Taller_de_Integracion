from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from burgerapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hamburguesa', views.hamburguesa_list),
    path('hamburguesa/<str:pk>', views.hamburguesa_detail),
    path('ingrediente', views.ingrediente_list),
    path('ingrediente/<str:pk>', views.ingrediente_detail),
    path('hamburguesa/<str:pk>/ingrediente/<str:pk2>', views.
         hamburguesa_ingrediente),
]

urlpatterns = format_suffix_patterns(urlpatterns)



