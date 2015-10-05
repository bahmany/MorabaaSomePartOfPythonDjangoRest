from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter, SimpleRouter

from rest_framework_nested import routers as _routers
from amspApp.CompaniesManagment.Charts.viewes.ChartSearchViews import ChartSearchViews
from amspApp.CompaniesManagment.Charts.viewes.ChartViews import ChartViewSet
from amspApp.CompaniesManagment.Charts.viewes.ZoneSearchViews import ChartZoneSearchViews
from amspApp.CompaniesManagment.Charts.viewes.ZonesViews import ZoneViewSet
from amspApp.CompaniesManagment.CompanyProfile.views.CompanyProfileViews import CompanyProfileViewSet
from amspApp.CompaniesManagment.Positions.views.PositionViews import PositionViewSet
from amspApp.CompaniesManagment.Processes.views.BpmnModelerView import BpmnViewSet
from amspApp.CompaniesManagment.Products.views.ProductView import CompanyProductionsViewSet
from amspApp.CompaniesManagment.Secretariat.viewes.SecretariatsViews import SecretariatsViewSet
from amspApp.CompaniesManagment.members.views.MemberView import MemberViewSet, MemberViewSetMongo
from amspApp.CompaniesManagment.views.CompaniesManagmentView import CompaniesManagmentViewSet
from amspApp.CompaniesManagment.views.CompanyMembersJointRequestView import CompanyMembersJointRequestViewset
from amspApp.Letter.views.InboxMembersGroupSearchView import MemberGroupSearchViews


url_companies_api = SimpleRouter()
url_companies_api.register(r'companies', CompaniesManagmentViewSet, base_name="companies", )

url_companies_profile = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_profile.register(r'profile', CompanyProfileViewSet, base_name="profile")

url_companies_process = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_process.register(r'process', BpmnViewSet, base_name="process")


url_companies_products = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_products.register(r'products', CompanyProductionsViewSet, base_name="products")

url_companies_chart = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_chart.register(r'chart', ChartViewSet, base_name="chart")

url_companies_zones = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_zones.register(r'chart-zone', ZoneViewSet, base_name="zones")

url_companies_positions = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_positions.register(r'positions', PositionViewSet, base_name="position", )

url_companies_members = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_members.register(r'members', MemberViewSet, base_name="position", )

url_companies_secretariats = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_secretariats.register(r'secretariats', SecretariatsViewSet, base_name="secretariats", )

url_companies_invite = _routers.NestedSimpleRouter(url_companies_api, r"companies", lookup="companyID")
url_companies_invite.register(r'invite', CompanyMembersJointRequestViewset, base_name="invite", )

urlpatterns = patterns(
    '',

    url(r'^page/companies', CompaniesManagmentViewSet.as_view({'get': 'template_page'})),
    url(r'^page/comopbase', CompaniesManagmentViewSet.as_view({'get': 'template_page_base'})),
    url(r'^page/company/profile', CompanyProfileViewSet.as_view({'get': 'template_page'})),
    url(r'^page/company/chart', ChartViewSet.as_view({'get': 'template_page'})),
    # url(r'^page/company/members', CompanyProfileViewSet.as_view({'get':'template_page'})),
    url(r'^page/company/products', CompanyProductionsViewSet.as_view({'get': 'template_page'})),
    url(r'^page/company/members', MemberViewSet.as_view({'get': 'template_page'})),
    url(r'^page/company/secretariats', SecretariatsViewSet.as_view({'get': 'template_page'})),
    url(r'^page/company/process', BpmnViewSet.as_view({'get': 'template_view'}),
        name='BpmnModelerViewTemplate'),
    url(r'^page/company/newProcess', BpmnViewSet.as_view({'get': 'template_view_new'}),
        name='template_view_newww'),
    url(r'^page/company/setupProcess', BpmnViewSet.as_view({'get': 'template_view_setup'}),
        name='template_view_setupp'),


    url(r'^search/company/members', MemberViewSetMongo.as_view(), name="members-list"),
    url(r'^search/charts/members', ChartSearchViews.as_view(), name="charts-list"),
    url(r'^search/zones/members', ChartZoneSearchViews.as_view(), name="zones-list"),
    url(r'^search/groups/members', MemberGroupSearchViews.as_view(), name="groups-list"),


    url(r'^api/v1/', include(url_companies_api.urls)),
    url(r'^api/v1/', include(url_companies_profile.urls)),
    url(r'^api/v1/', include(url_companies_products.urls)),
    url(r'^api/v1/', include(url_companies_chart.urls)),
    url(r'^api/v1/', include(url_companies_zones.urls)),
    url(r'^api/v1/', include(url_companies_process.urls)),
    url(r'^api/v1/', include(url_companies_positions.urls), name="position"),
    url(r'^api/v1/', include(url_companies_members.urls), name="members"),
    url(r'^api/v1/', include(url_companies_secretariats.urls), name="secretariats"),
    url(r'^api/v1/', include(url_companies_invite.urls), name="invite"),
)


