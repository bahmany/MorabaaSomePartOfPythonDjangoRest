from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework_mongoengine import viewsets
from amspApp.Infrustructures.Classes.PublicFilters import QuerySetFilter
from amspApp.MyProfile.models import Profile
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from amspApp._Share.ListPagination import ListPagination


class FriendViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ListPagination

    def template_view(self, request):
        return render_to_response('friends/friends.html', {}, context_instance=RequestContext(request))


    def get_queryset(self):
        # self.create_test()

        self.queryset = QuerySetFilter().filter(
            querySet=Profile.objects,
            kwargs = self.request.query_params
        )
        return super(FriendViewSet, self).get_queryset()