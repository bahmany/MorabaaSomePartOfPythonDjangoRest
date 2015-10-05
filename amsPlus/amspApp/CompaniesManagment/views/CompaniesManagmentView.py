from django.db.models import Q
from django.http.request import QueryDict
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.models import Company
from amspApp.CompaniesManagment.permissions.CompanyPermissions import CanCruid
from amspApp.CompaniesManagment.serializers.CompanySerializers import CompanySerializer
from amspApp.MyProfile.models import Profile
from amspApp._Share.ListPagination import ListPagination
from amspApp.amspUser.models import MyUser
from rest_framework import status


__author__ = 'mohammad'


class CompaniesManagmentViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    # currentUsername = None
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination

    # pagination_class = ListPagination
    # renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)
    # permission_classes = CanCruid




    def get_queryset(self):
        query = self.request.GET.get('query')
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = Company.objects.filter(
                Q(name__contains=search_text) &
                Q(owner_user=self.request.user.id))
        else:
            queryset = Company.objects.filter(owner_user=self.request.user.id)
        queryset.order_by("-post_date")
        return queryset


    def create(self, request, *args, **kwargs):
        data = dict(request.data.iterlists()) if type(request.data) == QueryDict else request.data
        data["owner_user"] = request.user.id
        # data["details"] = {}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            result = serializer.create(serializer.validated_data)
            return Response({
                                "name": result.name,
                                "id": result.id
                            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors
                        , status=status.HTTP_400_BAD_REQUEST)

    def template_page(self,request):
        return render_to_response(
            "companyManagement/CompaniesManagment.html",
            {'currentCompanyName':request.user.current_company.name},
            context_instance=RequestContext(self.request))

    def template_page_base(self,request):
        return render_to_response(
            "companyManagement/CompanyManagement.html",
            {},
            context_instance=RequestContext(self.request))

    @detail_route(methods=['post'])
    def AddMemberToWaitings(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(
            id=self.kwargs["id"],
            owner_user=request.user.id
        )
        chartInstance = Chart.objects.get(id = request.DATA["chartID"])
        profileInstance = Profile.objects.get(id = request.DATA["personID"])
        userInstance = MyUser.objects.get(id = profileInstance.userID)
        self = self
