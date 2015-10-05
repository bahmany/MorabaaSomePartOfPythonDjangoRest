from datetime import datetime
from mongoengine import *
# from mongoengine import Document

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models
from rest_framework.fields import CharField
from amspApp.MyProfile.models import Profile

__author__ = 'mohammad'
"""
This model holds everything about companies
so
here we have simple model to keep basic details of company
then more details keep on mongodb

"""


class Company(models.Model):
    owner_user = models.IntegerField(null=True,blank=True)
    #     to=MyUser,
    #     null=False,
    #     blank=False,
    #     help_text=_("Required, Please Choose a valid user to set owner of this company"),
    #     related_name="set_companies"
    # )
    name = models.CharField(
        null=False,
        blank=False,
                                   max_length=60,

    )
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True
    )

    public_name = models.CharField(null=True,
                                   blank=True,
                                   unique=True,
                                   max_length=60,

    )

    # this field is for showing if the following company is created automatically by server or not
    # is a company created by server , clients is not allowed to delete them

    automatically_created = models.BooleanField(default=False, blank=True)

    default = models.NullBooleanField(
        blank=True,
        null=True,
        default=False)


class CompanyDetails(Document):
    company = IntField()
    details = DictField()


class CompanyMembersJointRequest(Document):
    company = IntField(required=True)
    receiver = ReferenceField(Profile, required=True)
    chart = IntField(required=True)
    seen = BooleanField(required=True)
    dateOfPost = DateTimeField(default=datetime.now())
    sender = ReferenceField(Profile, required=True)
    isEmpty = BooleanField(required=False, default=False) # this field is for when we have an empty position with entire inbox
    positionID = IntField(required=False) # if is empty  = true then this field store positionID
    positionDocID = ObjectIdField(required=False) # this field store the exact place of position in pos docs







