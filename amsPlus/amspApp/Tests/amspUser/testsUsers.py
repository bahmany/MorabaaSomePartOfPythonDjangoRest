from datetime import datetime
import json
import os
from random import randint

from time import timezone
import uuid
from bs4 import BeautifulSoup

from classytags.test.run_tests import run_tests
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http.response import HttpResponse
from django.test import Client, override_settings
from django.test.utils import setup_test_environment, get_runner
import logging

from amspApp.Tests import settings as _settings
import sys
from django.test import TestCase

# if len(sys.argv) > 1 and sys.argv[1] == 'test':
# logging.disable(logging.CRITICAL)

__author__ = 'mohammad'

import unittest


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        # os.environ['DJANGO_SETTINGS_MODULE'] = 'amspApp.Tests.settings'
        os.environ['DJANGO_SETTINGS_MODULE'] = 'amsp.settings'
        application = get_wsgi_application()
        # settings.configure(_settings)
        setup_test_environment()

    def test_when_call_registration_should_return_registration_page_view_as_HttpReponse(self):
        client = Client()
        response = client.get("/our/signup/")
        self.assertEqual(type(response), HttpResponse)

    def test_when_call_registration_should_return_corrent_fields_count(self):
        client = Client()
        response = client.get("/our/signup/")
        content = BeautifulSoup(response.content, 'html.parser')
        objectsOfForm = len(content.div.find_all("div", {"class": "form-group"}))
        self.assertEqual(objectsOfForm, 4)

    def test_create_new_user_and_check_its_integrity(self):
        client = Client()
        gui = uuid.uuid1().hex
        valueToSerialize = \
            {'username': gui + 'alimorad',
             'confirm_password': gui + '1111',
             'password': gui + '1111',
             'email': gui + 'fsdf@test.com'}

        import json

        response = client.post("/api/v1/users/",
                               data=json.dumps(valueToSerialize),
                               content_type='application/json')

        self.assertEqual(response.charset, "utf-8")
        self.assertEqual(response.accepted_media_type, u"application/json")

        # user created !
        # now login with the user

        loginResp = client.login(
            username=gui + 'alimorad', password=gui + '1111'
        )

        self.assertEqual(loginResp, True)


    def create_1000test_user_in_list(self, isItEmail=False):
        names = []

        def createName():
            namesPart1 = ['al', 'bo', 'co', 'da', 'ei', 'fo', 'ha', 'zy', 'qu', 'w', 'x', 'z', 'por']
            newName = ""
            for c in range(1, 4):
                newName += namesPart1[randint(0, len(namesPart1) - 1)]
            for name in names:
                if name == newName:
                    # found duplicate created
                    createName()
                    return
            return newName if isItEmail == False else newName + "@gmailtest.com"

        for i in range(1, 1000):
            names.append(createName())
        return names


    """
    this test is suppose to add 1000 users with their all depedecies
    when a person register these items will be created automatically :
    1 - default company
    2 - default organization chart
    3 - set new user CEO in position
    4 - default secretariat
    5 - set this secretariat as default sec and creates its permission
    6 - creating default profile for user
    7 - creating default company profile
    """

    def test_create_1000_users_and_checking_its_auto_created_depedencies(self):
        client = Client()
        names = self.create_1000test_user_in_list()
        emails = self.create_1000test_user_in_list(isItEmail=True)
        usersToRegister = []
        i = -1
        for name in names:
            i += 1
            usersToRegister.append(
                {'username': name,
                 'confirm_password': "009100",
                 'password': '009100',
                 'email': emails[i]}
            )
        for reg in usersToRegister:
            response = client.post("/api/v1/users/",
                                   data=json.dumps(reg),
                                   content_type='application/json')
        pass


if __name__ == '__main__':
    unittest.main()