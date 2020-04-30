from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from burgerapp import views

urlpatterns = [
    path('', ""),
    path('hamburguesa', views.index, name='index'),
    path('hamburguesa/<slug:pk>', views.hamburguesa_detail),
    path('ingrediente', views.ingrediente_list),
    path('ingrediente/<slug:pk>', views.ingrediente_detail),
    path('hamburguesa/<int:pk>/ingrediente/<int:pk2>', views.
         hamburguesa_ingrediente),
]

urlpatterns = format_suffix_patterns(urlpatterns)



