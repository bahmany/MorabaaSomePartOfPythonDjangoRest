from django.shortcuts import render_to_response
from django.template import RequestContext
from mongoengine import QuerySet
from rest_framework.decorators import list_route
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from amspApp.CompaniesManagment import Positions
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder
from rest_framework import status
from amspApp.Letter.serializers.InboxFolderSerializer import InboxFolderSerializer
from amspApp._Share.ListPagination import ListPagination


class InboxFolderViewset(viewsets.ModelViewSet):

    # pagination_class = ListPagination
    lookup_field = "id"
    serializer_class = InboxFolderSerializer


    def template_view(self, request, *args, **kwargs):

        return render_to_response(
            "letter/InboxSidebar.html",
            {},
            context_instance=RequestContext(self.request)
        )
    def get_queryset(self):
        pos = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)
        self.queryset = InboxFolder.objects.filter(positionID = pos.id)
        return super(InboxFolderViewset, self).get_queryset()

    def get_object(self):
        return super(InboxFolderViewset, self).get_object()





    def create(self, request, *args, **kwargs):
        pos = Position.objects.get(
            user=self.request.user,
            company=self.request.user.current_company)
        request.data["positionID"] = pos.id
        request.data["companyID"] = pos.company_id

        return super(InboxFolderViewset, self).create(request, *args, **kwargs)

    @list_route(methods=['get'])
    def listFolderTreeView(self, request, *args, **kwargs):
        pos = Position.objects.get(user=self.request.user, company=self.request.user.current_company)
        foldersList = InboxFolder.objects.filter(positionID=pos.id)

        return Response(self.serializer_class().startTreeView(foldersList))


    #
    # def get_queryset(self):
    #     query = self.request.GET.get('query')
    #     item_per_page = self.request.GET.get('itemPerPage')
    #
    #     if item_per_page and not item_per_page == 'undefined':
    #         self.pagination_class.page_size = item_per_page
    #     try:
    #         currentProfile = InboxFolder.objects.get(userID = self.request.user.id)
    #         queryset = InboxFolder.objects.filter(profile = currentProfile).order_by("-dateOfPost")
    #         return queryset
    #     except:
    #         return []
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         newPost=serializer.create(serializer.validated_data,request=request)
    #         return Response({
    #         "id":str(newPost.pk)},
    #          status=status.HTTP_201_CREATED)
    #     return Response({
    #                         'status': 'Bad request',
    #                         'message': serializer.errors,
    #                     }, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    #

