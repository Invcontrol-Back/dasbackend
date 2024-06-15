from rest_framework import serializers
from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    rol_nombre = serializers.CharField(source='usu_rol.rol_nombre',read_only=True)
    class Meta:
        model = Usuario
        fields = ['usu_id','usu_correo','usu_contrasenia','usu_cedula','usu_nombres','usu_apellidos','usu_rol','usu_habilitado','usu_eliminado','rol_nombre']  

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
    cat_nombre = serializers.CharField(source='det_cat_cat.cat_nombre',read_only=True)
    class Meta:
        model = DetalleCategoria
        fields = ['det_cat_id','det_cat_nombre','det_cat_eliminado','det_cat_cat','cat_nombre']
        
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    dep_nombre = serializers.CharField(source='com_dep.dep_nombre',read_only=True)
    det_cat_nombre = serializers.CharField(source='com_det_cat.det_cat_nombre',read_only=True)
    mar_nombre = serializers.CharField(source='com_mar.mar_nombre',read_only=True)
    class Meta:
        model = Componente
        fields = ['com_id','com_serie','com_codigo_bien','com_codigo_uta','com_modelo','com_caracteristica','com_anio_ingreso','com_estado','com_mar','com_eliminado','com_det_cat','com_dep','dep_nombre','det_cat_nombre','mar_nombre']

class InmobiliarioSerializer(serializers.ModelSerializer):
    usu_nombres = serializers.CharField(source='inm_encargado.usu_nombres',read_only=True)
    usu_apellidos = serializers.CharField(source='inm_encargado.usu_apellidos',read_only=True)
    cat_nombre = serializers.CharField(source='inm_cat.cat_nombre',read_only=True)
    dep_nombre = serializers.CharField(source='inm_dep.dep_nombre',read_only=True)
    mar_nombre = serializers.CharField(source='inm_mar.mar_nombre',read_only=True)
    loc_nombre = serializers.CharField(source='inm_loc.loc_nombre',read_only=True)
    ubi_nombre = serializers.CharField(source='inm_loc.loc_ubi.ubi_nombre',read_only=True)
    blo_nombre = serializers.CharField(source='inm_loc.loc_ubi.ubi_blo.blo_nombre',read_only=True)

    class Meta:
        model = Inmobiliario
        fields = ['inm_id','inm_codigo','inm_cat','inm_dep','inm_serie','inm_modelo','inm_mar','inm_loc','inm_descripcion','inm_encargado','inm_anio_ingreso','usu_nombres','usu_apellidos','cat_nombre','dep_nombre','mar_nombre','loc_nombre','ubi_nombre','blo_nombre']


class TecnologicoSerializer(serializers.ModelSerializer):
    usu_nombres = serializers.CharField(source='tec_encargado.usu_nombres', read_only=True)
    usu_apellidos = serializers.CharField(source='tec_encargado.usu_apellidos', read_only=True)
    cat_nombre = serializers.CharField(source='tec_cat.cat_nombre', read_only=True)
    dep_nombre = serializers.CharField(source='tec_dep.dep_nombre', read_only=True)
    loc_nombre = serializers.CharField(source='tec_loc.loc_nombre', read_only=True)
    ubi_nombre = serializers.CharField(source='tec_loc.loc_ubi.ubi_nombre', read_only=True)
    blo_nombre = serializers.CharField(source='tec_loc.loc_ubi.ubi_blo.blo_nombre', read_only=True)
    mar_nombre = serializers.CharField(source='tec_mar.mar_nombre',read_only=True)
    class Meta:
        model = Tecnologico
        fields = ['tec_id','tec_codigo','tec_serie','tec_modelo','tec_mar','tec_ip','tec_anio_ingreso','tec_descripcion','tec_encargado','tec_loc','tec_cat','tec_dep','tec_eliminado','usu_nombres','usu_apellidos','cat_nombre','dep_nombre','loc_nombre','mar_nombre','ubi_nombre','blo_nombre']

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

                          
