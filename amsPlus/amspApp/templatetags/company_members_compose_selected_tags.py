from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyMembersComposeSelected.html",
    takes_context=True)
def CompanyMembersComposeSelectedTag(context, **kwargs):
    return kwargs