from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import QuerySet
from rest_framework.decorators import list_route
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.CompaniesManagment import Positions
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder, InboxLabel
from rest_framework import status
from amspApp.Letter.serializers.InboxFolderSerializer import InboxFolderSerializer
from amspApp.Letter.serializers.InboxLabelSerializer import InboxLabelSerializer
from amspApp._Share.ListPagination import ListPagination


class InboxLabelViewset(viewsets.ModelViewSet):
    pagination_class = ListPagination
    lookup_field = "id"
    serializer_class = InboxLabelSerializer


    def get_queryset(self):
        pos = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)

        self.queryset = InboxLabel.objects.filter(positionID=pos.id)
        return super(InboxLabelViewset, self).get_queryset()
    def create(self, request, *args, **kwargs):
        request.data["companyID"] = self.request.user.current_company.id
        pos = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)
        request.data["positionID"] = pos.id
        return super(InboxLabelViewset, self).create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        request.data["companyID"] = self.request.user.current_company.id
        pos = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)
        request.data["positionID"] = pos.id
        return super(InboxLabelViewset, self).update(request, *args, **kwargs)


