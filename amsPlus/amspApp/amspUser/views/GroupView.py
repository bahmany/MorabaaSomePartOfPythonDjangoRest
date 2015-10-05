import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets, permissions, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from amspApp.amspUser.models import MyUser
from amspApp.amspUser.permissions.UserPermissions import IsAccountOwner
from amspApp.amspUser.serializers.UserGroupSerializer import UserGroupSerializer
from amspApp.amspUser.serializers.UserSerializer import UserSerializer
from rest_framework import status
from amspApp.amspUser.views.UserView import UserListPagination


class GroupViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = UserGroupSerializer
    pagination_class = UserListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def get_queryset(self):
        query = self.request.GET.get('query')
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = Group.objects.filter(Q(name__contains=search_text))
        else:
            queryset = Group.objects.all()
        return queryset

    def template_view(self, request, *args, **kwargs):
        gt_datas_title = [
            'id',
            'name',
        ]
        gt_datas_dbtitle = [
            'id',
            'name',
        ]
        gt_buttons = [
            {'type': 'primary fa fa-edit', 'func': 'groupEdit(obj.name)', 'title': '', 'is_toggle': 0},
            {'type': 'danger fa fa-trash', 'func': 'groupDelete(obj.name)', 'title': '', 'is_toggle': 0},
        ]

        gm_group_buttons = [
            {'type': 'success fa fa-save', 'func': 'saveGroupEdit(obj.name)', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
        ]
        gm_group_create_buttons = [
            {'type': 'primary fa fa-save', 'func': 'saveGroup()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
        ]
        serializer = self.get_serializer()
        renderer = HTMLFormRenderer()
        gm_group_form = renderer.render(serializer.data, renderer_context={
            'template': 'forms/amsp-user/EditGroup.html',
            'request': self.request
        })
        gm_group_create_form = renderer.render(serializer.data, renderer_context={
            'template': 'forms/amsp-user/CreateGroup.html',
            'request': self.request
        })
        gm_aresure_buttons = [
            {'type': 'success fa fa-check', 'func': 'yes()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'no()', 'title': ''},
        ]

        # gt_ means GenericTable
        # gm_ means GenericModal

        data = {'gm_items': [{
                                 'gm_modal_title': 'editgroup',
                                 'gm_modal_id': 'GenericModalGroupEdit.html',
                                 'gm_form': gm_group_form,
                                 'gm_buttons': gm_group_buttons},
                             {
                                 'gm_modal_title': 'creategroup',
                                 'gm_modal_id': 'GenericModalGroupCreate.html',
                                 'gm_form': gm_group_create_form,
                                 'gm_buttons': gm_group_create_buttons}, {
                                 'gm_modal_title': 'areyuosure',
                                 'gm_modal_id': 'GenericModalAreYouSure.html',
                                 'gm_form': 'areusure',
                                 'gm_buttons': gm_aresure_buttons},{
                                 'gm_modal_title': 'forbiden',
                                 'gm_modal_id': 'GenericModalPermissionDenied.html',
                                 'gm_form': 'permissiondenied',
                                 'gm_buttons': [{'type': 'success fa fa-check', 'func': 'ok()', 'title': ''}]} ],
                'gt_table_title': 'grouplist',
                'gt_object_name': 'group',
                'gt_func_col': 'col-md-1',
                'gt_search_func': 'searchGroup()',
                'gt_create_func': 'createGroup()',
                'gt_datas_title': gt_datas_title,
                'gt_datas_dbtitle': gt_datas_dbtitle,
                'gt_buttons': gt_buttons,
                'group_table_template': 'ani-theme/generic-templates/Table.html',
                'group_edit_modal': 'ani-theme/generic-templates/Modal.html',
        }
        return render_to_response('amsp-user/GroupsTable.html', data,
                                  context_instance=RequestContext(self.request))