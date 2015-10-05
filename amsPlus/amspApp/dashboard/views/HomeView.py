from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template import RequestContext


class Home(viewsets.ViewSet):
    def home(self, request):
        data = {
            'currentUser': request.user.username
        }
        return render_to_response('others/home.html',data,context_instance=RequestContext(request))

    def topnav(self,request):
        data = {
            'currentUser': request.user.username
        }
        return render_to_response('others/top-nav/topnav.html',data,context_instance=RequestContext(request))

    def sidebar(self,request):
        data = {
            'currentUser': request.user.username
        }
        return render_to_response('others/sidebar/sidebar.html',data,context_instance=RequestContext(request))