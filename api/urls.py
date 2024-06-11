from django.urls import path, include
from rest_framework import routers
from api import views
from .views import *

router = routers.DefaultRouter()
#router.register(r'login', views.LoginView.as_view(), basename='login')
router.register(r'usuario',views.UsuarioViewSet)
router.register(r'rol',views.RolViewSet)
router.register(r'laboratorio',views.LaboratorioViewSet)
router.register(r'facultad',views.FacultadViewSet)
router.register(r'bloque',views.BloqueViewSet)
router.register(r'tipoUbi',views.TipoUbicacionViewSet)
router.register(r'software',views.SoftwareViewSet)
router.register(r'categoria',views.CategoriaViewSet)
router.register(r'detalleCategoria',views.DetalleCategoriaViewSet)
router.register(r'marca',views.MarcaViewSet)
router.register(r'dependencia',views.DependenciaViewSet)
router.register(r'componente',views.ComponenteViewSet)
router.register(r'Inmobiliario',views.InmobiliarioViewSet)
router.register(r'localizacion',views.LocalizacionViewSet)
router.register(r'tecnologico',views.TecnologicoViewSet)
router.register(r'detalletecnologico',views.DetalleTecnologicoViewSet)
router.register(r'reporte', ReporteDetalleView, basename='reporte')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(), name='login'),
    path('detalleC/',views.ComponenteDetalleView.as_view(), name='detalleC')
]
