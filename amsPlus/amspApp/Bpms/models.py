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
    name = StringField(max_length=255, null=True, required=False)
    thisStep = StringField(max_length=255, null=True, required=False)
    thisPerformer = StringField()
    isComplete = BooleanField(default=True)
    thisStatus = StringField(max_length=255, null=True, required=False)
    engineInstance = BinaryField(null=True, required=False)
    formData = DictField(null=True, required=False)
