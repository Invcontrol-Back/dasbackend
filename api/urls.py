from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'facultad',views.FacultadViewSet)
router.register(r'bloque',views.BloqueViewSet)
router.register(r'tipoUbi',views.TipoUbicacionViewSet)
router.register(r'software',views.SoftwareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
