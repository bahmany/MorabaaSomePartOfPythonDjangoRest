from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import QuerySet
from rest_framework.decorators import list_route, detail_route
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.CompaniesManagment import Positions
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder, InboxLabel, InboxGroup
from rest_framework import status
from amspApp.Letter.serializers.InboxGroupSerializer import InboxGroupSerializer, InboxGroupSerializerForInboxSidebar
from amspApp.Letter.serializers.InboxFolderSerializer import InboxFolderSerializer
from amspApp.Letter.serializers.InboxLabelSerializer import InboxLabelSerializer
from amspApp._Share.ListPagination import ListPagination


class InboxGroupViewset(viewsets.ModelViewSet):
    pagination_class = ListPagination
    lookup_field = "id"
    serializer_class = InboxGroupSerializer

    def get_queryset(self):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        self.queryset = InboxGroup.objects.filter(positionID=pos.id)
        return super(InboxGroupViewset, self).get_queryset()

    def create(self, request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        request.data["positionID"] = pos.id
        return super(InboxGroupViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        request.data["positionID"] = pos.id
        return super(InboxGroupViewset, self).update(request, *args, **kwargs)

    @list_route(methods=["get"])
    def GetListForBar(self, request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        groups = InboxGroup.objects.filter(positionID=pos.id).limit(100)
        serial = InboxGroupSerializerForInboxSidebar(groups, many=True)
        return Response(serial.data)

    @list_route(methods=["put"])
    def UpdateGroup(self,request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        groupInstance = InboxGroup.objects.get(
            positionID = pos.id,
            id = request.data['group']['id']
        )
        newPosName = {
            "title":request.data["group"]["title"],
            "members":request.data["members"]
        }
        groupSerial = InboxGroupSerializer(instance=groupInstance, data=newPosName, partial=True)
        groupSerial.is_valid(raise_exception=True)
        updatedGroup = groupSerial.update(groupInstance, groupSerial.validated_data)
        return Response({})

    @detail_route(methods=["get"])
    def GetGroupMember(self, request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        groupInstance = InboxGroup.objects.get(
            positionID = pos.id,
            id = kwargs["id"]
        )
        serial = self.serializer_class(instance=groupInstance)
        return Response(serial.data)






