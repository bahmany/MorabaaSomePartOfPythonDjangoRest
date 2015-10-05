import uuid

__author__ = 'mohammad'

from django import template


register = template.Library()


@register.inclusion_tag(
    "ani-theme/../../templates/generic-templates/ProgressBtn.html",
    takes_context=True)
def ProgressSuccessBtn(context, **kwargs):
    context = context
    kwargs["btnCssClass"] = "btn btn-xs progress-button progress-button-success"
    kwargs["DataStyle"] = "shrink"
    kwargs["OtherProp"] = "data-horizontal"
    kwargs["BtnContent"] = kwargs["BtnContent"] if "BtnContent" in kwargs.keys() else  "<i class='fa fa-save'></i>"
    return kwargs


@register.inclusion_tag(
    "ani-theme/../../templates/generic-templates/ProgressBtn.html",
    takes_context=True)
def ProgressPrimaryBtn(context, **kwargs):
    context = context
    kwargs["btnCssClass"] = "progress-button"
    kwargs["DataStyle"] = "shrink"
    kwargs["OtherProp"] = "data-horizontal"
    kwargs["BtnContent"] = kwargs["BtnContent"] if "BtnContent" in kwargs.keys() else  "<i class='fa fa-plus'></i>"

    return kwargs
