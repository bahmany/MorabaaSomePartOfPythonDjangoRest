import json
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from amspApp.CompaniesManagment.Charts.models import Chart, ChartZones, ZoneItems
from amspApp.CompaniesManagment.Charts.serializers.ChartSerializers import ChartSerializer
from amspApp.CompaniesManagment.Charts.serializers.ZoneSerializers import ZoneSerializer
from amspApp.CompaniesManagment.Positions.models import PositionsDocument, Position
from amspApp.CompaniesManagment.models import Company
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter, QuerySetFilterInMysql
from amspApp.MyProfile.models import Profile
from amspApp._Share.ListPagination import ListPagination, ListPaginationSmall
from django.core.cache import caches, cache, get_cache


class ChartZoneSearchViews(generics.ListAPIView):
    lookup_field = 'id'
    model = ChartZones
    serializer_class = ZoneSerializer
    pagination_class = ListPaginationSmall
    # filter_backends = (filters.DjangoFilterBackend,)
    # my_filter_fields = ("chartName","profileName","companyName", )

    def get_queryset(self):
        self.queryset = QuerySetFilterInMysql(["title"]).filter(
            querySet=ChartZones.objects.filter(company=self.request.user.current_company),
            kwargs = self.request.query_params)
        return super(ChartZoneSearchViews, self).get_queryset()


    def list(self, request, *args, **kwargs):
        supeRes = super(ChartZoneSearchViews, self).list(request, *args, **kwargs)
        result = self.get_queryset()
        posInstance = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)

        # cacheName = 'charts_members_'+str(posInstance.id)
        # chartFromCache = cache.get(cacheName)
        # if chartFromCache!=None:
        #     return Response(chartFromCache)

        res = []
        for zone in supeRes.data["results"]:
            crt = {
                "title": zone["title"],
                "id": zone["id"],
                "members": list(ZoneItems.objects.filter(zone = zone["id"])),
            }
            res.append(crt)
        for re in res:
            re["membersInfo"] = []
            for r in re["members"]:
                positionList = list(r.chart.set_position.all())
                for userPos in positionList:
                    userPosition = PositionsDocument.objects.get(
                        userID=userPos.user_id,
                        companyID = self.request.user.current_company.id )
                    newR = {
                        'avatar': userPosition.avatar,
                        'chartID': userPosition.chartID,
                        'chartName': userPosition.chartName,
                        'companyID': userPosition.companyID,
                        'companyName': userPosition.companyName,
                        'id': str(userPosition.id),
                        'last': userPosition.last,
                        'positionID': userPosition.positionID,
                        'postDate': userPosition.postDate,
                        'profileID': userPosition.profileID,
                        'profileName': userPosition.profileName,
                        'userID': userPosition.userID,
                    }
                    re["membersInfo"].append(newR)
            re["members"] = []
        # get_cache('default')
        # cache.set(cacheName, res, 6)
        supeRes.data["results"] = res
        return supeRes



