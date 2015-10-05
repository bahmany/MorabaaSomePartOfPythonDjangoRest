from amspApp.Infrustructures.views import *

__author__ = 'Administrator'
from django.conf.urls import patterns, url, include

from amspApp.Infrustructures.views.TimeZoneViews import *
# from dms.viewsClasses.companies import *


urlpatterns = patterns('',
                       url(r'^api/v1/timezone/', view=set_timezone, name="set_timezone"),
                       url(r'^api/v1/gettimezone/', view=get_timezone, name="get_timezone"),



)