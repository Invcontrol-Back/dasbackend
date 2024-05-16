from rest_framework import serializers
from .models import *

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__' 

class BloqueSerializer(serializers.ModelSerializer):
    fac_nombre = serializers.CharField(source='blo_fac.fac_nombre', read_only=True)
    class Meta:
        model = Bloque
        fields = ['blo_id', 'blo_nombre', 'blo_fac', 'fac_nombre']

