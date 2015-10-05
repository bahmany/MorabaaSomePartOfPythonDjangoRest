from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.models import Company
from amspApp.amspUser.models import MyUser

__author__ = 'mohammad'

from django.db import models
from django.utils.translation import ugettext_lazy as _


"""

ems
"""


class Secretariat(models.Model):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False)
    dakheli_letters_format = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    sadereh_letters_format = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    varede_letters_format = models.CharField(
        max_length=255,
        blank=False,
        null=False)

    dakheli_last_id = models.IntegerField(
        blank=False,
        null=False,

    )
    sadere_last_id = models.IntegerField(
        blank=False,
        null=False)
    varede_last_id = models.IntegerField(
        blank=False,
        null=False)
    post_date = models.DateTimeField(
        default=datetime.now(),
        blank=True
    )

    company = models.ForeignKey(
        Company,
        related_name="set_secratraite"
    )


class SecretariatPermissions(models.Model):
    chart = models.ForeignKey(
        Chart,
        related_name="set_SecretariatPermissions",
    )
    secretariat = models.ForeignKey(
        Secretariat,
        related_name="set_SecretariatPermissions"
    )
    permission = models.CharField(
        default="000",  # index[0]= dakheli 1=sadereh 2=varede
        blank=True,
        null=True,
        max_length=3)
    default = models.NullBooleanField(
        blank=True,
        null=True,
        default=False)
    post_date = models.DateTimeField(
        default=datetime.now,
        blank=True
    )


