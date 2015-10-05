from django.conf.urls import patterns, include, url
from rest_framework_mongoengine import routers
from amspApp.Bpms.views import LunchedProcessView


router = routers.SimpleRouter()
router.register(r'LunchedProcess', LunchedProcessView.LunchedProcessViewSet,base_name='LunchedProcess')

urlpatterns = patterns(
    '',
    # ... URLs

    url(r'^api/v1/', include(router.urls)),
    url(r'^page/process/inbox', LunchedProcessView.LunchedProcessViewSet.as_view({'get': 'template_view_inbox'}), name='template_vieew_inbox'),
    url(r'^page/process/myProcess', LunchedProcessView.LunchedProcessViewSet.as_view({'get': 'template_view_my_process'}), name='template_view_mey_process'),
    url(r'^page/process/myDoneProcess', LunchedProcessView.LunchedProcessViewSet.as_view({'get': 'template_view_my_done_process'}), name='template_view_mey_done_process'),
    url(r'^page/process/do', LunchedProcessView.LunchedProcessViewSet.as_view({'get': 'template_view_do_process'}), name='template_view_do_process'),
    # url(r'^api/v1/buildForm/', BpmnModelerView.BpmnViewSet.as_view({'get': 'build_form'}), name='BpmnModelerViewBuildForm'),


)
