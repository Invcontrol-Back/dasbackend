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


class TipoUbicacion(models.Model):
    tip_ubi_id = models.AutoField(primary_key=True)
    tip_ubi_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_ubicacion'

class Bloque(models.Model):
    blo_id = models.AutoField(primary_key=True)
    blo_nombre = models.CharField(max_length=30)
    blo_fac = models.ForeignKey('Facultad', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloque'

class Facultad(models.Model):
    fac_id = models.AutoField(primary_key=True)
    fac_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'facultad'


class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_nombre = models.CharField(max_length=30)
    ubi_blo = models.ForeignKey(Bloque, models.DO_NOTHING)
    ubi_tip_ubi = models.ForeignKey(TipoUbicacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ubicacion'



























class Dependencia(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_nombre = models.CharField(max_length=30, blank=True, null=True)
    dep_descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencia'




class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=30)
    cat_tipobien = models.CharField(db_column='cat_tipoBien', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'




class Categoriadetalle(models.Model):
    det_cat_id = models.AutoField(primary_key=True)
    det_cat_nombre = models.CharField(max_length=30)
    det_cat_cat = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriadetalle'





class Componente(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_serie = models.CharField(max_length=30)
    com_codigo_bien = models.CharField(max_length=30, blank=True, null=True)
    com_codigo_uta = models.CharField(max_length=255)
    com_det_cat = models.ForeignKey(Categoriadetalle, models.DO_NOTHING)
    com_modelo = models.CharField(max_length=30, blank=True, null=True)
    com_marca = models.CharField(max_length=30, blank=True, null=True)
    com_caracteristica = models.CharField(max_length=30)
    com_dep = models.ForeignKey('Dependencia', models.DO_NOTHING, blank=True, null=True)
    com_anio_ingreso = models.TextField(blank=True, null=True)  # This field type is a guess.
    com_disponible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'componente'

