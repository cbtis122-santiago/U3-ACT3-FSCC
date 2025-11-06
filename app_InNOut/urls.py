from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_in_n_out, name='inicio'),
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/ver/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursal/actualizar/<int:sucursal_id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursal/actualizar/realizar/<int:sucursal_id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursal/borrar/<int:sucursal_id>/', views.borrar_sucursal, name='borrar_sucursal'),
]