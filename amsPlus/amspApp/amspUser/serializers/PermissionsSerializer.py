import uuid
from django.contrib.auth.models import Group, Permission
from requests import Response
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class PermissionsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')

    def update(self, instance, validated_data):
        pass
    def create(self, validated_data):
        pass
