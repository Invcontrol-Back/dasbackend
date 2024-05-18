from django.db.models import F
from rest_framework import viewsets
from .models import *
from .serializer import *

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class BloqueViewSet(viewsets.ModelViewSet):
    queryset = Bloque.objects.annotate(fac_nombre=F('blo_fac__fac_nombre')).all()
    serializer_class = BloqueSerializer

class TipoUbicacionViewSet(viewsets.ModelViewSet):
    queryset = TipoUbicacion.objects.all()
    serializer_class = TipoUbicacionSerializer    

class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.annotate(tip_ubi_nombre=F('sof_tip_ubi__tip_ubi_nombre')).all()
    serializer_class = SoftwareSerializer