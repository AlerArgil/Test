from rest_framework import serializers

from clients.models import User, AdditionalInfo


class NativeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'password', 'last_login', 'is_superuser', 'username', 'is_staff', 'is_active', 'date_joined', 'id', \
                 'phone', 'first_name', 'last_name', 'middle_name', 'type', 'gender', 'timezone', 'ok', 'instagram', \
                 'telegram', 'whatsapp', 'viber', 'created_at', 'updated_at',


class ListUserSerializer(NativeUserSerializer):
    additional_info = 'AdditionalInfoSerializers'


class NativeAdditionalInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = 'user', 'type', 'value'


class AdditionalInfoSerializers(NativeAdditionalInfoSerializers):
    pass
