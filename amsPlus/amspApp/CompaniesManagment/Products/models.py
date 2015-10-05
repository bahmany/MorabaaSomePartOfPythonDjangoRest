from datetime import datetime
from mongoengine import Document, IntField, ReferenceField, DateTimeField, StringField, DictField
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile

__author__ = 'mohammad'





class CompanyProductions(Document):
    authorUserID = IntField()
    companyProfile = ReferenceField(CompanyProfile, required=True)
    dateOfPost = DateTimeField(default=datetime.now())
    name = StringField(max_length=400, required=True)
    extra = DictField()
