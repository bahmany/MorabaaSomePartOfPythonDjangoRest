from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import MultipleObjectsReturned, DoesNotExist
from rest_framework.generics import get_object_or_404
from rest_framework_mongoengine import viewsets
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile
from amspApp.CompaniesManagment.CompanyProfile.serializers.CompanyProfileSerializers import CompanyProfileSerializer
from amspApp.CompaniesManagment.models import Company

__author__ = 'mohammad'


class CompanyProfileViewSet(viewsets.ModelViewSet):
    # lookup_field = 'id'
    # queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer





    """
    This method checkes if selected company has profile then return it and when has no profile
    creates it
    """
    def get_queryset(self):
        self.queryset = CompanyProfile.objects.filter(companyID = self.kwargs["companyID_id"], creatorUserID = self.request.user.id)
        if self.queryset.count() == 0:
            companyInstance = Company.objects.get(id = self.kwargs["companyID_id"])
            CompanyProfileSerializer().create_default_company_profile(self.kwargs["companyID_id"],self.request.user.id,companyInstance.name)
            self.queryset = CompanyProfile.objects.filter(companyID = self.kwargs["companyID_id"], creatorUserID = self.request.user.id)
        return self.queryset

    def template_page(self,request):
        return render_to_response('companyManagement/CompanyProfile.html', {},
                          context_instance=RequestContext(self.request))