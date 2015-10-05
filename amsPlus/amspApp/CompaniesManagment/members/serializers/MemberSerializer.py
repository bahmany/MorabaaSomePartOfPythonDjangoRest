from datetime import datetime
from rest_framework import serializers
from rest_framework.fields import Field, CharField
from rest_framework.serializers import ModelSerializer
from rest_framework_mongoengine.serializers import DocumentSerializer
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Positions.models import Position, PositionsDocument
from amspApp.CompaniesManagment.models import Company
from amspApp.MyProfile.models import Profile
from amspApp._Share.DynamicFieldModelSerializer import DynamicFieldsModelSerializer
from amspApp.amspUser.models import MyUser


__author__ = 'mohammad'
# class MembersSerializer(DynamicFieldsModelSerializer):
class MembersSerializer(ModelSerializer):
    userName = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Position
        # fields = ("id","post_date","userName")
        depth = 0

    def get_userName(self, obj):
        profileName = Profile.objects.get(userID=obj.user_id)
        result = {
            "name": profileName.extra["Name"],
            "avatar": profileName.extra["profileAvatar"]["url"],
            "job": obj.chart.title
        }
        return result


    # here is very important
    def create_in_mongo(self, data, positionInstance):
        if "chart" in data and "company" in data:
            if data["chart"] == None and data["company"] == None:
                posInstance = self._kwargs['instance']
                finalChanges = {
                    "chartID": posInstance.chart_id,
                    "companyID": posInstance.company_id,
                    "userID": posInstance.user_id,
                    "dateof": datetime.now(),

                }
                pos = PositionsDocument.objects.get(
                    chartID=posInstance.chart_id,
                    companyID=posInstance.company_id,
                    userID=posInstance.user_id
                )
                ll = pos.last
                if ll == None:
                    ll = [finalChanges]
                else:
                    ll.append(finalChanges)
                pos.last = ll
                pos.chartID = None
                pos.companyID = None
                pos.save()
                return pos

        if "user" in data:
            if data["user"] == None:
                posInstance = self.instance
                finalChanges = {
                    "chartID": posInstance.chart_id,
                    "companyID": posInstance.company_id,
                    "userID": posInstance.user_id,
                    "dateof": datetime.now()
                }
                pos = PositionsDocument.objects.get(
                    positionID = posInstance.id
                )
                ll = pos.last
                if ll == None:
                    ll = [finalChanges]
                else:
                    ll.append(finalChanges)
                pos.last = ll
                pos.userID = None
                pos.profileID = None
                pos.avatar = None
                pos.profileName = None
                pos.save()
                return pos

        userInstance = MyUser.objects.get(id=data["user"]) if type(data["user"]) == int else data["user"]
        profileInstance = Profile.objects.get(userID=userInstance.id)
        final = {}
        if self.partial:
            final = {
                'chartID': positionInstance.chart.id,
                'profileID': profileInstance.id.__str__(),
                'userID': data["user"] if type(data["user"]) == int else data["user"].id,
                'companyID': positionInstance.company.id,
                'chartName': positionInstance.chart.title,
                'profileName': profileInstance.extra["Name"],
                'avatar': profileInstance.extra["profileAvatar"]["url"],
                'companyName': positionInstance.company.name,
                'post_date': data["post_date"]
            }
            posDoc = PositionsDocument.objects.get(
                positionID = self.instance.id
            )
            posDocSerial = MembersDocumentSerializer(instance=posDoc, data=final, partial=True)
            posDocSerial.is_valid(raise_exception=True)
            posDocSerial.update(instance=posDoc, validated_data=posDocSerial.validated_data)
            return
        else:
            final = {
                'chartID': data["chart"].id,
                'profileID': profileInstance.id.__str__(),
                'userID': data["user"].id if data["user"] != None else None,
                'companyID': data["company"].id,
                'chartName': data["chart"].title,
                'profileName': profileInstance.extra["Name"],
                'avatar': profileInstance.extra["profileAvatar"]["url"],
                'companyName': data["company"].name,
                'positionID':positionInstance.id
            }


        # if data['chart'].set_position.all().count() != 0:
        # raise serializers.ValidationError({"status": "Bad request", "message": {
        # "Created Before": ["This user has an chart position before, first you must faceout it"]}})

        poss = PositionsDocument.objects.filter(
            companyID=data["company"].id,
            userID=data["user"] if type(data["user"]) == int else data["user"].id
        )
        if poss.count() != 0:
            raise serializers.ValidationError({"status": "Bad request", "message": {
                "Created Before": ["This user has an chart position before, first you must faceout it"]}})

        PositionsDocument.objects.create(**final)
        return


    def create(self, validated_data):

        if type(validated_data['chart']) == int:
            validated_data["chart"] = Chart.objects.get(id=validated_data["chart"])
        if type(validated_data['company']) == int:
            validated_data["company"] = Company.objects.get(id=validated_data["company"])
        if type(validated_data['user']) == int:
            validated_data["user"] = MyUser.objects.get(id=validated_data["user"])

        # if validated_data['chart'].set_position.all().count() != 0:
        # raise serializers.ValidationError({"status": "Bad request", "message": {
        # "Created Before": ["This user has an chart position before, first you must faceout it"]}})

        if Position.objects.filter(user=validated_data["user"], company=validated_data["company"]).count() != 0:
            raise serializers.ValidationError({"status": "Bad request", "message": {
                "Created Before": ["This user has an chart position before, first you must faceout it,"]}})
        positionInstace = super(MembersSerializer, self).create(validated_data)
        self.create_in_mongo(validated_data, positionInstace)
        return positionInstace

    def update(self, instance, validated_data):
        updatedPosition = super(MembersSerializer, self).update(instance, validated_data)
        self.create_in_mongo(validated_data, updatedPosition)
        return updatedPosition


class MembersDocumentSerializer(DocumentSerializer):
    class Meta:
        model = PositionsDocument


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

