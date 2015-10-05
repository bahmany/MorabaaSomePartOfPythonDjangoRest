import uuid
from django.contrib.auth.models import Group, Permission
from requests import Response
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from amspApp.amspUser.models import MyUser

class UserGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        style={
            'template': 'forms/base-templates/textarea.html',
            'cssclass': 'col-md-12',
            'ngmodel': 'group.name'
        },
        label='name', validators=[UniqueValidator(queryset=Group.objects.all())])
    permissions = serializers.PrimaryKeyRelatedField(many=True, queryset=Permission.objects.all(), required=False,
                                                     style={'template': 'forms/base-templates/select_multiple.html',
                                                            'cssclass': 'col-md-12', 'ngmodel': 'group.permissions',
                                                            'searchFunc': 'searchPermissions()',
                                                            'searchInput': 'permissionSearchInput',
                                                            'options': 'permissionsOptions','dataname':'name'},

                                                     label='permissions', )
    user_set = serializers.PrimaryKeyRelatedField(many=True, queryset=MyUser.objects.all(), required=False,
                                                     style={'template': 'forms/base-templates/select_multiple.html',
                                                            'cssclass': 'col-md-12', 'ngmodel': 'group.user_set',
                                                            'searchFunc': 'searchUsers()',
                                                            'searchInput': 'userSearchInput',
                                                            'options': 'userOptions','dataname':'username'},

                                                     label='users', )
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions','user_set')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.permissions = validated_data.get('permissions', instance.permissions)
        instance.user_set = validated_data.get('user_set', instance.user_set)

        instance.save()

        return instance

