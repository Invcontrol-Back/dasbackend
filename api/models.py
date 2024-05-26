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
    usu_habilitado = models.IntegerField(blank=True, null=True)

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

    class Meta:
        managed = False
        db_table = 'software'

class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_nombre = models.CharField(max_length=30)
    ubi_blo = models.ForeignKey(Bloque, models.DO_NOTHING)
    ubi_tip_ubi = models.ForeignKey(TipoUbicacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ubicacion'

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
    inm_categoria = models.CharField(max_length=30)
    inm_dep = models.ForeignKey(Dependencia, models.DO_NOTHING, blank=True, null=True)
    inm_serie = models.CharField(max_length=30, blank=True, null=True)
    inm_modelo = models.CharField(max_length=30, blank=True, null=True)
    inm_marca = models.CharField(max_length=30, blank=True, null=True)
    inm_encargado = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    inm_anio_ingreso = models.TextField(blank=True, null=True)  # This field type is a guess.
    inm_eliminado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inmobiliario'





