from rest_framework_mongoengine.serializers import *
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Charts.serializers.ChartSerializers import ChartSerializer
from amspApp.CompaniesManagment.models import CompanyMembersJointRequest
from amspApp._Share.DynamicFieldModelSerializer import DynamicFieldsModelSerializer
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer

__author__ = 'mohammad'




class CompanyMembersJointRequestSerializer(DynamicFieldsDocumentSerializer):
    senderName= serializers.CharField(source='sender.extra.Name',read_only=True)
    receiverName= serializers.CharField(source='receiver.extra.Name',read_only=True)
    # chartName= chartNameField(queryset = Chart.objects.all())
    # chartName= serializers.CharField(source='chart.title',read_only=True)
    # companyName= serializers.CharField(source='company.name',read_only=True)
    class Meta:
        model = CompanyMembersJointRequest
        depth = 0
        extra_kwargs = {
            'receiver': {'write_only': True},
            'sender': {'write_only': True},
            # 'chart': {'write_only': True},
            # 'company': {'write_only': True},
        }

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

