from rest_framework import serializers

from companies.models import Company
from departaments.serializers import ListDepartamentSerializer, DepartamentWithUserSerializer


class NativeCompanySerializer(serializers.ModelSerializer):
    """
    Comapny serializer with basic fields
    """
    class Meta:
        model = Company
        fields = 'id', 'full_name', 'cut_name', 'inn', 'kpp', 'created_at', 'updated_at',


class ListCompanySerializer(NativeCompanySerializer):
    """
    Company Serializers for List Ciew
    """
    departaments = DepartamentWithUserSerializer(many=True)

    class Meta(NativeCompanySerializer.Meta):
        fields = NativeCompanySerializer.Meta.fields + ('departaments',)

