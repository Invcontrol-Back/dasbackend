from django.urls import path, include
from rest_framework import routers
from api import views
from .views import LoginView

router = routers.DefaultRouter()
#router.register(r'login', views.LoginView.as_view(), basename='login')
router.register(r'usuario',views.UsuarioViewSet)
router.register(r'rol',views.RolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(), name='login'),
]
