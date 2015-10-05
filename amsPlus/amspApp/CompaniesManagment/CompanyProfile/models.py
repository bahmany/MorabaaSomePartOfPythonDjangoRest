from datetime import datetime
from mongoengine import *

__author__ = 'mohammad'
class CompanyProfile(Document):
    companyID = IntField(unique=True)
    creatorUserID = IntField()
    dateOfPost = DateTimeField(default=datetime.now())
    extra = DictField()

# class CompanyNews(Document):
#     authorUserID = IntField()
#     companyProfile = ReferenceField(CompanyProfile)
#     dateOfPost = DateTimeField(default=datetime.now())
#     text = StringField(max_length=400)
#     extra = DictField()
#






