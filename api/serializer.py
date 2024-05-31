from rest_framework import serializers
from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usu_id','usu_correo','usu_contrasenia','usu_cedula','usu_nombres','usu_apellidos','usu_rol']  

class LaboratorioSerializer(serializers.ModelSerializer):
    blo_nombre = serializers.CharField(source='ubi_blo.blo_nombre', read_only=True)
    tip_ubi_nombre = serializers.CharField(source='ubi_tip_ubi.tip_ubi_nombre', read_only=True)
    class Meta:
        model = Ubicacion
        fields = ['ubi_id','ubi_nombre','ubi_blo','blo_nombre','ubi_tip_ubi','tip_ubi_nombre'] 


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

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class DetalleCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCategoria
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    dep_nombre = serializers.CharField(source='com_dep.dep_nombre',read_only=True)
    det_cat_nombre = serializers.CharField(source='com_det_cat.det_cat_nombre',read_only=True)
    class Meta:
        model = Componente
        fields = ['com_id','com_serie','com_codigo_bien','com_codigo_uta','com_modelo','com_marca','com_caracteristica','com_anio_ingreso','com_eliminado','com_det_cat','com_dep','dep_nombre','det_cat_nombre']

class InmobiliarioSerializer(serializers.ModelSerializer):
    usu_nombres = serializers.CharField(source='inm_encargado.usu_nombres',read_only=True)
    cat_nombre = serializers.CharField(source='inm_cat.cat_nombre',read_only=True)
    dep_nombre = serializers.CharField(source='inm_dep.dep_nombre',read_only=True)

    class Meta:
        model = Inmobiliario
        fields = ['inm_id','inm_codigo','inm_cat','inm_dep','inm_serie','inm_modelo','inm_marca','inm_encargado','inm_anio_ingreso','usu_nombres','cat_nombre','dep_nombre']


class TecnologicoSerializer(serializers.ModelSerializer):
    usu_nombres = serializers.CharField(source='tec_encargado.usu_nombres', read_only=True)
    cat_nombre = serializers.CharField(source='tec_cat.cat_nombre', read_only=True)
    dep_nombre = serializers.CharField(source='tec_dep.dep_nombre', read_only=True)
    loc_nombre = serializers.CharField(source='tec_loc.loc_nombre', read_only=True)
    class Meta:
        model = Tecnologico
        fields = ['tec_id','tec_codigo','tec_serie','tec_modelo','tec_marca','tec_ip','tec_anio_ingreso','tec_encargado','tec_loc','tec_cat','tec_dep','tec_eliminado','usu_nombres','cat_nombre','dep_nombre','loc_nombre']

class DetalleTecnologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleTecnologico
        fields = '__all__'

class LocalizacionSerializer(serializers.ModelSerializer):
    ubi_nombre = serializers.CharField(source='loc_ubi.ubi_nombre',read_only=True)
    blo_nombre = serializers.CharField(source='loc_ubi.ubi_blo.blo_nombre',read_only=True)
    tec_codigo = serializers.SerializerMethodField()

    class Meta:
        model = Localizacion
        fields = ['loc_id','loc_nombre','loc_ubi','ubi_nombre','blo_nombre','tec_codigo']

    def get_tec_codigo(self, obj):
        tecnologicos = Tecnologico.objects.filter(tec_loc=obj)
        return [tecnologico.tec_codigo for tecnologico in tecnologicos]

                          
