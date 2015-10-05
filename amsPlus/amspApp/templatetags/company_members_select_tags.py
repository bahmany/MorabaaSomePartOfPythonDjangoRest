from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersSelectList.html",
    takes_context=True)
def CompanyMembersSelectTag(context, **kwargs):
    return kwargs