from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.VehiculosView.as_view(), name='lista_vehiculos'),
    path('add/', views.VehiculoCreateView.as_view(), name='add_vehiculos'),
]
