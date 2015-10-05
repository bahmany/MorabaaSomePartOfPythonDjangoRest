from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets
from amspApp.CompaniesManagment.Secretariat.models import Secretariat
from amspApp.CompaniesManagment.Secretariat.serializers.SecretariatsSerializers import SecretariatSerializer
from amspApp.CompaniesManagment.models import Company
from amspApp._Share.ListPagination import ListPagination


class SecretariatsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Secretariat.objects.all()
    serializer_class = SecretariatSerializer
    pagination_class = ListPagination
    # filter_backends = (filters.DjangoFilterBackend,)




    def get_queryset(self):
        companyInstance = Company.objects.get(
            id = self.kwargs["companyID_id"],
            owner_user = self.request.user.id)
        self.queryset = Secretariat.objects.filter(company = companyInstance).order_by("-id")
        return super(SecretariatsViewSet, self).get_queryset()

    def create(self, request, *args, **kwargs):

        return super(SecretariatsViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(
            id = self.kwargs["companyID_id"],
            owner_user = self.request.user.id)
        secInstance = Secretariat.objects.get(id = self.kwargs["id"])

        if secInstance.set_SecretariatPermissions.count() != 0 :
            raise Exception()

        return super(SecretariatsViewSet, self).destroy(request, *args, **kwargs)



    def template_page(self,request, *args, **kwargs):
        return render_to_response("companyManagement/Secretarait.html",{}, context_instance=RequestContext(self.request))
