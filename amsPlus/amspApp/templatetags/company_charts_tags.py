from django import template
from django.template.loader_tags import register


@register.inclusion_tag(
    "generic-templates/CompanyCharts.html",
    takes_context=True)
def CompanyChartsTag(context, **kwargs):
    if not "cencelMethodName" in kwargs: kwargs["cencelMethodName"] = "CancelPostionSelect()"
    if not "postMethodName" in kwargs: kwargs["postMethodName"] = "PostPostionSelect()"

    context = context

    return kwargs