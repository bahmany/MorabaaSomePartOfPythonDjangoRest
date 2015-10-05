from rest_framework_mongoengine import generics
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter
from amspApp.Letter.models import InboxGroup
from amspApp.Letter.serializers.InboxGroupSerializer import InboxGroupSerializer
from amspApp._Share.ListPagination import ListPagination


class MemberGroupSearchViews(generics.ListAPIView):
    lookup_field = 'id'
    model = InboxGroup
    serializer_class = InboxGroupSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        posInstance = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)
        self.queryset = QuerySetFilter().filter(
            querySet=InboxGroup.objects.filter(positionID=posInstance.id),
            kwargs=self.request.query_params
        )
        return super(MemberGroupSearchViews, self).get_queryset()

