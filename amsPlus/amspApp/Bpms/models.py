from mongoengine import *"""
WSGI config for bmps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from amspApp.CompaniesManagment.Processes.models import Bpmn


class LunchedProcess(Document):
    user_id=StringField()
    position_id = StringField()
    bpmn = ReferenceField(document_type=Bpmn)
    sorry skipped
