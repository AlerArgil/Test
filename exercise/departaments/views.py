from django.db.models import Prefetch
from rest_framework import generics

from departaments.models import Departament
from departaments.serializers import ListDepartamentSerializer


class DepartamentList(generics.ListAPIView):
    """
    DRF class to list Departaments(with depth level and binding departaments)
    """
    queryset = Departament.objects.prefetch_related(
        Prefetch('families', queryset=Departament.objects.select_related('parent'))
    ).all()
    serializer_class = ListDepartamentSerializer
