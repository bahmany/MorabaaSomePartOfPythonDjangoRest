from rest_framework import serializers
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder, InboxLabel
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer


class InboxLabelSerializer(DynamicFieldsDocumentSerializer):
    title = serializers.CharField(allow_null=False, allow_blank=False)

    class Meta:
        model = InboxLabel
        fields = (
            'id',
            'positionID',
            'companyID',
            'title',
            'bgcolor',
            'color',
            'count',
        )


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)
    #
    # def validate(self, attrs):
    #     pos = Position.objects.get(user=self.context["request"].user)
    #     if InboxFolder.objects.filter(title=attrs['title'], positionID=pos.id).count() > 0:
    #         raise serializers.ValidationError(
    #             {"status": "Bad request", "message": [{"name": "Name", "message": "This field should be unique"}]})
    #     return super(InboxLabelSerializer, self).validate(attrs)





