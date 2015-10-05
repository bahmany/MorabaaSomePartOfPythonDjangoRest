from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter, Route, DynamicDetailRoute
from amspApp.Letter.views.InboxComposeView import InboxComposeViewSet
from amspApp.Letter.views.InboxFolderView import InboxFolderViewset
from amspApp.Letter.views.InboxGroupView import InboxGroupViewset
from amspApp.Letter.views.InboxLabelView import InboxLabelViewset
from amspApp.Letter.views.InboxView import InboxViewSet


letterInboxFolder_router = SimpleRouter()
letterInboxFolder_router.register("inboxFolders", InboxFolderViewset, base_name="InboxFolderPage")

letterInboxLabel_router = SimpleRouter()
letterInboxLabel_router .register("inboxLabels", InboxLabelViewset, base_name="InboxLabelPage")


letterInboxGroup_router = SimpleRouter()
letterInboxGroup_router .register("inboxGroups", InboxGroupViewset, base_name="InboxGroupPage")




urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(letterInboxFolder_router.urls)),
    url(r'^api/v1/', include(letterInboxLabel_router.urls)),
    url(r'^api/v1/', include(letterInboxGroup_router.urls)),
    url(r'^page/letterBase', InboxViewSet.as_view({"get":"template_view_base"})),
    # url(r'^page/letter/inbox', InboxViewSet.as_view({"get":"template_view"})),
    url(r'^page/letter/compose', InboxComposeViewSet.as_view({"get":"template_view"})),

)