import io
from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import Q
from rest_framework_mongoengine import viewsets as me_viewsets
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
import xml.etree.ElementTree as ET

from rest_framework import status
from amspApp.CompaniesManagment.Processes.models import Bpmn
from amspApp.CompaniesManagment.Processes.serializers.BpmnSerializer import BpmnSerializer
from amspApp.amspUser.views.UserView import UserListPagination
from amspApp.Bpms.Validator import Validator


class BpmnViewSet(me_viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Bpmn.objects.all()
    serializer_class = BpmnSerializer
    pagination_class = UserListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def get_queryset(self):
        query = self.request.GET.get('query')
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = Bpmn.objects.filter(Q(name__icontains=search_text) |
                                           Q(description__icontains=search_text)
            )
        else:
            queryset = Bpmn.objects.all()
        queryset = queryset.filter(company_id=int(self.kwargs["companyID_id"]))
        return queryset

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            bpmn = serializer.validated_data['xml']
            bpmn = ET.parse(io.StringIO(bpmn))
            validator = Validator(bpmn)
            if (len(validator.validate_diagram()) == 0):
                serializer.validated_data['is_valid_form'] = True
            else:
                serializer.validated_data['is_valid_form'] = False

            serializer.create(serializer.validated_data, request=request)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
                            'message': serializer.errors,
                            'status': 'Bad request',
                        }, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        bpmn = serializer.validated_data['xml']
        bpmn = ET.parse(io.StringIO(bpmn))
        validator = Validator(bpmn)
        if (len(validator.validate_diagram()) == 0):
            serializer.validated_data['is_valid_form'] = True
        else:
            serializer.validated_data['is_valid_form'] = False

        self.perform_update(serializer)
        return Response(serializer.data)

    def template_view_new(self, request, *args, **kwargs):

        return render_to_response('companyManagement/newbpmn.html', {},
                                  context_instance=RequestContext(self.request))

    def template_view_setup(self, request, *args, **kwargs):

        return render_to_response('companyManagement/SetupBpmnElements.html', {},
                                  context_instance=RequestContext(self.request))

    def template_view(self, request, *args, **kwargs):
        gt_datas_title = [
            'name',
            'description',
        ]

        gt_datas_dbtitle = [
            'name',
            'description',
        ]

        gt_buttons = [
            {'type': 'primary fa fa-edit', 'func': 'bpmnEdit(obj.id)', 'is_toggle_func': 's', 'is_toggle': 0},
            {'type': 'primary fa fa-file-text', 'type2': ' disabled fa fa-lock', 'is_toggle_func': 'is_valid_form',
             'func': 'buildForm(obj.id)', 'title': '',
             'is_toggle': 1},
            {'type': 'danger fa fa-trash', 'func': 'bpmnDelete(obj.id)', 'is_toggle_func': 's', 'is_toggle': 0}

        ]

        gm_aresure_buttons = [
            {'type': 'success fa fa-check', 'func': 'yes()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'no()', 'title': ''},
        ]



        # gt_ means GenericTable
        # gm_ means GenericModal

        data = {'gm_items': [
            {
                'gm_modal_title': 'areyuosure',
                'gm_modal_id': 'GenericModalAreYouSure.html',
                'gm_form': 'areusure',
                'gm_buttons': gm_aresure_buttons},
            {
                'gm_modal_title': 'forbiden',
                'gm_modal_id': 'GenericModalPermissionDenied.html',
                'gm_form': 'permissiondenied',
                'gm_buttons': [{'type': 'success fa fa-check', 'func': 'ok()', 'title': ''}]}],
                'gt_table_title': 'bpmnlist',
                'gt_object_name': 'bpmn',
                'gt_func_col': 'col-md-2',
                'gt_search_func': 'searchBpmn()',
                'gt_create_func': 'createBpmn()',
                'gt_datas_title': gt_datas_title,
                'gt_datas_dbtitle': gt_datas_dbtitle,
                'gt_buttons': gt_buttons,
                'bpmn_table_template': 'generic-templates/Table.html',
                'bpmn_edit_modal': 'generic-templates/Modal.html',
        }

        return render_to_response('companyManagement/BpmnsTable.html', data,
                                  context_instance=RequestContext(self.request))
