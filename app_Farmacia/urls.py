from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Farmacia, name='inicio_Farmacia'),

    # CRUD PROVEEDOR
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/editar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/editar/<int:id>/guardar/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
]
