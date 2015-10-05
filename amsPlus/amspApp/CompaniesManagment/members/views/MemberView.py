from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_mongoengine import generics
from rest_framework_mongoengine.generics import ListCreateAPIView, ListAPIView
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Positions.models import Position, PositionsDocument
from amspApp.CompaniesManagment.members.serializers.MemberSerializer import MembersSerializer, MembersDocumentSerializer
from amspApp.CompaniesManagment.models import Company
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter
from amspApp.Letter.models import InboxGroup
from amspApp.Letter.serializers.InboxGroupSerializer import InboxGroupSerializer
from amspApp._Share.ListPagination import ListPagination
from rest_framework import filters
from amspApp.amspUser.models import MyUser

__author__ = 'mohammad'



class MemberViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    # queryset = CompanyProductions.objects.all()
    serializer_class = MembersSerializer
    pagination_class = ListPagination
    # filter_backends = (filters.DjangoFilterBackend,)




    def get_queryset(self):
        companyInstance = Company.objects.get(
            id = self.kwargs["companyID_id"],
            owner_user = self.request.user.id
            )
        self.queryset = Position.objects.filter(company = companyInstance).order_by("-id")
        return super(MemberViewSet, self).get_queryset()


    def template_page(self,request, *args, **kwargs):
        return render_to_response("companyManagement/Members.html",{}, context_instance=RequestContext(self.request))


class MemberViewSetMongo(generics.ListCreateAPIView):
    lookup_field = 'id'
    model = PositionsDocument
    serializer_class = MembersDocumentSerializer
    pagination_class = ListPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # my_filter_fields = ("chartName","profileName","companyName", )


    def get_queryset(self):
        if self.request.query_params["cid"] == "drede23fa":
            companyInstance = Company.objects.get(
                id = self.request.user.current_company_id,
                owner_user = self.request.user.id
                )
        else:
            companyInstance = Company.objects.get(
                id = int(self.request.query_params["cid"]),
                owner_user = self.request.user.id
                )

        self.queryset = QuerySetFilter().filter(
            querySet=PositionsDocument.objects.filter(companyID = companyInstance.id),
            kwargs = self.request.query_params
        )
        return super(MemberViewSetMongo, self).get_queryset()









