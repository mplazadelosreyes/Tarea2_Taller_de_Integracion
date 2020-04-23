from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from burgerapp import views

urlpatterns = [
    path('hamburguesa/', views.hamburguesa_list),
    path('hamburguesa/<int:pk>', views.hamburguesa_detail),
    path('ingrediente/', views.ingrediente_list),
    path('ingrediente/<int:pk>', views.ingrediente_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)



