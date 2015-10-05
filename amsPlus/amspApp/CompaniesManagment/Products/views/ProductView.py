from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import Q
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile
from amspApp.CompaniesManagment.Products.models import CompanyProductions
from amspApp.CompaniesManagment.Products.serializers.ProductSerializer import CompanyProductionSerializer
from amspApp._Share.ListPagination import ListPagination

__author__ = 'mohammad'


class CompanyProductionsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    # queryset = CompanyProductions.objects.all()
    serializer_class = CompanyProductionSerializer
    pagination_class = ListPagination


    def get_queryset(self):
        query = self.request.GET.get('query')
        # converting mysql companyID to mongo companyProfile objectID in GUID
        companyProfile = CompanyProfile.objects.get(companyID=self.kwargs["companyID_id"])
        item_per_page = self.request.GET.get('itemPerPage')
        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page
        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = CompanyProductions.objects.filter(
                Q(name__contains=search_text) &
                Q(companyProfile=companyProfile) &
                Q(authorUserID=self.request.user.id)
            ).order_by("-dateOfPost").exclude("authorUserID","companyProfile")
        else:
            queryset = CompanyProductions.objects.filter(
                Q(authorUserID=self.request.user.id) &
                Q(companyProfile=companyProfile)
            ).order_by("-dateOfPost").exclude("authorUserID","companyProfile")
        return queryset


    def template_page(self,request, *args, **kwargs):
        return render_to_response("companyManagement/CompanyProducts.html",{}, context_instance=RequestContext(self.request))







