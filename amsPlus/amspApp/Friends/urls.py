from django.conf.urls import patterns, url, include
from amspApp.FileServer.views.FileUploadView import FileUploadViewSet
from amspApp.Friends.views.FriendsViews import FriendViewSet

__author__ = 'mohammad'

urlpatterns = patterns(
    '',
    url(r'^page/friends', FriendViewSet.as_view({"get": "template_view"})),


)