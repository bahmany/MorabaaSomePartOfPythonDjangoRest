from django.db.models.query_utils import Q
from django.http.request import QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets, permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer
from rest_framework.response import Response
from rest_framework import status
# from amspApp.CompaniesManagment import permissions
from amspApp.CompaniesManagment.models import Company
from amspApp.CompaniesManagment.permissions.CompanyPermissions import CanCruid
from amspApp.CompaniesManagment.serializers.CompanySerializers import CompanySerializer
from amspApp._Share.ListPagination import ListPagination
from amspApp.amspUser.models import MyUser


class CompanyViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    ref_name = 'company'
    ref_namePular = 'companies'
    ref_namePularCap = 'Companies'
    ref_nameCap = 'Company'
    # currentUsername = None
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)
    permission_classes = CanCruid


    def get_permissions(self):
        # in this section we have some permissions :
        # 1: default company is not deletable
        # 2: accounts must have at least one company

        # if self.request.method in permissions.SAFE_METHODS:
        #     return (permissions.AllowAny(),)


        return (permissions.IsAuthenticated(), CanCruid())





    def create(self, request, *args, **kwargs):
        data = dict(request.data.iterlists()) if type(request.data) == QueryDict else request.data
        data["owner_user"] = request.user.id
        data["details"] = {}
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            result = serializer.create(serializer.validated_data)
            return Response({
                "name":result.name,
                "id":result.id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors
                        , status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, *args, **kwargs):
    #     to_delete = self.serializer_class(data = kwargs)
    #


    def get_queryset(self):
        query = self.request.GET.get('query')
        user = MyUser.objects.get(id = self.request.user.id)
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = Company.objects.filter(
                Q(name__contains=search_text) &
                Q(owner_user=user))
        else:
            queryset = Company.objects.filter(owner_user=user)
        # serial = self.serializer_class(queryset, many=True, context={'request':request})
        return queryset


    # def update(self, request, *args, **kwargs):
    #     self.serializer_class.update()
    #     pass
    #
    #
    #
    #
    #
    # def template_view(self, request, *args, **kwargs):
    #     # gt_ means GenericTable
    #     # gm_ means GenericModal
    #     gt_datas_title = [
    #         'name',
    #     ]
    #     gt_datas_dbtitle = [
    #         'name',
    #     ]
    #     gt_buttons = [
    #         {'type': 'primary fa fa-edit', 'func': self.ref_name + 'Edit(obj.'+self.lookup_field+')', 'title': '', 'is_toggle': 0},
    #         {'type': 'danger fa fa-trash', 'func': self.ref_name + 'Delete(obj.'+self.lookup_field+')', 'title': '', 'is_toggle': 0},
    #     ]
    #
    #     gm_group_buttons = [
    #         {'type': 'success fa fa-save', 'func': 'save' + self.ref_nameCap + 'Edit(obj.'+self.lookup_field+')', 'title': ''},
    #         {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
    #     ]
    #     gm_group_create_buttons = [
    #         {'type': 'primary fa fa-save', 'func': 'save' + self.ref_nameCap + '()', 'title': ''},
    #         {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
    #     ]
    #     serializer = self.get_serializer()
    #     renderer = HTMLFormRenderer()
    #     gm_group_form = renderer.render(serializer.data, renderer_context={
    #         'template': 'forms/' + self.ref_nameCap + '/Edit' + self.ref_nameCap + '.html',
    #         'request': self.request
    #     })
    #     gm_group_create_form = renderer.render(serializer.data, renderer_context={
    #         'template': 'forms/' + self.ref_nameCap + '/Create' + self.ref_nameCap + '.html',
    #         'request': self.request
    #     })
    #     gm_aresure_buttons = [
    #         {'type': 'success fa fa-check', 'func': 'yes()', 'title': ''},
    #         {'type': 'danger fa fa-times', 'func': 'no()', 'title': ''},
    #     ]
    #
    #     data = {'gm_items': [{
    #                              'gm_modal_title': 'edit' + self.ref_name,
    #                              'gm_modal_id': 'GenericModal' + self.ref_nameCap + 'Post.html',
    #                              'gm_form': gm_group_form,
    #                              'gm_buttons': gm_group_buttons},
    #                          {
    #                              'gm_modal_title': 'create' + self.ref_name,
    #                              'gm_modal_id': 'GenericModal' + self.ref_nameCap + 'Post.html',
    #                              'gm_form': gm_group_create_form,
    #                              'gm_buttons': gm_group_create_buttons}, {
    #                              'gm_modal_title': 'areyuosure',
    #                              'gm_modal_id': 'GenericModalAreYouSure.html',
    #                              'gm_form': 'areusure',
    #                              'gm_buttons': gm_aresure_buttons}, {
    #                              'gm_modal_title': 'forbiden',
    #                              'gm_modal_id': 'GenericModalPermissionDenied.html',
    #                              'gm_form': 'permissiondenied',
    #                              'gm_buttons': [{'type': 'success fa fa-check', 'func': 'ok()', 'title': ''}]}],
    #             'gt_table_title': self.ref_name + 'list',
    #             'gt_object_name': self.ref_name,
    #             'gt_object_name_capital': self.ref_nameCap,
    #             'gt_object_name_pular': self.ref_namePular,
    #             'gt_object_name_pular_capital': self.ref_namePularCap,
    #             'gt_func_col': 'col-md-1',
    #             'gt_search_func': 'search' + self.ref_nameCap + '()',
    #             'gt_create_func': 'create' + self.ref_nameCap + '()',
    #             'gt_datas_title': gt_datas_title,
    #             'gt_datas_dbtitle': gt_datas_dbtitle,
    #             'gt_buttons': gt_buttons,
    #             'table_template': 'ani-theme/generic-templates/Table.html',
    #             'edit_modal': 'ani-theme/generic-templates/Modal.html',
    #
    #     }
    #
    #     return render_to_response(
    #         "ani-theme/views/pages/dashboard/../../../templates/companyManagement/CompaniesTable.html",
    #         data,
    #         context_instance=RequestContext(self.request)
    #     )
