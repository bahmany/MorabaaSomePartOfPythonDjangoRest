from mongoengine import DictField
from rest_framework import serializers
from rest_framework.fields import *
# from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, DynamicDocumentSerializer
from amspApp.MyProfile.models import Profile
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer
from django.utils.translation import ugettext_lazy as _


class ProfileSerializer(DynamicFieldsDocumentSerializer):
    class Meta:
        model = Profile
        depth = 2

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)


    def update(self, instance, validated_data):
        instance.extra = validated_data['extra']
        if instance.extra["Name"] == "":
            raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": _("Name"), "message": _("This field is required")}]})
        return super(ProfileSerializer, self).update(instance, validated_data)


    def defaultExtra(self, userInstance):
        return {"extra": {
            "profileHeaderBackground": {
                "url": "/static/images/person_profile_default.jpg",
            },
            "profileAvatar": {
                "url": "/static/images/avatar_empty.jpg",
            },
            "Name": str(_("%s - change it please !" % (userInstance.username,))),
            "Title": str(_("Nothing yet..!")),
            "Phones": [],
            "AboutMe": {
                "title": str(_("A little about me")),
                "detail": """
                                    Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum
                                    soluta nobis est eligendi optio
                                    cumque nihil impedit quo minus id quod maxime placeat facer
                """,
            }
        }
        }
    def create_default_profile(self, userInstance):
        returnProfile = self.defaultExtra(userInstance)
        returnProfile["userID"] = userInstance.pk
        returnProfile["emails"] = [userInstance.email, ]
        returnProfile["friends"] = []
        returnProfile["companyMembers"] = []
        obj = Profile.objects.create(**returnProfile)
        return obj


# class PhonesField(ListField):
#
#
# class extraProfileField(DictField):
# profileHeaderBackground = CharField(max_length=200, min_length=10,
#                                         default="/static/images/default_company_profile_header_background.png")
#     Name = CharField(max_length=150, min_length=3)
#     Title = CharField(max_length=150, min_length=3)
#     Phones = PhonesField()
#

#
# MyProfile.extra.profileHeaderBackground.url
# MyProfile.extra.Name
# MyProfile.extra.Title
# MyProfile.extra.Phones.length
# item.phoneORemail == 1 to 2
# item.security == 1 to 4
# item.tel
# RemovePhone(MyProfile.extra.Phones,$index)
# MyProfile.extra.AboutMe.title
# MyProfile.extra.AboutMe.detail
#
#
#
#
#
#


# def defaultExtra(self):
# return {"extra": {
#         "profileHeaderBackground": {
#             "url": "/static/images/person_profile_default.jpg",
#         },
#         "profileAvatar": {
#             "url": "/static/images/avatar_empty.jpg",
#         },
#         "Name": str(_("%s - change it please !" % (self.request.user.username,))),
#         "Title": _("Nothing yet..!"),
#         "Phones": [],
#         "AboutMe": {
#             "title": _("A little about me"),
#             "detail": """
#                                 Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum
#                                 soluta nobis est eligendi optio
#                                 cumque nihil impedit quo minus id quod maxime placeat facer
#             """,
#         }
#     }
#     }

