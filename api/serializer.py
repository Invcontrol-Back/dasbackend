from rest_framework import serializers
from .models import *



class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'  
 