from rest_framework import serializers
from .models import *

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__' 

class BloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque
        fields = '__all__' 

