from django.conf.urls import patterns, include, url

from django.contrib import admin
from amspApp import views
from amspApp.CompaniesManagment.views.CompanyView import CompanyViewSet


from amspApp.amspUser import urls as amspUserUrls
from amspApp.dashboard import urls as dashboardUrls
from amspApp.Bpms import urls as taskUrl
from amspApp.CompaniesManagment import urls as companyUrl
from amspApp.MyProfile import urls as profileUrl
from amspApp.Letter import urls as letterInboxUrl
from amspApp.FileServer import urls as fileUrl
from amspApp.Infrustructures import urls as InfrUrl
from amspApp.Friends import urls as FrndUrl



from amspApp.dashboard.views import HomeView
from amspApp.amspUser.views.UserView import UserViewSet
from amspApp.amspUser.views.GroupView import GroupViewSet

from amspApp.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',

                       # 1
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^page/base', views.base),
                       url(r'^page/login', views.login),
                       url(r'^page/signup', views.signup),
                       url(r'^page/forget', views.forget),

                       url(r'^', include(amspUserUrls)),
                       url(r'^', include(dashboardUrls)),
                       url(r'^', include(companyUrl)),
                       url(r'^', include(taskUrl)),
                       url(r'^', include(profileUrl)),
                       url(r'^', include(letterInboxUrl)),
                       url(r'^', include(fileUrl)),
                       url(r'^', include(InfrUrl)),
                       url(r'^', include(FrndUrl)),

                       url(r'^page/dashboard', views.dashboard),
                       url(r'^page/generic/upload', views.upload),
                       url(r'^page/generic/selectPosition', views.selectPosition),
                       url(r'^getCurrent', views.getCurrent),


                       url('^.*$', IndexView.as_view(), name='index'),

)
