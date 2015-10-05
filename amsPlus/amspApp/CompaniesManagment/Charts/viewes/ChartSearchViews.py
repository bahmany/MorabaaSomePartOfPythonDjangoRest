import json
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from amspApp.CompaniesManagment.Charts.models import Chart
from amspApp.CompaniesManagment.Charts.serializers.ChartSerializers import ChartSerializer
from amspApp.CompaniesManagment.Positions.models import PositionsDocument, Position
from amspApp.CompaniesManagment.models import Company
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter, QuerySetFilterInMysql
from amspApp.MyProfile.models import Profile
from amspApp._Share.ListPagination import ListPagination, ListPaginationSmall
from django.core.cache import caches, cache, get_cache


class ChartSearchViews(generics.ListAPIView):
    lookup_field = 'id'
    model = Chart
    serializer_class = ChartSerializer
    pagination_class = ListPaginationSmall
    # filter_backends = (filters.DjangoFilterBackend,)
    # my_filter_fields = ("chartName","profileName","companyName", )

    def get_queryset(self):
        self.queryset = QuerySetFilterInMysql(["title"]).filter(
            querySet=Chart.objects.filter(owner=self.request.user.current_company),
            kwargs = self.request.query_params)
        return super(ChartSearchViews, self).get_queryset()


    def list(self, request, *args, **kwargs):
        supeRes = super(ChartSearchViews, self).list(request, *args, **kwargs)
        result = self.get_queryset()
        posInstance = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)

        # cacheName = 'charts_members_'+str(posInstance.id)
        # chartFromCache = cache.get(cacheName)
        # if chartFromCache!=None:
        #     return Response(chartFromCache)

        res = []
        for chart in supeRes.data["results"]:
            crt = {
                "title": chart["title"],
                "id": chart["id"],
                "members": list(PositionsDocument.objects.filter(chartID = chart["id"])),
                "parentid": chart["top"],
            }
            res.append(crt)
        for re in res:
            re["membersInfo"] = []
            for r in re["members"]:
                userPosition = PositionsDocument.objects.get(
                    userID=r.userID,
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



