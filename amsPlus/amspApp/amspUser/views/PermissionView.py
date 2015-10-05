import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets, permissions, views
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from amspApp.amspUser.models import MyUser
from amspApp.amspUser.permissions.UserPermissions import IsAccountOwner
from amspApp.amspUser.serializers.PermissionsSerializer import PermissionsSerializer
from amspApp.amspUser.serializers.UserGroupSerializer import UserGroupSerializer
from amspApp.amspUser.serializers.UserSerializer import UserSerializer
from rest_framework import status



class PermissionViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Permission.objects.all()
    serializer_class = PermissionsSerializer
    # pagination_class = UserListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = Permission.objects.filter(Q(name__contains=search_text))[:50]
        else:
            queryset = Permission.objects.all()[:50]
        return queryset

