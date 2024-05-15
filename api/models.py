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