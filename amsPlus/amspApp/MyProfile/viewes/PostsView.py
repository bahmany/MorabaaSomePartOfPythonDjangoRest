from mongoengine import QuerySet
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.MyProfile.models import Posts, Profile
from amspApp.MyProfile.serializers.PostSerializers import PostsSerializer
from amspApp.MyProfile.serializers.ProfileSerializer import ProfileSerializer
from rest_framework import status
from amspApp._Share.ListPagination import ListPagination


class PostsViewset(viewsets.ModelViewSet):

    pagination_class = ListPagination
    lookup_field = "id"
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('query')
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page
        try:
            currentProfile = Profile.objects.get(userID = self.request.user.id)
            queryset = Posts.objects.filter(profile = currentProfile).order_by("-dateOfPost")
            return queryset
        except:
            return []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            newPost=serializer.create(serializer.validated_data,request=request)
            return Response({
            "id":str(newPost.pk)},
             status=status.HTTP_201_CREATED)
        return Response({
                            'status': 'Bad request',
                            'message': serializer.errors,
                        }, status=status.HTTP_400_BAD_REQUEST)




