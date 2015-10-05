from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersChartSelectList.html",
    takes_context=True)
def CompanyMembersChartSelectTag(context, **kwargs):
    return kwargs