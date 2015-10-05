import uuid

__author__ = 'mohammad'

from django import template


register = template.Library()




@register.inclusion_tag(
    "generic-templates/PagerLeftRight.html",
    takes_context=True)
def pagerNavigator(context, **kwargs):
    if not "PageTo" in kwargs: kwargs["PageTo"] = "PageTo"
    return kwargs
