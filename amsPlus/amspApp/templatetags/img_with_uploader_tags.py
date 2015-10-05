import uuid

__author__ = 'mohammad'

from django import template


register = template.Library()




@register.inclusion_tag(
    "ani-theme/../../templates/generic-templates/ImageWithUploader.html",
    takes_context=True)
def ImageWithUploaderForAvatar(context, **kwargs):
    context = context
    kwargs["overlayerClass"] = "div"+uuid.uuid4().hex
    kwargs["uploading_profile_wait"] = "upload"+uuid.uuid4().hex
    kwargs["change_profile_image"] = "chng"+uuid.uuid4().hex
    kwargs["id"] = "img"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["imageContainerSize"] = "col-sm-3"
    kwargs["imageContainerBorder"] = "1px solid white"
    kwargs["imageContainerBorderRadius"] = "5px"
    kwargs["imageContainerOtherCss"] = "margin-top: -30px;"
    kwargs["defaultEmptyAvatarUrl"] = "/static/images/avatar_empty.jpg"
    return kwargs

@register.inclusion_tag(
    "ani-theme/../../templates/generic-templates/ImageWithUploader.html",
    takes_context=True)
def ImageWithUploaderForDefaultPicOfCompanyProduct(context, **kwargs):
    context = context
    kwargs["overlayerClass"] = "div"+uuid.uuid4().hex
    kwargs["uploading_profile_wait"] = "upload"+uuid.uuid4().hex
    kwargs["change_profile_image"] = "chng"+uuid.uuid4().hex
    kwargs["id"] = "img"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["imageContainerSize"] = "col-sm-3"
    kwargs["imageContainerBorder"] = "1px solid white"
    kwargs["imageContainerBorderRadius"] = "5px"
    kwargs["imageContainerOtherCss"] = "padding: 5px;"
    kwargs["defaultEmptyAvatarUrl"] = "//"+kwargs["modelName"]+"//" if "modelName" in kwargs.keys() else "/static/images/default_pic_production.png"
    return kwargs

@register.inclusion_tag(
    "ani-theme/../../templates/generic-templates/ImageWithUploader.html",
    takes_context=True)
def ImageWithUploader(context, **kwargs):
    context = context
    kwargs["overlayerClass"] = "div"+uuid.uuid4().hex
    kwargs["uploading_profile_wait"] = "upload"+uuid.uuid4().hex
    kwargs["change_profile_image"] = "chng"+uuid.uuid4().hex
    kwargs["id"] = "img"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["fileUploaderID"] = "uploader"+uuid.uuid4().hex
    kwargs["imageContainerSize"] = "col-sm-3" if not "imageContainerSize" in kwargs.keys() else kwargs["imageContainerSize"]
    kwargs["imageContainerBorder"] = "1px solid white" if not "imageContainerBorder" in kwargs.keys() else kwargs["imageContainerBorder"]
    kwargs["imageContainerBorderRadius"] = "5px" if not "imageContainerBorderRadius" in kwargs.keys() else kwargs["imageContainerBorderRadius"]
    kwargs["imageContainerOtherCss"] = "padding: 5px;" if not "imageContainerOtherCss" in kwargs.keys() else kwargs["imageContainerOtherCss"]
    kwargs["defaultEmptyAvatarUrl"] = "//"+kwargs["modelName"]+"//" if "modelName" in kwargs else "/static/images/default_pic_production.png"
    return kwargs



