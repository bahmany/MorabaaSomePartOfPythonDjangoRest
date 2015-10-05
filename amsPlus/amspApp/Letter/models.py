from datetime import datetime
from mongoengine import *
from rest_framework.fields import NullBooleanField


class InboxFolder(Document):
    positionID = IntField(required=False, null=True, )
    companyID = IntField(required=False, null=True)
    parentID = StringField(required=False, null=True)
    isPublic = IntField(default=0)
    title = StringField(required=True)
    count = IntField(default=0)


class InboxLabel(Document):
    positionID = IntField()
    companyID = IntField()
    title = StringField()
    color = StringField()
    bgcolor = StringField()
    count = IntField(default=0)


class InboxGroup(Document):
    positionID = IntField()
    companyID = IntField()
    title = StringField()
    members = ListField()
    count = IntField(default=0)
    meta = {'indexes': [
        {'fields': ['$title'],
         'default_language': 'english',
         'weights': {'title': 1}
        },
    ],
    }


class Letter(Document):
    subject = StringField(max_length=50)
    body = StringField(max_length=6000)
    dateOfPost = DateTimeField(default=datetime.now())
    letterType = IntField()  # 1=Dakheli 2=Sadereh 3=Varedeh 4=Document 5=Message 6=report 7=draft dekheli 8=draft sadere 9=draft dakheli
    creatorPositionID = IntField()
    creatorPosition = DictField()
    recievers = ListField()
    ccrecievers = ListField()
    secretariatID = IntField()
    secretariat = DictField()
    hasAttachment = BooleanField()
    attachments = ListField()
    security = IntField()  # 1=addi 2=mahramaneh 3=serri
    periority = IntField()  # 1=addi 2=forri 3=kheili forri
    related = ListField()
    sign = DictField()
    parent = DictField()


class Inbox(Document):
    currentPositionID = IntField()
    dateOfObservable = DateTimeField()
    dateOfCreate = DateTimeField(default=datetime.now())
    sender = DictField()
    reciever = DictField()
    hamesh = DictField()
    letterID = IntField()
    security = IntField()  # 1=addi 2=mahramaneh 3=serri
    periority = IntField()  # 1=addi 2=forri 3=kheili forri
    letter = DictField()
    labels = ListField()
    readTimes = ListField()
    seen = BooleanField(default=False)
    """
    itemType:
    1 = this inbox item received and sent by some one else as usual inside letter
    2 = this inbox item is sent to a user and an inbox item listed in send letters
    3 = this inbox item forwarded
    4 = this inbox item is replied one, i mean this letter is a replay letter
    5 = this inbox item is auto send inbox as rooneveshte khodkar

    """
    itemType = IntField(default=1)
    replyedInbox = DictField()  # when a sent=4 this field store old inbox body
    """
    itemMode :
    1= dakheli
    2= rooneveshte sadereh
    3= rooneveshte varedeh
    4= draft
    5= draft sadere
    6= draft varedeh
    """
    itemMode = IntField(default=1)




