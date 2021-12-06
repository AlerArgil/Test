from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from companies.models import Company
from companies.serializers import ListCompanySerializer


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = ListCompanySerializer
    pagination_class = LimitOffsetPagination
