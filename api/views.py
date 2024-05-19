from django.db.models import F
from rest_framework import viewsets
from .serializer import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    #Metodo para insertar
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        password = data.get('usu_contrasenia')
        encrypted_password = encrypt_password(password)
        data['usu_contrasenia'] = encrypted_password
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for usuario in queryset:
            usuario.usu_contrasenia = decrypt_password(usuario.usu_contrasenia)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    #Metodo para dar de baja
    def destroy(self, request, *args, **kwargs):
            
            cedula = kwargs.get('pk')
            try:
                usuario = Usuario.objects.get(usu_cedula=cedula)
                usuario.usu_habilitado = 0
                usuario.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Usuario.DoesNotExist:
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    #Metodo para buscar por cedula
    def retrieve(self, request, *args, **kwargs):
        cedula = kwargs.get('pk')
        try:
            usuario = Usuario.objects.get(usu_cedula=cedula)
            usuario.usu_contrasenia = decrypt_password(usuario.usu_contrasenia)
            serializer = self.get_serializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    # Método para actualizar
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        cedula = kwargs.get('pk')  # Obtener la cédula del usuario de los parámetros de la URL
        try:
            # Buscar el usuario por su cédula
            instance = Usuario.objects.get(usu_cedula=cedula)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        password = data.get('usu_contrasenia')
        encrypted_password = encrypt_password(password)
        data['usu_contrasenia'] = encrypted_password
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

 
class LoginView(APIView):
    def post(self, request):
        usu_nombres = request.data.get('usu_nombres')
        usu_contrasenia_provided = request.data.get('usu_contrasenia')

        try:
            # Obtener el usuario de la base de datos
            usuario = Usuario.objects.get(usu_nombres=usu_nombres)
            
            # Desencriptar la contraseña almacenada en la base de datos
            usu_contrasenia_stored = decrypt_password(usuario.usu_contrasenia)

            # Verificar si la contraseña proporcionada coincide con la almacenada desencriptada
            if usu_contrasenia_stored == usu_contrasenia_provided:
                # Desencriptar la contraseña para devolverla en la respuesta
                usuario.usu_contrasenia = usu_contrasenia_stored
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)


def encrypt_password(password):
    # Algoritmo César para encriptar la contraseña
    encrypted_password = ''.join(chr((ord(char) + 3) % 256) for char in password)
    return encrypted_password

def decrypt_password(encrypted_password):
    # Algoritmo César para desencriptar la contraseña
    decrypted_password = ''.join(chr((ord(char) - 3) % 256) for char in encrypted_password)
    return decrypted_password


class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = LaboratorioSerializer
    
    #Metodo para buscar por cedula
    def retrieve(self, request, *args, **kwargs):
        nombre_laboratorio = kwargs.get('pk')
        try:
            laboratorio = Ubicacion.objects.get(ubi_nombre__iexact=nombre_laboratorio) 
            serializer = self.get_serializer(laboratorio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ubicacion.DoesNotExist:
            return Response({'error': 'Laboratorio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class BloqueViewSet(viewsets.ModelViewSet):
    queryset = Bloque.objects.annotate(fac_nombre=F('blo_fac__fac_nombre')).all()
    serializer_class = BloqueSerializer

class TipoUbicacionViewSet(viewsets.ModelViewSet):
    queryset = TipoUbicacion.objects.all()
    serializer_class = TipoUbicacionSerializer    

class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.annotate(tip_ubi_nombre=F('sof_tip_ubi__tip_ubi_nombre')).all()
    serializer_class = SoftwareSerializer