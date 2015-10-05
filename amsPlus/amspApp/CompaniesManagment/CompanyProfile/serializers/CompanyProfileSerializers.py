from rest_framework_mongoengine.serializers import DocumentSerializer
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile
from amspApp.CompaniesManagment.models import Company
from django.utils.translation import ugettext_lazy as _

__author__ = 'mohammad'


class CompanyProfileSerializer(DocumentSerializer):
    class Meta:
        model = CompanyProfile
        fields = (
            'id',
            'companyID',
            'creatorUserID',
            'dateOfPost',
            'extra',
        )


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

    def validate(self, attrs):
        from rest_framework import serializers
        if not "name" in attrs["extra"]:
            raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": _("Name"), "message": _("This field is required")}]})
        if attrs["extra"]["name"] == "":
            raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": _("Name"), "message": _("This field is required")}]})
        return attrs


    def update(self, instance, validated_data):
        mysqlcompany = Company.objects.get(id = validated_data["companyID"])
        mysqlcompany.name = validated_data["extra"]["name"]
        mysqlcompany.save()
        return super(CompanyProfileSerializer, self).update(instance, validated_data)


    """
    This method is for using default style of company profile
    """
    def defaultExtra(self, companyName = ""):
        return {
            "logo": "/static/images/default-logo.png",
            "name": companyName,
            "background": "/static/images/default_company_profile_header_background.png",
            "biefIntroduction": " click here to type brief introduction ",
            "introduction": " click here to type complete introduction ",
            "options": [{
                            "type": 1,  # 1=email 2=tel 3=address 4=website
                            "text": "Add Address/Phone/Email/... ",
                            "privacy": 1
                        }]  # keeping tels, emails, address
        }

    def create_default_company_profile(self, companyid, userid, companyName):
        newCompanyProfile = {
                "companyID": companyid,
                "creatorUserID": userid,
                "extra": CompanyProfileSerializer().defaultExtra(companyName),
            }
        CompanyProfile.objects.create(**newCompanyProfile)









