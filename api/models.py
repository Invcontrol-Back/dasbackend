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


class Localizacion(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50)
    loc_ubi = models.ForeignKey('Ubicacion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'localizacion'

class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_nombre = models.CharField(max_length=30)
    ubi_blo = models.ForeignKey('bloque', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ubicacion'

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
