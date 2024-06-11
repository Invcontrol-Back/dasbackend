from django.db import models

# Create your models here.

class Rol(models.Model):
    rol_id  = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'  

class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_correo = models.CharField(max_length=30)
    usu_contrasenia = models.CharField(max_length=300)
    usu_cedula = models.CharField(max_length=10)
    usu_nombres = models.CharField(max_length=30)
    usu_apellidos = models.CharField(max_length=30)
    usu_rol = models.ForeignKey(Rol, models.DO_NOTHING)
    usu_habilitado = models.CharField(max_length=30)
    usu_eliminado = models.CharField(max_length=30,default="no")

    class Meta:
        managed = False
        db_table = 'usuario'

class Dependencia(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_nombre = models.CharField(max_length=30, blank=True, null=True)
    dep_descripcion = models.CharField(max_length=30, blank=True, null=True)
    dep_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'dependencia'

class Facultad(models.Model):
    fac_id  = models.AutoField(primary_key=True)
    fac_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'facultad' 

class Bloque(models.Model):
    blo_id  = models.AutoField(primary_key=True)
    blo_nombre = models.CharField(max_length=30)
    blo_fac = models.ForeignKey('Facultad', on_delete=models.CASCADE, blank=True, null=True)
    blo_eliminado = models.CharField(max_length=20)
    
    class Meta:
        managed = False
        db_table = 'bloque'

class TipoUbicacion(models.Model):
    tip_ubi_id = models.AutoField(primary_key=True)
    tip_ubi_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_ubicacion'

class Software(models.Model):
    sof_id = models.AutoField(primary_key=True)
    sof_nombre = models.CharField(max_length=30)
    sof_version = models.CharField(max_length=30)
    sof_tipo = models.CharField(max_length=30)
    sof_duracion = models.CharField(max_length=30)
    sof_descripcion = models.CharField(max_length=200)
    sof_tip_ubi = models.ForeignKey('TipoUbicacion', models.DO_NOTHING)
    sof_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'software'

class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_nombre = models.CharField(max_length=30)
    ubi_blo = models.ForeignKey(Bloque, models.DO_NOTHING)
    ubi_tip_ubi = models.ForeignKey(TipoUbicacion, models.DO_NOTHING)
    ubi_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ubicacion'

class Localizacion(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_nombre = models.CharField(max_length=30)
    loc_ubi = models.ForeignKey('Ubicacion', models.DO_NOTHING)
    loc_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'localizacion'


class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=30)
    cat_tipoBien = models.CharField(max_length=30)
    cat_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'categoria'

class DetalleCategoria(models.Model):
    det_cat_id = models.AutoField(primary_key=True)
    det_cat_nombre = models.CharField(max_length=30)
    det_cat_cat = models.ForeignKey(Categoria,models.DO_NOTHING)
    det_cat_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'categoriadetalle'

class Marca(models.Model):
    mar_id = models.AutoField(primary_key=True)
    mar_nombre = models.CharField(max_length=30)
    mar_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'marca'

class Componente(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_serie = models.CharField(max_length=30)
    com_codigo_bien = models.CharField(max_length=30, default=None, null=True, blank=True)
    com_codigo_uta = models.CharField(max_length=30,default=None,null=True,blank=True)
    com_det_cat = models.ForeignKey('DetalleCategoria', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    com_modelo = models.CharField(max_length=30)
    com_marca = models.CharField(max_length=30)
    com_caracteristica = models.CharField(max_length=30)
    com_dep = models.ForeignKey('Dependencia', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    com_anio_ingreso = models.CharField(max_length=30)
    com_eliminado = models.CharField(max_length=30,default="no")

    class Meta:
        managed = False
        db_table = 'componente'

class Inmobiliario(models.Model):
    inm_id = models.AutoField(primary_key=True)
    inm_codigo = models.CharField(unique=True, max_length=30)
    inm_cat = models.ForeignKey(Categoria,models.DO_NOTHING, blank=True, null=True)
    inm_dep = models.ForeignKey(Dependencia, models.DO_NOTHING, blank=True, null=True)
    inm_serie = models.CharField(max_length=30, blank=True, null=True)
    inm_modelo = models.CharField(max_length=30, blank=True, null=True)
    inm_marca = models.CharField(max_length=30, blank=True, null=True)
    inm_encargado = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    inm_anio_ingreso = models.CharField(max_length=30,blank=True, null=True)
    inm_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inmobiliario'

class Localizacion(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_nombre = models.CharField(max_length=30)
    loc_ubi = models.ForeignKey('Ubicacion', on_delete=models.DO_NOTHING)
    loc_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'localizacion'

class Tecnologico(models.Model):
    tec_id = models.AutoField(primary_key=True)
    tec_codigo = models.CharField(max_length=30)
    tec_serie = models.CharField(max_length=30)
    tec_modelo = models.CharField(max_length=30)
    tec_marca = models.CharField(max_length=30)
    tec_ip = models.CharField(max_length=30, blank=True, null=True, default=None)
    tec_anio_ingreso = models.CharField(max_length=30)
    tec_encargado = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    tec_loc = models.ForeignKey('Localizacion', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    tec_cat = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    tec_dep = models.ForeignKey('Dependencia', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    tec_eliminado = models.CharField(max_length=20,default="no")

    class Meta:
        managed = False
        db_table = 'tecnologico'

class DetalleTecnologico(models.Model):
    det_tec_id = models.AutoField(primary_key=True)
    det_tec_tec = models.ForeignKey('Tecnologico', on_delete=models.DO_NOTHING)
    det_tec_com_adquirido = models.ForeignKey('Componente', on_delete=models.DO_NOTHING, related_name='adquirido', null=True, blank=True, default=None)
    det_tec_com_uso = models.ForeignKey('Componente', on_delete=models.DO_NOTHING, related_name='uso', null=True, blank=True, default=None)
    det_tec_descripcion_repotencia = models.CharField(max_length=30, null=True, blank=True, default=None)
    det_tec_estado_repotencia = models.CharField(max_length=30, default=0)
    det_tec_eliminado = models.CharField(max_length=20, default="no")

    class Meta:
        managed = False
        db_table = 'detalle_tecnologico'