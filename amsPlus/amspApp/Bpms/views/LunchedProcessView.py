import io
import pickle
from SpiffWorkflow.bpmn.parser.util import xpath_eval
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from rest_framework.decorators import detail_route, list_route

from rest_framework_mongoengine import viewsets as me_viewsets
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
import xml.etree.ElementTree as ET

from rest_framework import status
from amspApp.Bpms.models import LunchedProcess
from amspApp.Bpms.serializers.LunchedProcessSerializer import LunchedProcessSerializer
from amspApp.CompaniesManagment.Positions.models import Position, PositionsDocument
from amspApp.amspUser.views.UserView import UserListPagination


class LunchedProcessViewSet(me_viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = LunchedProcess.objects.all()
    serializer_class = LunchedProcessSerializer
    pagination_class = UserListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data, request=request)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
                            'message': serializer.errors,
                            'status': 'Bad request',
                        }, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['get'])
    def Inbox(self, request, *args, **kwargs):
        posistionId = PositionsDocument.objects.get(userID=request.user.id, companyID=request.user.current_company.id)
        queryset = LunchedProcess.objects.filter(thisPerformer=str(posistionId.id))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @list_route(methods=['get'])
    def MyProcess(self, request, *args, **kwargs):
        posistionId = PositionsDocument.objects.get(userID=request.user.id, companyID=request.user.current_company.id)
        queryset = LunchedProcess.objects.filter(position_id=str(posistionId.id))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def MyDoneProcess(self, request, *args, **kwargs):
        posistionId = PositionsDocument.objects.get(userID=request.user.id, companyID=request.user.current_company.id)
        queryset = LunchedProcess.objects.filter(position_id=str(posistionId.id), isComplete=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @detail_route(methods=['patch'])
    def CompleteJob(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        engineInstance=pickle.loads(instance.engineInstance)
        engineInstance.keep_going(request.data,instance.formData)
        return Response(serializer.data)


    def template_view_inbox(self, request, *args, **kwargs):
        gt_datas_title = [
            'name',
            'bpmnName',
        ]

        gt_datas_dbtitle = [
            'name',
            'bpmnName',
        ]

        gt_buttons = [
            {'type': 'primary fa fa-gear', 'func': 'doJob(obj.id)', 'is_toggle_func': 's', 'is_toggle': 0},

        ]
        serializer = self.get_serializer()
        renderer = HTMLFormRenderer()
        gm_task_create_form = renderer.render(serializer.data, renderer_context={
            'template': 'forms/LunchedProcess/CreateLunchedProcess.html',
            'request': self.request
        })
        # ali = render(request, 'forms/task/CreateTask.html',{})
        gm_task_create_buttons = [
            {'type': 'primary fa fa-save', 'func': 'saveLunchedProcess()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
        ]
        # gt_ means GenericTable
        # gm_ means GenericModal

        data = {'gm_items': [{
                                 'gm_modal_title': 'createLunchedProcess',
                                 'gm_modal_id': 'GenericModalTaskCreate.html',
                                 'gm_form': gm_task_create_form,
                                 'gm_buttons': gm_task_create_buttons}],
                'gt_table_title': 'LunchedProcessInbox',
                'gt_object_name': 'LunchedProcess',
                'gt_func_col': 'col-md-1',
                'gt_search_func': 'searchLunchedProcess()',
                'gt_create_func': 'createLunchedProcess()',
                'gt_datas_title': gt_datas_title,
                'gt_datas_dbtitle': gt_datas_dbtitle,
                'gt_buttons': gt_buttons,
                'LunchedProcess_table_template': 'generic-templates/Table.html',
                'LunchedProcess_edit_modal': 'generic-templates/Modal.html',
        }

        return render_to_response('others/LunchedProcessInbox.html', data,
                                  context_instance=RequestContext(self.request))
    def template_view_my_process(self, request, *args, **kwargs):
            gt_datas_title = [
                'name',
                'bpmnName',
            ]

            gt_datas_dbtitle = [
                'name',
                'bpmnName',
            ]

            gt_buttons = [
                {'type': 'primary fa fa-gear', 'func': 'doJob(obj.id)', 'is_toggle_func': 's', 'is_toggle': 0},

            ]
            serializer = self.get_serializer()
            renderer = HTMLFormRenderer()
            gm_task_create_form = renderer.render(serializer.data, renderer_context={
                'template': 'forms/LunchedProcess/CreateLunchedProcess.html',
                'request': self.request
            })
            # ali = render(request, 'forms/task/CreateTask.html',{})
            gm_task_create_buttons = [
                {'type': 'primary fa fa-save', 'func': 'saveLunchedProcess()', 'title': ''},
                {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
            ]
            # gt_ means GenericTable
            # gm_ means GenericModal

            data = {'gm_items': [{
                                     'gm_modal_title': 'createLunchedProcess',
                                     'gm_modal_id': 'GenericModalTaskCreate.html',
                                     'gm_form': gm_task_create_form,
                                     'gm_buttons': gm_task_create_buttons}],
                    'gt_table_title': 'MyLunchedProcess',
                    'gt_object_name': 'LunchedProcess',
                    'gt_func_col': 'col-md-1',
                    'gt_search_func': 'searchLunchedProcess()',
                    'gt_create_func': 'createLunchedProcess()',
                    'gt_datas_title': gt_datas_title,
                    'gt_datas_dbtitle': gt_datas_dbtitle,
                    'gt_buttons': gt_buttons,
                    'LunchedProcess_table_template': 'generic-templates/Table.html',
                    'LunchedProcess_edit_modal': 'generic-templates/Modal.html',
            }

            return render_to_response('others/LunchedProcessMyProcess.html', data,
                                      context_instance=RequestContext(self.request))
    def template_view_my_done_process(self, request, *args, **kwargs):
            gt_datas_title = [
                'name',
                'bpmnName',
            ]

            gt_datas_dbtitle = [
                'name',
                'bpmnName',
            ]

            gt_buttons = [
                {'type': 'primary fa fa-gear', 'func': 'doJob(obj.id)', 'is_toggle_func': 's', 'is_toggle': 0},

            ]
            serializer = self.get_serializer()
            renderer = HTMLFormRenderer()
            gm_task_create_form = renderer.render(serializer.data, renderer_context={
                'template': 'forms/LunchedProcess/CreateLunchedProcess.html',
                'request': self.request
            })
            # ali = render(request, 'forms/task/CreateTask.html',{})
            gm_task_create_buttons = [
                {'type': 'primary fa fa-save', 'func': 'saveLunchedProcess()', 'title': ''},
                {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
            ]
            # gt_ means GenericTable
            # gm_ means GenericModal

            data = {'gm_items': [{
                                     'gm_modal_title': 'createLunchedProcess',
                                     'gm_modal_id': 'GenericModalTaskCreate.html',
                                     'gm_form': gm_task_create_form,
                                     'gm_buttons': gm_task_create_buttons}],
                    'gt_table_title': 'MyDoneProcess',
                    'gt_object_name': 'LunchedProcess',
                    'gt_func_col': 'col-md-1',
                    'gt_search_func': 'searchLunchedProcess()',
                    'gt_create_func': 'createLunchedProcess()',
                    'gt_datas_title': gt_datas_title,
                    'gt_datas_dbtitle': gt_datas_dbtitle,
                    'gt_buttons': gt_buttons,
                    'LunchedProcess_table_template': 'generic-templates/Table.html',
                    'LunchedProcess_edit_modal': 'generic-templates/Modal.html',
            }

            return render_to_response('others/LunchedProcessMyDoneProcess.html', data,
                                      context_instance=RequestContext(self.request))

    def template_view_do_process(self, request, *args, **kwargs):
        return render_to_response('others/LunchedProcessDo.html', {},
                                  context_instance=RequestContext(request))