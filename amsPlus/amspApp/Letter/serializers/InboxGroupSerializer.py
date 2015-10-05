from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder, InboxLabel, InboxGroup
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer


class InboxGroupSerializer(DynamicFieldsDocumentSerializer):
    title = serializers.CharField(allow_null=False, allow_blank=False)

    class Meta:
        model = InboxGroup
        fields = (
            'id',
            'positionID',
            'companyID',
            'title',
            'members',
            'count',
        )


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)



class InboxGroupSerializerForInboxSidebar(DynamicFieldsDocumentSerializer):
    memberCount = SerializerMethodField()

    class Meta:
        model = InboxGroup
        fields = (
            'id',
            'positionID',
            'companyID',
            'memberCount',
            'title',
            'count',
        )

    def get_memberCount(self, obj):
        res = len(obj.members)
        return res


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)



