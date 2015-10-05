from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from rest_framework.renderers import HTMLFormRenderer
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.CompaniesManagment.Positions.models import PositionsDocument
from amspApp.amspUser.serializers.UserSerializer import UserSerializer


def base(request):
    return render_to_response('others/base.html', {}, context_instance=RequestContext(request))


def login(request):
    return render_to_response('authentication/login.html', {}, context_instance=RequestContext(request))


def signup(request):
    return render_to_response('authentication/signup.html', {}, context_instance=RequestContext(request))


def forget(request):
    return render_to_response('authentication/forget.html', {}, context_instance=RequestContext(request))


def dashboard(request):
    return render_to_response('others/dashboard.html', {}, context_instance=RequestContext(request))


def upload(request):
    return render_to_response('generic-templates/upload.html', {}, context_instance=RequestContext(request))


def selectPosition(request):
    return render_to_response('generic-templates/selectPositions.html', {}, context_instance=RequestContext(request))


from rest_framework.decorators import api_view


@api_view()
def getCurrent(request):
    from rest_framework.response import Response

    return Response({'company': request.user.current_company.id,
                     'positionMysql': Position.objects.get(user=request.user,
                                                           company=request.user.current_company).id if request.GET[
                         'position'] else '',
                     'positionDocument': str(PositionsDocument.objects.get(companyID=request.user.current_company.id,
                                                                           userID=request.user.id).id) if request.GET[
                         'position'] else ''})


def blank(request):
    return render_to_response('others/blank.html', {},
                              context_instance=RequestContext(request))


def newbpmn(request):
    return render_to_response('others/../templates/companyManagement/newbpmn.html', {},
                              context_instance=RequestContext(request))


def build_form(request):
    return render_to_response('others/../templates/companyManagement/SetupBpmnElements.html', {},
                              context_instance=RequestContext(request))


def companydash(request):
    return render_to_response('companyManagement/CompanyManagement.html', {},
                              context_instance=RequestContext(request))


def companydashboard(request):
    return render_to_response('companyManagement/companyDashboard.html', {},
                              context_instance=RequestContext(request))


def chartcompany(request):
    return render_to_response('companyManagement/CompanyChart.html', {},
                              context_instance=RequestContext(request))


def memberscompany(request):
    return render_to_response('companyManagement/CompanyMembers.html', {},
                              context_instance=RequestContext(request))


def profilecompany(request):
    return render_to_response('companyManagement/CompanyProfile.html', {},
                              context_instance=RequestContext(request))


def productscompany(request):
    return render_to_response('companyManagement/CompanyProducts.html', {},
                              context_instance=RequestContext(request))


class IndexView(TemplateView):
    template_name = 'others/index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)



