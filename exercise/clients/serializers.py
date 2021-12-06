from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

from clients.models import User, AdditionalInfo


class NativeAdditionalInfoSerializers(serializers.ModelSerializer):
    """
    AdditionalInfo serialiszer with basic fields
    """
    class Meta:
        model = AdditionalInfo
        fields = 'user', 'type', 'value'


class AdditionalInfoSerializers(NativeAdditionalInfoSerializers):
    """
    AdditionalInfo serialiszer for main and use
    """
    pass


class NativeUserSerializer(serializers.ModelSerializer):
    """
    User serializer with basic fields
    """
    timezone = TimeZoneSerializerField()

    class Meta:
        model = User
        fields = 'password', 'last_login', 'is_superuser', 'username', 'is_staff', 'is_active', 'date_joined', 'id', \
                 'phone', 'first_name', 'last_name', 'middle_name', 'type', 'gender', 'timezone', 'ok', 'instagram', \
                 'telegram', 'whatsapp', 'viber', 'created_at', 'updated_at',


class ListUserSerializer(NativeUserSerializer):
    """
    User serializers with additional infos for List view
    """
    add_infos = AdditionalInfoSerializers(many=True)

    class Meta(NativeUserSerializer.Meta):
        fields = NativeUserSerializer.Meta.fields + ('add_infos',)

