from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersSelected.html",
    takes_context=True)
def CompanyMembersSelectedTag(context, **kwargs):
    return kwargs