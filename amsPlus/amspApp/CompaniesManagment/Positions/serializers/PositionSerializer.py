from rest_framework import serializers
from rest_framework.fields import CharField
from amspApp.CompaniesManagment.Positions.models import Position,PositionsDocument
from amspApp.MyProfile.models import Profile
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from amspApp._Share.DynamicFieldModelSerializer import DynamicFieldsModelSerializer
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer

from amspApp.amspUser.models import MyUser
from amspApp.amspUser.serializers.UserSerializer import UserSerializer, UserNameSerializer


class PositionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Position
        fields = ("id", "company", "chart", "user", "post_date")
        depth = 1



class PositionDocumentSerializer(DynamicFieldsDocumentSerializer):
    class Meta:
        model = PositionsDocument
        depth = 1



    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

class PrositionSerializerJustUsername(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("id", "user")
        depth = 0




