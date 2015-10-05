from mongoengine import *

class Bpmn(Document):

    user_id = IntField()
    company_id = IntField(default=1)
    name = StringField(max_length=50,required=True)
    description = StringField(max_length=255,null=True,required=False)
    xml = StringField(null=True,required=False)
    form = ListField(null=True,required=False)
    processObjs = ListField(null=True,required=False)
    userTasks = ListField(null=True,required=False)
    is_valid_form = BooleanField(default=False)
