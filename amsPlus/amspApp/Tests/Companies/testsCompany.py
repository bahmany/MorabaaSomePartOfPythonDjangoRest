import json
import os
import uuid
from django.core.wsgi import get_wsgi_application
from django.test.utils import setup_test_environment
from django.utils import unittest


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'amspApp.Tests.settings'
        # from mongoengine import connect

        # connect("amsPlusMongo")
        application = get_wsgi_application()
        # settings.configure(_settings)
        setup_test_environment()


    def test_model_create_company_should_return(self):
        guid = uuid.uuid4().hex
        from amspApp.amspUser.models import MyUser

        newUser = MyUser(
            username=guid + "test1",
            email=guid + "test1@edd.com",
            password=guid + "test1",
        )
        newUser.save()
        # user created
        # creating new company from model
        from amspApp.CompaniesManagment.models import Company

        newCompany = Company(
            owner_user=newUser,
            name="Hellow" + guid
        )
        newCompany.save()
        self.assertIsNotNone(newCompany.id)

    def test_model_create_duplicate_company_should_return_duplicate_exception(self):
        guid = uuid.uuid4().hex
        from amspApp.amspUser.models import MyUser

        newUser = MyUser(
            username=guid + "test1",
            email=guid + "test1@edd.com",
            password=guid + "test1",
        )
        newUser.save()
        # user created
        # creating new company from model
        from amspApp.CompaniesManagment.models import Company

        newCompany = Company(
            owner_user=newUser,
            name="Hellow" + guid
        )
        newCompany.save()

        newCompany2 = Company(
            owner_user=newUser,
            name="Hellow" + guid
        )
        from django.core.exceptions import ValidationError

        self.assertRaises(newCompany2.save(), ValidationError)

    def test_serializer_create_company(self):
        guid = uuid.uuid4().hex
        from amspApp.amspUser.models import MyUser

        newUser = MyUser(
            username=guid + "test1",
            email=guid + "test1@edd.com",
            password=guid + "test1",
        )
        newUser.save()
        # user created

        newCompany = {
            "name": "testName",
            "details": {
                "test1": "test2",
                "test11": "test3",
                "test12": "test4",
                "test13": "test5",
                "test14": "test6",

            },
            "owner_user": newUser
        }
        from amspApp.CompaniesManagment.serializers.CompanySerializers import CompanySerializer
        newCompany = CompanySerializer(data=newCompany)
        if newCompany.is_valid():
            newCompany = newCompany.create(newCompany.validated_data)

        self.assertTrue(newCompany)







