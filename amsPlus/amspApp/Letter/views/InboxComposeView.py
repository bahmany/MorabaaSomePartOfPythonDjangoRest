from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import QuerySet
from rest_framework.decorators import list_route
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.CompaniesManagment import Positions
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder
from rest_framework import status
from amspApp.Letter.serializers.InboxFolderSerializer import InboxFolderSerializer
from amspApp._Share.ListPagination import ListPagination


class InboxComposeViewSet(viewsets.ModelViewSet):
    pagination_class = ListPagination
    lookup_field = "id"
    serializer_class = InboxFolderSerializer
    queryset = InboxFolder.objects.all()


    def template_view(self, request, *args, **kwargs):
        return render_to_response(
            "letter/Compose/InboxCompose.html",
            {},
            context_instance=RequestContext(request)
        )
