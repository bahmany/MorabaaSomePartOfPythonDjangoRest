from bson import ObjectId
from datetime import datetime
import collections
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Charts.serializers.ChartSerializers import ChartSerializer
from amspApp.CompaniesManagment.CompanyProfile.models import CompanyProfile
from amspApp.CompaniesManagment.Positions.models import Position,PositionsDocument
from amspApp.CompaniesManagment.Positions.serializers.PositionSerializer import PositionSerializer,PositionDocumentSerializer
from amspApp.CompaniesManagment.Secretariat.models import Secretariat, SecretariatPermissions
from amspApp.CompaniesManagment.Secretariat.serializers.SecretariatsSerializers import SecretariatSerializer, \
    SecretariatSerializerPermission
from amspApp.CompaniesManagment.members.serializers.MemberSerializer import MembersSerializer
from amspApp.CompaniesManagment.models import Company
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter
from amspApp.MyProfile.models import Profile
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from amspApp._Share.ListPagination import ListPagination
from django.utils.translation import ugettext_lazy as _
from amspApp.amspUser.models import MyUser


class ChartViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    serializer_class = ChartSerializer
    queryset = Chart.objects.all()
    pagination_class = ListPagination


    def get_queryset(self):
        companyInstance = Company.objects.get(id=self.kwargs["companyID_id"])
        self.queryset = Chart.objects.filter(owner=companyInstance)
        # if self.queryset.count() == 0:
        #     self.serializer_class().create_default_chart(companyInstance)
        #     self.queryset = Chart.objects.filter(owner=companyInstance)
        return self.queryset


    def destroy(self, request, *args, **kwargs):
        instance = Chart.objects.get(
            id=kwargs["id"],
            owner=Company.objects.get(id=kwargs["companyID_id"], owner_user=request.user.id)
        )
        if (Chart.objects.all().filter(top=instance).count() > 0):
            return Response(status=status.HTTP_403_FORBIDDEN)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def template_page(self, request, *args, **kwargs):
        return render_to_response("companyManagement/CompanyChart.html", {},
                                  context_instance=RequestContext(self.request))


    def list(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(id=self.kwargs["companyID_id"])
        queryset = Chart.objects.all().filter(owner=companyInstance)
        if "q" in request.query_params:
            if request.query_params["q"] != "":
                queryset = queryset.filter(title__contains=request.query_params["q"])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, fields=('id', 'title'))
        return Response(serializer.data)


    @list_route(methods=['get'])
    def jsonRecursiveChart(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(id=self.kwargs["companyID_id"])
        return Response(self.serializer_class().get_json_chart(companyInstance))


    @detail_route(methods=['post'])
    def ChangeLevel(self, request, *args, **kwargs):
        # here i have to check if the person is owner of company or not
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )
        chartItemInstance = Chart.objects.get(
            id=kwargs["id"],
            owner=companyInstance
        )
        chartItemInstance.top = Chart.objects.get(id=request.DATA["parentId"])
        chartItemInstance.save()
        res = self.serializer_class(instance=chartItemInstance)
        return Response(res.data)


    @detail_route(methods=['post'])
    def AddNewChart(self, request, *args, **kwargs):
        # here i have to check if the person is owner of company or not
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id

        )
        chartItemInstance = Chart.objects.get(
            id=kwargs["id"],
            owner=companyInstance
        )
        newChart = self.serializer_class(data={

            "title": request.DATA["name"],
            "top": chartItemInstance.id,
            "owner": companyInstance.id
        })

        if newChart.is_valid():
            newChart.save()
            return Response(newChart.data)


    @detail_route(methods=['post'])
    def ChangeChartName(self, request, *args, **kwargs):
        # here i have to check if the person is owner of company or not
        if len(request.data["name"]) < 1:
            return Response(
                {
                    "status": "Bad request",
                    "message": [{"name": _("PositionName"), "message": _("This field is required")}]},
                status.HTTP_400_BAD_REQUEST
            )
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id

        )
        chartItemInstance = Chart.objects.get(
            id=kwargs["id"],
            owner=companyInstance
        )

        chartItemInstance.title = request.DATA["name"]
        chartItemInstance.save()

        res = self.serializer_class(instance=chartItemInstance)

        return Response(res.data)

    @detail_route(methods=["post"])
    def UpdatePost(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )

        userInstance = MyUser.objects.get(id=request.data['UserID'])

        positionInstance = Position.objects.filter(
            company=companyInstance,
            user=userInstance,
        )

        if positionInstance.count() == 0:
            chart = Chart.objects.get(id=request.data["NewPositionID"])
            newPosition = {
                "chart": chart,
                "user": userInstance,
                "company": companyInstance,
                "post_date": datetime.now()
            }
            created = MembersSerializer().create(newPosition)
            return Response(created.data)
        positionInstance = Position.objects.get(
            company=companyInstance,
            user=userInstance,
        )
        newChartInstance = Chart.objects.get(
            owner=companyInstance,
            id=request.data['NewPositionID']
        )

        positionInstance.chart = newChartInstance
        updatingPos = MembersSerializer(instance=positionInstance, data={
            "chart": newChartInstance.id,
            "user": userInstance.id,
            "company": companyInstance.id,
            "post_date": datetime.now()

        }, partial=True)

        if updatingPos.is_valid():
            updatingPos.save()

            return Response({})


    """
    here i have to update 2 places
    1: my sql
    2: mongo
    i have to say both of them to empty user id !!! :))
    """

    @detail_route(methods=["post"])
    def ForceOut(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )
        mySqlPositionInstance = Position.objects.get(
            id = request.data["positionID"]
        )
        updating = {
            "user": None
        }

        memSerial = MembersSerializer(instance=mySqlPositionInstance, data=updating, partial=True)
        memSerial.is_valid(raise_exception=True)
        memSerial.update(instance=mySqlPositionInstance, validated_data=memSerial.validated_data)

        return Response({})

    @detail_route(methods=["post"])
    def RemoveFromInbox(self, request, *args, **kwargs):
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )
        mySqlPositionInstance = Position.objects.get(
            chart=request.data["chartID"],
            company=companyInstance.id,
            user=request.data["userID"],
        )
        updating = {
            "chart": None,
            "company":None
        }
        serial = MembersSerializer(instance=mySqlPositionInstance, data=updating, partial=True)
        serial.is_valid(raise_exception=True)
        serial.update(mySqlPositionInstance, updating)
        return Response({})





    """
    This method gets long time :
    1- it gets the sec
    2- then checked sec permissions
    3- if sec has no perm then created it with all sec and then make the first one default
    4- if a chart has no default it sets the first one as default sec
    5- then return list of sec permissions
    """

    @detail_route(methods=["get"])
    def getSecWithChartPerm(self, request, *args, **kwargs):
        # getting secs
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )
        result = {}
        """
        byte[0] = Access to current dabir
        byte[1] = Access to current sadere
        byte[2] = Access to current varede
        """
        chartInstance = Chart.objects.get(
            owner=companyInstance,
            id=kwargs['id']
        )

        def findSadereInPerm(DabirID, items):
            for item in items:
                if item.secretariat_id == DabirID:
                    if item.permission == "":
                        return [
                            False,
                            False,
                            False
                        ]
                    else:
                        return [
                            True if item.permission[0] == "1" else False,
                            True if item.permission[1] == "1" else False,
                            True if item.permission[2] == "1" else False
                        ]
                    return item.permission
            return [
                False,
                False,
                False
            ]

        dabirList = Secretariat.objects.all().filter(company=companyInstance).order_by("id")
        permissionList = SecretariatPermissions.objects.all().filter(chart=chartInstance)
        dabirList = list(dabirList)
        dabirListDict = dabirList
        permissionList = list(permissionList)
        dabirListDict = [
            {"Name": x.name,
             "Id": x.id,
             "perm": findSadereInPerm(x.id, permissionList)} for x in dabirList
        ]
        defaultID = 0
        # detect that there is no dabir permission for the following chart
        # must creates for this
        if len(permissionList) == 0:
            for dl in dabirList:
                new = {
                    "chart": chartInstance,
                    "secretariat": dl,
                    "permission": "000",
                    "default": False,
                }
                newSer = SecretariatSerializerPermission().create(new)
                return self.getSecWithChartPerm(request, *args, **kwargs)
        for p in permissionList:
            defaultID = p.secretariat_id if p.default else 0
            if defaultID != 0:
                break;
        if defaultID == 0:
            permissionList[0].default = True
            permissionList[0].save()
            return self.getSecWithChartPerm(request, *args, **kwargs)
        for d in dabirListDict:
            if d["Id"] == defaultID:
                d["default"] = True
            else:
                d["default"] = False
        return Response(dabirListDict)

    @detail_route(methods=["post"])
    def updateSecPerm(self, request, *args, **kwargs):
        data = request.data
        companyInstance = Company.objects.get(
            id=self.kwargs["companyID_id"],
            owner_user=request.user.id
        )
        chartInstance = Chart.objects.get(
            owner=companyInstance,
            id=kwargs['id']
        )
        secInstance = Secretariat.objects.get(id=data["Id"])

        # check if has permission before or not ??

        countOf = SecretariatPermissions.objects.filter(chart=chartInstance, secretariat=secInstance).count()
        if countOf == 0:
            SecretariatSerializerPermission().create({
                "chart": chartInstance,
                "secretariat": secInstance,
                "permission": "000",
                "default": False,
            })
            return self.updateSecPerm(request, *args, **kwargs)

        permissionInstace = SecretariatPermissions.objects.get(chart=chartInstance, secretariat=secInstance)
        if data['default']:
            SecretariatPermissions.objects.filter(chart=chartInstance).update(default=False)
            permissionInstace.default = True
        permissionInstace.permission = "".join(map(str, map(int, data["perm"])))
        permissionInstace.save()
        return Response({})


    @list_route(methods=["get"])
    def GetAllCharts(self, request, *args, **kwargs):
        allCompanyInstance = Company.objects.filter(owner_user=request.user.id)
        allChartsInstance = Chart.objects.filter(owner__in=allCompanyInstance)
        queryset = allChartsInstance.filter(
            (
                Q(owner__name__icontains = request.query_params["q"]) |
                Q(title__icontains = request.query_params["q"])
            ) &
            (
                ~Q(top_id = None)
            )
        )
        page = self.paginate_queryset(queryset)

        # now getting empty positions
        emptyPositions = Position.objects.filter(
            Q(company__icontains = allCompanyInstance)
            &
            Q(user = None)
        )
        rendered = [collections.OrderedDict({
            "CompanyID":x.company_id,
            "CompanyName":x.company.name,
            "id":x.chart_id,
            "title":x.chart.title,
            "isEmpty":True,
            "positionID":x.id
        }) for x in emptyPositions]


        if page is not None:
            serializer = self.get_serializer(page, many=True, fields=('CompanyID',"id","CompanyName","title"))
            dt = serializer.data
            finalList = rendered + dt
            result = self.get_paginated_response(finalList)
            return result

        # serializer = self.get_serializer(queryset, many=True, fields=('CompanyID',"id","CompanyName","title"))
        # return Response(serializer.data)
        # serializer = self.get_serializer(queryset, many=True, fields=('CompanyID',"id","CompanyName","title"))
        return Response({})
    
    @detail_route(methods=['get'])
    def PositionsList(self, request, *args, **kwargs):
        queryset = PositionsDocument.objects.filter(chartID=kwargs["id"],companyID=kwargs["companyID_id"])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PositionDocumentSerializer(page, many=True, fields=('id', 'profileName'))
            return self.get_paginated_response(serializer.data)

        serializer = PositionDocumentSerializer(queryset, many=True, fields=('id', 'profileName'))
        return Response(serializer.data)

