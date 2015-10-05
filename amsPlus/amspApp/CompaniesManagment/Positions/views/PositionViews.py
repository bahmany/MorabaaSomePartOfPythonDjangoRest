from rest_framework import status
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Positions.models import Position, PositionsDocument
from amspApp.CompaniesManagment.Positions.serializers import PositionSerializer
from amspApp.CompaniesManagment.Positions.serializers.PositionSerializer import PositionDocumentSerializer
from amspApp.CompaniesManagment.models import Company, CompanyMembersJointRequest
from amspApp.MyProfile.models import Profile
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from amspApp._Share.ListPagination import ListPagination
from amspApp.amspUser.models import MyUser
from django.utils.translation import ugettext as _


"""
Rules :
       1- when a position is posted no body can not change them
       2- before updating a position the remaining should be freed by company owner
       3- in the searchs members should not be appeared
       4-




"""


class PositionViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    pagination_class = ListPagination

    # security check has been remain
    # this invitation are only avalaible by the reciever user
    # but in this sprint company owner can do that
    def create(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(id=kwargs["companyID_id"])
        currentUserInstance = request.user
        invitationInstance = CompanyMembersJointRequest.objects.get(id=request.data["invitationID"])
        chartInstance = Chart.objects.get(id=invitationInstance.chart)
        # the user who is suppose to get position
        userInstance = MyUser.objects.get(id=invitationInstance.sender.userID)
        # checking if position exits
        positions = Position.objects.filter(
            company=companyInstance,
            user=userInstance
        )
        if positions.count() > 0:
            return Response(
                data={
                    "message": _("This person has an exiting position in your selected company, please drop him first ")
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # ------------------------------
        newItem={
            'chart': chartInstance,
            'user': userInstance,
            'company': companyInstance,
        }
        serializer = self.serializer_class(data=newItem)
        if serializer.is_valid():
            serializer.validated_data["chart"]=chartInstance
            serializer.validated_data["user"]=userInstance
            serializer.validated_data["company"]=companyInstance
            serializer.create(serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            invitationInstance.delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # this is for currnet company selector
    @list_route(methods=['get'])
    def CompaniesForCurrent(self, request, *args, **kwargs):
        queryset = PositionsDocument.objects.filter(userID=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PositionDocumentSerializer(page, many=True,fields=('companyID','companyName'))
            return self.get_paginated_response(serializer.data)

        serializer = PositionDocumentSerializer(queryset, many=True,fields=('companyID','companyName'))
        return Response(serializer.data)






