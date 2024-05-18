from django.db import models

# Create your models here.

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