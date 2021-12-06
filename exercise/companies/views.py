from django.db.models import Prefetch
from rest_framework import generics

from companies.models import Company
from companies.serializers import ListCompanySerializer
from departaments.models import Departament


class CompanyList(generics.ListAPIView):
    """
    Company List view
    """
    queryset = Company.objects.prefetch_related(
        Prefetch('departaments', queryset=Departament.objects.prefetch_related('users'))
    ).all()
    serializer_class = ListCompanySerializer
