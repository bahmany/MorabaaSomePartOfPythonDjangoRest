from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter, Route, DynamicDetailRoute
from amspApp.MyProfile.viewes.PostsView import PostsViewset
from amspApp.MyProfile.viewes.ProfileManagmentView import ProfileManagmentViewSet

#
# class ProfileRouter(SimpleRouter):
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={
#                 'get': 'list',  # responding current user profile
#
#             },
#             name="{basename}-list",
#             initkwargs={},
#         ),
#         Route(
#             url=r'^{prefix}/get-profile$',
#             mapping={
#                 'get': 'retrieve',  # responding current user profile
#                 'put': 'update',  # responding current user profile
#             },
#             name="{basename}-detail",
#             initkwargs={},
#         ),
#         Route(
#             url=r'^{prefix}/get-avatar$',
#             mapping={
#                 'get': 'GetAvatar',  # responding current user profile
#             },
#             name="{basename}-get-avatar",
#             initkwargs={},
#         ),
#
#         DynamicDetailRoute(
#             url=r'^{prefix}/{methodname}{trailing_slash}$',
#             name='{basename}-{methodnamehyphen}',
#             initkwargs={}
#         ),
#
#         DynamicDetailRoute(
#             url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
#             name='{basename}-{methodnamehyphen}',
#             initkwargs={}
#         ),
#
#         # Route(
#         # url=r'^{prefix}/posts$',
#         #     mapping={
#         #         'get':'GetPosts',  # responding current user profile
#         #         'post':'PostPost',  # responding current user profile
#         #     },
#         #     name = "{basename}-list",
#         #     initkwargs={},
#         # ),
#
#     ]


profile_router = SimpleRouter()
profile_router.register("profile", ProfileManagmentViewSet, base_name="ProfilePage")

posts_router = SimpleRouter()
posts_router.register("posts", PostsViewset, base_name="PostsPage")



urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(profile_router.urls)),
    url(r'^api/v1/', include(posts_router.urls)),

    url(r'^page/myProfile', ProfileManagmentViewSet.as_view({"get":"template_view"})),

)