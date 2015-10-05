# coding=utf-8

from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from mongoengine import ValidationError
from rest_framework import status
from rest_framework.decorators import list_route, detail_route
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.models import CompanyMembersJointRequest, Company
from amspApp.CompaniesManagment.serializers.CompanyMembersJointRequestSerializers import \
    CompanyMembersJointRequestSerializer
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter
from amspApp.MyProfile.models import Profile, Posts
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from django.utils.translation import ugettext_lazy as _
from mongoengine.django.shortcuts import get_document_or_404
from amspApp._Share.ListPagination import ListPagination

__author__ = 'mohammad'


class ProfileManagmentViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ListPagination

    def get_object(self):
        try:
            obj = Profile.objects.get(userID=self.request.user.pk)
        except(Profile.DoesNotExist, ValidationError):
            obj = ProfileSerializer().create_default_profile(self.request.user)
        # self.check_object_permissions(self.request, obj)
        return obj









    # def GetAvatar(self, request):
    #     try:
    #         profile = MyProfile.objects.get(userID=request.user.pk)
    #         profilePic = profile["extra"]["profileAvatar"]["url"]
    #         return Response({"addr": profilePic})
    #     except(MyProfile.DoesNotExist, ValidationError):
    #         return Response({
    #             "addr": "/static/ani-theme/images/flat-avatar.png"
    #         })
    #

    def template_view(self, request, *args, **kwargs):
        data = {
            "YearOfJoint":request.user.date_joined.year
        }
        return render_to_response(
            "myProfile/PersonProfile.html",
            data,
            context_instance=RequestContext(self.request)
        )

    def list(self, request, *args, **kwargs):
        return Response({})

    @list_route(methods=['get'])
    def SearchProfiles(self,request, *args, **kwargs):
        self.queryset = QuerySetFilter().filter(
            querySet=Profile.objects,
            kwargs = self.request.query_params
        )

        # queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            jsonresult = serializer.data
            jsonresult = [
                {
                    "id":i["id"],
                    "Name":i["extra"]["Name"],
                    "AboutDetail":i["extra"]["AboutMe"]["detail"],
                    "AboutTitle":i["extra"]["AboutMe"]["title"],
                    "AvatarUrl":i["extra"]["profileAvatar"]["url"],
                    }

                for i in jsonresult]
        return self.get_paginated_response(jsonresult)

    # @detail_route(methods=['get'])
    # def SearchProfiles(self,request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    @detail_route(methods=['get'])
    def GetUserInvitations(self, request, *args, **kwargs):
        if kwargs["id"] == "undefined":
            return Response({"results":[]})

        senderUserProfileInstance = Profile.objects.get(userID = request.user.pk)
        recieverUserProfileInstance = Profile.objects.get(id = kwargs["id"])
        # it must shows invitations of logined user
        queryset = CompanyMembersJointRequest.objects.filter(
            receiver = recieverUserProfileInstance,
            sender = senderUserProfileInstance
        ).order_by("-dateOfPost")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CompanyMembersJointRequestSerializer(page, many=True)
            jsonResult = []
            for j in serializer.data:
                j["companyName"] = Company.objects.get(id = j["company"]).name
                j["chartName"] = Chart.objects.get(id = j["chart"]).title
                j.pop("company", None)
                j.pop("receiverName", None)
                j.pop("senderName", None)
                jsonResult.append(j)

            return self.get_paginated_response(jsonResult)

        serializer = CompanyMembersJointRequestSerializer(queryset, many=True)
        return Response(serializer.data)




    @detail_route(methods=['get'])
    def RemoveInvitations(self, request, *args, **kwargs):
        senderUserProfileInstance = Profile.objects.get(userID = request.user.pk)
        CompanyMembersJointRequest.objects(id = request.QUERY_PARAMS["q"],sender = str(senderUserProfileInstance.id)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


