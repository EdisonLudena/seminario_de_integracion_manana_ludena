from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, VehiculoViewSet
from .calculate_view import calcular_area_triangulo, promedio_ventas

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet, basename="marcas")
router.register(r"vehiculos", VehiculoViewSet, basename="vehiculos")

urlpatterns = [
    path('triangle/area', calcular_area_triangulo, name='triangule-area'),
    path('products/promedio-ventas', promedio_ventas, name='promedio-ventas')
]
urlpatterns += router.urls