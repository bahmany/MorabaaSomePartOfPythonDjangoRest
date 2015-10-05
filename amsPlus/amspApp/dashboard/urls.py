from django.conf.urls import patterns, include, url

from django.contrib import admin
from amspApp.dashboard.views import HomeView
from amspApp.views import IndexView



urlpatterns = patterns('',

            url(r'^our/home', HomeView.Home.as_view({'get':'home'})),
            url(r'^scripts/directives/topnav/', HomeView.Home.as_view({'get':'topnav'})),
            url(r'^scripts/directives/sidebar/', HomeView.Home.as_view({'get':'sidebar'})),


)
