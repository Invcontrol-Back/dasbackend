from rest_framework import serializers
from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'  

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'  

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__' 

class BloqueSerializer(serializers.ModelSerializer):
    fac_nombre = serializers.CharField(source='blo_fac.fac_nombre', read_only=True)
    class Meta:
        model = Bloque
        fields = ['blo_id', 'blo_nombre', 'blo_fac', 'fac_nombre']
    
class TipoUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUbicacion
        fields = '__all__'

class SoftwareSerializer(serializers.ModelSerializer):
    tip_ubi_nombre = serializers.CharField(source='sof_tip_ubi.tip_ubi_nombre', read_only=True)
    class Meta:
        model = Software
        fields = ['sof_id','sof_nombre','sof_version','sof_tipo','sof_duracion','sof_descripcion','sof_tip_ubi','tip_ubi_nombre']


