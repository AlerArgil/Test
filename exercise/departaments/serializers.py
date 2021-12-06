from rest_framework import serializers

from clients.serializers import NativeUserSerializer
from departaments.models import Departament, Family


class NativeParentSerializers(serializers.ModelSerializer):
    """
    Serializer with basic field for Family departament relation
    """
    class Meta:
        model = Family
        fields = 'id', 'parent', 'child'


class NativeDepartamentSerializer(serializers.ModelSerializer):
    """
    Serializer with basic field for Departament model
    """
    class Meta:
        model = Departament
        fields = 'id', 'name', 'company'


class DepartamentWithFamiliesSerializer(NativeDepartamentSerializer):
    """
    Serializer Departament model with Family information
    """
    parent = NativeParentSerializers()

    class Meta(NativeDepartamentSerializer.Meta):
        fields = NativeDepartamentSerializer.Meta.fields + ('parent',)


class ListDepartamentSerializer(NativeDepartamentSerializer):
    """
    Serializer Departament model for list view
    """
    families = DepartamentWithFamiliesSerializer(many=True)

    class Meta(NativeDepartamentSerializer.Meta):
        fields = NativeDepartamentSerializer.Meta.fields + ('families',)


class DepartamentWithUserSerializer(NativeDepartamentSerializer):
    """
    Serializer Departament model with Users relation for Company list view
    """
    users = NativeUserSerializer(many=True)

    class Meta(NativeDepartamentSerializer.Meta):
        fields = NativeDepartamentSerializer.Meta.fields + ('users',)
