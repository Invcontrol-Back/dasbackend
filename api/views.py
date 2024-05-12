from rest_framework import viewsets
from .serializer import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Usuario
from rest_framework.response import Response
from rest_framework import status

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

 
 
class LoginView(APIView):
    def post(self, request):
        usu_nombres = request.data.get('usu_nombres')
        usu_contrasenia = request.data.get('usu_contrasenia')

        try:
            usuario = Usuario.objects.get(usu_nombres=usu_nombres, usu_contrasenia=usu_contrasenia)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)