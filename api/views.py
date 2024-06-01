from django.db.models import F
from rest_framework import viewsets
from .serializer import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
from django.db import connection
from rest_framework.decorators import action

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        return Usuario.objects.filter(usu_eliminado="no")

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

    def destroy(self, request, *args, **kwargs):
        usu_id = kwargs.get('pk')
        try:
            usuario = Usuario.objects.get(usu_id=usu_id)
            usuario.usu_eliminado = "si"
            usuario.save()
            
            Inmobiliario.objects.filter(inm_encargado_id=usuario.usu_id).update(inm_encargado_id=None)
            Tecnologico.objects.filter(tec_encargado_id=usuario.usu_id).update(tec_encargado_id=None)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        usu_id = kwargs.get('pk')
        try:
            instance = Usuario.objects.get(usu_id=usu_id)
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

    @action(detail=False, methods=['get'])
    def buscar_por_cedula(self, request):
        cedula = request.query_params.get('cedula', None)
        if cedula is not None:
            queryset = self.get_queryset().filter(usu_cedula__icontains=cedula)
            for usuario in queryset:
                usuario.usu_contrasenia = decrypt_password(usuario.usu_contrasenia)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Debe proporcionar un valor para buscar por cédula'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'])
    def actualizar_bienes_generales(self, request):
        enc_anterior = request.data.get('encargado_anterior')
        enc_nuevo = request.data.get('encargado_nuevo')

        if not enc_anterior or not enc_nuevo:
            return Response({'error': 'Debe proporcionar ambos valores: encargado_anterior y encargado_nuevo'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tecnologico_actualizado = Tecnologico.objects.filter(tec_encargado=enc_anterior).update(tec_encargado=enc_nuevo)
            inmobiliario_actualizado = Inmobiliario.objects.filter(inm_encargado=enc_anterior).update(inm_encargado=enc_nuevo)

            return Response({
                'tecnologico_actualizado': tecnologico_actualizado,
                'inmobiliario_actualizado': inmobiliario_actualizado
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



 
class LoginView(APIView):
    def post(self, request):
        usu_correo = request.data.get('usu_correo')
        usu_contrasenia_provided = request.data.get('usu_contrasenia')

        try:
            # Obtener el usuario de la base de datos
            usuario = Usuario.objects.get(usu_correo=usu_correo)
            
            # Desencriptar la contraseña almacenada en la base de datos
            usu_contrasenia_stored = decrypt_password(usuario.usu_contrasenia)

            # Verificar si la contraseña proporcionada coincide con la almacenada desencriptada
            # verifica que este habilitado
            if usu_contrasenia_stored == usu_contrasenia_provided and usuario.usu_habilitado == 1:
                # Desencriptar la contraseña para devolverla en la respuesta
                usuario.usu_contrasenia = usu_contrasenia_stored
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:

                return Response({'error': 'Usuario o contraseña incorrectos '}, status=status.HTTP_401_UNAUTHORIZED)
        
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
    
    def perform_create(self, serializer):
        ubicacion = serializer.save(ubi_eliminado="no")
        for i in range(1, 31):
            nombre_localizacion = f"PC{i:02d}"
            Localizacion.objects.create(loc_nombre=nombre_localizacion, loc_ubi=ubicacion)
        return Response(serializer.data)

    def get_queryset(self):
        return Ubicacion.objects.filter(ubi_eliminado="no")

    def retrieve(self, request, *args, **kwargs):
        nombre_laboratorio = kwargs.get('pk')
        try:
            laboratorio = Ubicacion.objects.get(ubi_nombre__iexact=nombre_laboratorio) 
            serializer = self.get_serializer(laboratorio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ubicacion.DoesNotExist:
            return Response({'error': 'Laboratorio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            laboratorio = Ubicacion.objects.get(pk=pk)
            serializer = self.get_serializer(laboratorio, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ubicacion.DoesNotExist:
            return Response({'error': 'Laboratorio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            laboratorio = Ubicacion.objects.get(pk=pk)
            laboratorio.ubi_eliminado = "si"
            laboratorio.save()

            localizaciones = Localizacion.objects.filter(loc_ubi_id=laboratorio.ubi_id)
            localizaciones.update(loc_eliminado = "si")

            for localizacion in localizaciones:
                Tecnologico.objects.filter(tec_loc_id=localizacion.loc_id).update(tec_loc_id=None)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ubicacion.DoesNotExist:
            return Response({'error': 'Laboratorio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class BloqueViewSet(viewsets.ModelViewSet):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer

    def perform_create(self, serializer):
        serializer.save(blo_eliminado="no")

    def get_queryset(self):
        return Bloque.objects.filter(blo_eliminado="no")


    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            bloque = Bloque.objects.get(blo_id=id)
            bloque.blo_eliminado = "si"
            bloque.save()
            
            ubicaciones = Ubicacion.objects.filter(ubi_blo_id=bloque.blo_id)
            ubicaciones.update(ubi_eliminado="si")

            for ubicacion in ubicaciones:
                localizaciones = Localizacion.objects.filter(loc_ubi_id=ubicacion.ubi_id)
                localizaciones.update(loc_eliminado="si")
                for localizacion in localizaciones:
                    Tecnologico.objects.filter(tec_loc_id=localizacion.loc_id).update(tec_loc_id=None)
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Bloque.DoesNotExist:
            return Response({'error': 'Bloque no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class TipoUbicacionViewSet(viewsets.ModelViewSet):
    queryset = TipoUbicacion.objects.all()
    serializer_class = TipoUbicacionSerializer    

class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

    
    def get_queryset(self):
        return Software.objects.filter(sof_eliminado="no")


    def perform_create(self, serializer):
        serializer.save(sof_eliminado="no")

    def destroy(self, request, *args, **kwargs):
            
        id = kwargs.get('pk')
        try:
            software = Software.objects.get(sof_id=id)
            software.sof_eliminado = "si"
            software.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Software.DoesNotExist:
            return Response({'error': 'Software no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.filter(cat_eliminado="no")

class DetalleCategoriaViewSet(viewsets.ModelViewSet):
    queryset = DetalleCategoria.objects.all()
    serializer_class = DetalleCategoriaSerializer

    def get_queryset(self):
        return DetalleCategoria.objects.filter(det_cat_eliminado="no",det_cat_cat__cat_eliminado="no")
    
class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

    def get_queryset(self):
        return Componente.objects.filter(com_eliminado="no")
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc('eliminarComponente', [instance.com_id])
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class InmobiliarioViewSet(viewsets.ModelViewSet):
    queryset = Inmobiliario.objects.all()
    serializer_class = InmobiliarioSerializer

    def get_queryset(self):
        return Inmobiliario.objects.filter(inm_eliminado="no")

    def perform_create(self, serializer):
        serializer.save(inm_eliminado="no")

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            inmueble = Inmobiliario.objects.get(inm_id=id)
            inmueble.inm_eliminado = "si"
            inmueble.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Software.DoesNotExist:
            return Response({'error': 'Inmobiliario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    

class LocalizacionViewSet(viewsets.ModelViewSet):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

    def get_queryset(self):
        return Localizacion.objects.filter(loc_eliminado="no")
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            localizacion = Localizacion.objects.get(loc_id=id)
            localizacion.loc_eliminado = "si"
            localizacion.save()
            
            Tecnologico.objects.filter(tec_loc_id=localizacion.loc_id).update(tec_loc_id=None)
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Bloque.DoesNotExist:
            return Response({'error': 'Bloque no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class TecnologicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnologico.objects.annotate(usu_nombres=F('tec_encargado__usu_nombres'),cat_nombre=F('tec_cat__cat_nombre'),dep_nombre=F('tec_dep__dep_nombre'),loc_nombre=F('tec_loc__loc_nombre')).all()
    serializer_class = TecnologicoSerializer

    def get_queryset(self):
        return Tecnologico.objects.filter(tec_eliminado="no")
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            with connection.cursor() as cursor:
                cursor.callproc('eliminarTecnologico', [instance.tec_id])
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            tecnologico_anterior = Tecnologico.objects.get(tec_id=id, tec_eliminado="no")
            nueva_etiqueta = request.data.get('tec_loc')

            id_categoria = request.data.get('tec_cat')
            categoria = Categoria.objects.get(cat_id=id_categoria)

            id_dependencia = request.data.get('tec_dep')
            dependencia = Dependencia.objects.get(dep_id=id_dependencia)

            id_usuario = request.data.get('tec_encargado')
            usuario = Usuario.objects.get(usu_id=id_usuario)

            Tecnologico.objects.filter(tec_loc=nueva_etiqueta).update(tec_loc=None)
            tecnologico_anterior.tec_loc_id = nueva_etiqueta
            tecnologico_anterior.tec_anio_ingreso = request.data.get('tec_anio_ingreso')
            tecnologico_anterior.tec_cat = categoria
            tecnologico_anterior.tec_codigo = request.data.get('tec_codigo')
            tecnologico_anterior.tec_dep = dependencia
            tecnologico_anterior.tec_encargado = usuario
            tecnologico_anterior.tec_ip = request.data.get('tec_ip')
            tecnologico_anterior.tec_marca = request.data.get('tec_marca')
            tecnologico_anterior.tec_modelo = request.data.get('tec_modelo')
            tecnologico_anterior.tec_serie = request.data.get('tec_serie')
            

            tecnologico_anterior.save()
            serializer = self.get_serializer(tecnologico_anterior)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tecnologico.DoesNotExist:
            return Response({'error': 'Tecnologico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
class DetalleTecnologicoViewSet(viewsets.ModelViewSet):
    queryset = DetalleTecnologico.objects.all()
    serializer_class = DetalleTecnologicoSerializer


class ComponenteDetalleView(APIView):
    def get(self, request):
        parametro = self.request.query_params.get('parametro', None)
        
        if parametro is not None:
            with connection.cursor() as cursor:
                cursor.execute("CALL obtenerComponentesTecnologicos(%s)", [parametro])
                columns = [col[0] for col in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return Response(results)
        else:
            return Response({"error": "Parámetro 'parametro' no proporcionado."})