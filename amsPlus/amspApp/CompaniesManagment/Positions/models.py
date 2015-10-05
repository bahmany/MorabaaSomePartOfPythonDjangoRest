from datetime import datetime
from mongoengine import Document, IntField, StringField, DateTimeField, ListField
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.models import Company
from amspApp.amspUser.models import MyUser
from django.db import models


class Position(models.Model):
    chart = models.ForeignKey(
        to=Chart,
        null=True,
        blank=True,
        related_name="set_position",
    )
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True
    )

    # here we have a lots of gaps ...
    # all inboxes links to here
    # when company owner eject an employer,
    # developer empty user field and this position going to wait for another user
    # in this way we can keep its positional inbox
    # and we can transfer inbox item to new user,,,
    # but we have to work one more and stimulate more states

    user = models.ForeignKey(
        to=MyUser,
        related_name="set_positions",
        blank=True,
        null=True
    )

    company = models.ForeignKey(
        to=Company,
        related_name="set_positions",
        blank=True,
        null=True
    )



class PositionsDocument(Document):
    chartID = IntField(null=True,)
    userID = IntField(null=True,)
    companyID = IntField(null=True,)
    chartName = StringField(null=True,)
    profileName = StringField(null=True,)
    companyName = StringField(null=True,)
    profileID = StringField(null=True,)
    avatar = StringField(null=True,)
    postDate = DateTimeField()
    last = ListField(null=True,)
    positionID = IntField(required=False, null=True)
    """
    hasBulkSentPermission :
    0 = has not permission
    1 = has permission
    """
    hasBulkSentPermission = IntField(required=False, null=True, default=1)

    """
    isPositionAllowedToSendDirectly
    0 = No
    1 = Yes
    This is for auto send letters through chart hierarchy
    """
    isPositionAllowedToSendDirectly = IntField(required=False, null=True, default=1)

    """
    isPositionIgonreAssistantHardSent
    0 = No
    1 = Yes
    """
    isPositionIgonreAssistantHardSent = IntField(required=False, null=True, default=1)


    meta = {'indexes': [
        {'fields': ['$profileName', "$chartName"],
         'default_language': 'english',
         'weights': {'profileName': 1, 'chartName': 1}
        },
    ],
    }
