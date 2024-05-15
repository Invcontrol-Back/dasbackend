from django.db import models

# Create your models here.

class Facultad(models.Model):
    fac_id  = models.AutoField(primary_key=True)
    fac_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'facultad' 