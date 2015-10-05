from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersZonesSelectList.html",
    takes_context=True)
def CompanyMembersZoneSelectTag(context, **kwargs):
    return kwargs