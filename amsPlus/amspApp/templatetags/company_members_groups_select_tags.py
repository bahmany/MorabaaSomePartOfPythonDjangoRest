from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersGroupsSelectList.html",
    takes_context=True)
def CompanyMembersGroupSelectTag(context, **kwargs):
    return kwargs