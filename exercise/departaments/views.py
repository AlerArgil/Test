from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from departaments.models import Departament
from departaments.serializers import ListDepartamentSerializer


class DepartamentList(generics.ListAPIView):
    queryset = Departament.objects.all()
    serializer_class = ListDepartamentSerializer
    pagination_class = LimitOffsetPagination
