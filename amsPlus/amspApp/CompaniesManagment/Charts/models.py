from datetime import datetime
from django.core.validators import MinValueValidator
from amspApp.CompaniesManagment.models import Company
from amspApp.amspUser.models import MyUser

__author__ = 'mohammad'

from django.db import models
from django.utils.translation import ugettext_lazy as _


"""
this model is for ChartZones
this is very usefull for BPMS
we have two area, ChartZone, and ChartZoneItems
"""


class Chart(models.Model):
    top = models.ForeignKey(
        to='self',
        null=True,
        blank=True,
        related_name="set_top",
        help_text=_("Required, This is for upper chart position for making tree like structure of a organization")
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=[
            MinValueValidator(3, _("Please enter more than 3 character"))
        ])
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        to=Company,
        null=False,
        blank=False,
        help_text=_("Required, Please Choose a valid user to set owner of this position"),
        related_name="set_position"
    )


class ChartZones(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        # validators=[
        #     MinValueValidator(3, _("Please enter more than 3 character"))
        # ]
        )
    company = models.ForeignKey(
        null=False,
        blank=False,
        to=Company,
        related_name="set_zones",
        help_text=_("Required, Please select your preferred company to gain this zone")
    )
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True
    )


class ZoneItems(models.Model):
    zone = models.ForeignKey(
        null=False,
        blank=False,
        to=ChartZones,
        related_name="set_items",
    )
    chart = models.ForeignKey(
        null=False,
        blank=False,
        to=Chart,
        related_name="set_zones"
    )
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True
    )




