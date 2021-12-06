from rest_framework import serializers

from clients.models import User, AdditionalInfo
from departaments.models import Departament


class NativeDepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = 'id', 'name', 'level', 'company'


class ListDepartamentSerializer(NativeDepartamentSerializer):
    pass
