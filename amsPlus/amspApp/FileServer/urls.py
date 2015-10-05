from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter, Route
from amspApp.FileServer.views.FileUploadView import  FileUploadViewSet

__author__ = 'mohammad'



urlpatterns = patterns(
    '',
    url(r'^api/v1/file/upload$', FileUploadViewSet.as_view()

    )
)