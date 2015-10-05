from django.conf.urls import patterns, include, url
from rest_framework_mongoengine import routers
from amspApp.BpmnModeler.views import BpmnModelerView


router = routers.SimpleRouter()
router.register(r'bpmns', BpmnModelerView.BpmnViewSet,base_name='bpmns')

urlpatterns = patterns(
    '',
    # ... URLs

    url(r'^api/v1/', include(router.urls)),
    url(r'^myapi/bpmns/', BpmnModelerView.BpmnViewSet.as_view({'get': 'list'}), name='BpmnModelerViewList'),
    # url(r'^api/v1/buildForm/', BpmnModelerView.BpmnViewSet.as_view({'get': 'build_form'}), name='BpmnModelerViewBuildForm'),


)
