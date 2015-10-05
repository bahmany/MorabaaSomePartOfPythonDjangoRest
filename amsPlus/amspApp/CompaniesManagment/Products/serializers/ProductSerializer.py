from rest_framework_mongoengine.serializers import DocumentSerializer
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile
from amspApp.CompaniesManagment.Products.models import CompanyProductions

__author__ = 'mohammad'
class CompanyProductionSerializer(DocumentSerializer):
    class Meta:
        model = CompanyProductions
        fields = (
            'id',
            'name',
            'dateOfPost',
            'extra',
        )

    # def create(self, validated_data):
    #     super().create()


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)




    def create(self, validated_data, **kwargs):
        validated_data["authorUserID"] = self._kwargs["context"]["request"].user.id
        validated_data["companyProfile"] = \
            CompanyProfile.objects.get(companyID = self._kwargs['context']['view'].kwargs['companyID_id'])
        return super(CompanyProductionSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data["authorUserID"] = self._kwargs["context"]["request"].user.id
        validated_data["companyProfile"] = \
            CompanyProfile.objects.get(companyID = self._kwargs['context']['view'].kwargs['companyID_id'])
        return super(CompanyProductionSerializer, self).update(instance, validated_data)
