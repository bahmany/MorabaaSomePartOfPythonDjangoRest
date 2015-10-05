from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from amspApp.CompaniesManagment.Charts.serializers.ChartSerializers import ChartSerializer
from amspApp.CompaniesManagment.CompanyProfile.serializers.CompanyProfileSerializers import CompanyProfileSerializer
from amspApp.CompaniesManagment.Secretariat.serializers.SecretariatsSerializers import SecretariatSerializer, \
    SecretariatSerializerPermission
from amspApp.CompaniesManagment.members.serializers.MemberSerializer import MembersSerializer
from amspApp.CompaniesManagment.models import Company, CompanyDetails
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from amspApp.amspUser.models import MyUser

__author__ = 'mohammad'


class CompanySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(
    #     style={'template': 'forms/base-templates/textarea.html',
    #            'cssclass': 'col-md-12',
    #            'ngmodel': 'company.name'},
    #     label=_("Name"),
    #     max_length=60,
    #     min_length=3,
    #     required=True,
    #     allow_blank=False
    # )



    class Meta:
        model = Company
        fields = ("id", "name", "owner_user", "post_date",  "automatically_created", "public_name")


    def get_users(self, obj):
        return MyUser.objects.all()

    def validate_name(self, data):
        countOfName = Company.objects.all().filter(
            name=data,
            owner_user=self._kwargs["data"]["owner_user"]
        ).count()
        if countOfName > 0:
            raise serializers.ValidationError(_("Please change company name, it should by unique"))
        return data


    def create(self, validated_data):
        # creating company in mongodb
        # whenever company creates it make himself in mongodb
        newCompanyDataForModel = validated_data



        newCompanyDataForModel["owner_user"] = self._kwargs["data"]["owner_user"]
        newCompanyDataForModel["public_name"] = None
        if not "automatically_created" in newCompanyDataForModel:
            newCompanyDataForModel["automatically_created"] = False

        newCompany = Company.objects.create(**newCompanyDataForModel)

        newCompanyDetail = CompanyProfileSerializer().create_default_company_profile(newCompany.id, self._kwargs["data"]["owner_user"], newCompany.name)

        self.createDepedenciesOfCompany(self._kwargs["data"]["owner_user"], newCompany)

        return newCompany

    def createDepedenciesOfCompany(self, user, newCompany):

        # CompanyProfileSerializer().create_default_company_profile(newCompany.id, user, newCompany.name)
        chartOfNewUser = ChartSerializer().create_default_chart(newCompany)
        newMember = {
            "chart": chartOfNewUser.id,
            "user": user,
            "company": newCompany.id,
        }
        newMemberPosition = MembersSerializer(data = newMember)
        newMemberPosition.is_valid(raise_exception=True)
        newMemberPosition.create(newMember)
        newSec = {
            'name': _("main office"),
            'dakheli_letters_format': 'yy./.xxxx',
            'sadereh_letters_format': 'yy./.1./.xxxx',
            'varede_letters_format': 'yy./.2./.xxxx',
            'dakheli_last_id': 0,
            'sadere_last_id': 0,
            'varede_last_id': 0,
            'company': newCompany.id
        }
        newSec = SecretariatSerializer(data=newSec)
        newSec.is_valid(raise_exception=True)
        newSec = newSec.create(newSec.validated_data)
        newSecPerm = {
            "chart": chartOfNewUser.id,
            "secretariat": newSec.id,
            "permission": "111",
            "default": True,
            }
        newSecPerm = SecretariatSerializerPermission(data = newSecPerm)
        newSecPerm.is_valid(raise_exception=True)
        newSecPerm = newSecPerm.create(newSecPerm.validated_data)




    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()
        return instance


    """
    This procedure call by user registration, to create all depedencies
    """
    def create_default_company_from_user(self, MyUser):
        newComp = {
            "owner_user":MyUser.id,
            "name":str(_("Default company of ")) + MyUser.username,
            "public_name":str(_("Default company of ")) + MyUser.username,
            "automatically_created":True
        }
# "id", "name", "owner_user", "post_date",  "automatically_created", "public_name"
        # a new company created with its dependecies
        # dependecies are : chart, secratrait, profile, company profile
        newCompany = CompanySerializer(data = newComp)
        newCompany.is_valid(raise_exception=True)
        newCompany = newCompany.create(newComp)
        # this company gets default
        MyUser.current_company = newCompany
        MyUser.save()
        # ChartSerializer().create_default_chart(newCompany)
        return newCompany













