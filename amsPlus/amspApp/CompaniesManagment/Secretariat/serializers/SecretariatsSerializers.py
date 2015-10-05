from rest_framework import serializers
from amspApp.CompaniesManagment.Secretariat.models import Secretariat, SecretariatPermissions


class SecretariatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretariat

class SecretariatSerializerPermission(serializers.ModelSerializer):
    class Meta:
        model = SecretariatPermissions

