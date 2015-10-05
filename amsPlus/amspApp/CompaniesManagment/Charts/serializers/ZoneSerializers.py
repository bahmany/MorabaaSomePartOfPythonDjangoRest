from rest_framework import serializers
from rest_framework.fields import BooleanField
from amspApp.CompaniesManagment.Charts.models import ChartZones, ZoneItems

__author__ = 'mohammad'




class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartZones
        fields = ("id","title","company","post_date")



class ZoneItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZoneItems
        fields = ("id","zone","chart","post_date")



