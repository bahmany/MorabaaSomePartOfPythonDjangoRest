from datetime import datetime
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.CompaniesManagment.Positions.serializers.PositionSerializer import PositionSerializer
from amspApp.CompaniesManagment.members.serializers.MemberSerializer import MembersSerializer
from amspApp.CompaniesManagment.models import CompanyMembersJointRequest, Company
from amspApp.CompaniesManagment.serializers.CompanyMembersJointRequestSerializers import \
    CompanyMembersJointRequestSerializer
from amspApp.MyProfile.models import Profile
from amspApp._Share.ListPagination import ListPagination
from amspApp.amspUser.models import MyUser
from django.utils.translation import ugettext_lazy as _

__author__ = 'mohammad'


class CompanyMembersJointRequestViewset(viewsets.ModelViewSet):
    lookup_field = "id"
    # currentUsername = None
    queryset = CompanyMembersJointRequest.objects.all()
    serializer_class = CompanyMembersJointRequestSerializer
    pagination_class = ListPagination

    """
    there is two types of invitation accept

    1: is to approve invitation by CEO
    2: approve invitation by reciever

    """

    @list_route(methods=['post'])
    def DoInvite(self, request, *args, **kwargs):
        currentUserInstance = request.user
        # checking if current is user is CEO or reciever
        invitationInstance = self.queryset.get(id=request.data['invitationID'])
        chartInstance = Chart.objects.get(id=invitationInstance.chart)
        companyInstance = Company.objects.get(id=invitationInstance.company)
        recieverProfileInstance = invitationInstance.receiver
        senderProfileInstance = invitationInstance.sender
        recieverUserInstance = MyUser.objects.get(id=recieverProfileInstance.userID)
        senderUserInstance = MyUser.objects.get(id=senderProfileInstance.userID)

        isCurrentUserApproveAsReciever = recieverUserInstance == currentUserInstance
        isCurrentUserApproveAsCEO = senderUserInstance == currentUserInstance

        if not isCurrentUserApproveAsCEO and not isCurrentUserApproveAsReciever:
            return Response({"message": _("You are not allowed to perform this operation")},
                            status=status.HTTP_401_UNAUTHORIZED)

        # partial update is here
        # it means we have to update an position
        if invitationInstance.isEmpty:
            positionInstance = Position.objects.get(id=invitationInstance.positionID)
            updated = {
                "user": recieverUserInstance.id,
                "post_date": datetime.now()
            }
            posSerializer = MembersSerializer(instance=positionInstance, data=updated, partial=True)
            posSerializer.is_valid(raise_exception=True)
            posSerializer.update(instance=positionInstance, validated_data=posSerializer.validated_data)
            invitationInstance.delete()
            return Response({}, status=status.HTTP_200_OK)

        newMember = {
            "company": companyInstance.id,
            "chart": chartInstance.id,
            "user": recieverUserInstance.id
        }
        posSerializer = MembersSerializer(data=newMember)
        posSerializer.is_valid(raise_exception=True)
        posSerializer.create(posSerializer.validated_data)
        invitationInstance.delete()
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        CompanyMembersJointRequest.objects.filter(
            company=kwargs["companyID_id"],
            chart=request.data['chart']
        ).delete()
        if request.data["selected"] == False:
            return Response({})
        request.data["sender"] = str(Profile.objects.get(userID=request.user.id).id)
        return super(CompanyMembersJointRequestViewset, self).create(request, *args, **kwargs)










