from rest_framework import serializers

from clients.models import User, AdditionalInfo
from companies.models import Company


class NativeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = 'id', 'full_name', 'cut_name', 'inn', 'kpp', 'created_at', 'updated_at',


class ListCompanySerializer(NativeCompanySerializer):
    pass
