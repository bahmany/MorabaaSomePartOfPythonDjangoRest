from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from amspApp.CompaniesManagment.Positions.models import Position
from amspApp.Letter.models import InboxFolder
from amspApp._Share.DynamicFieldsDocumentSerializer import DynamicFieldsDocumentSerializer
from django.utils.translation import ugettext_lazy as _


class InboxFolderSerializer(DynamicFieldsDocumentSerializer):
    # title = serializers.CharField(allow_null=False, allow_blank=False)

    class Meta:
        model = InboxFolder
        extra_kwargs = {
            'parentID': {'allow_null': True,'allow_blank': True,'required': False}

        }
        # fields = (
        #     'id',
        #     'positionID',
        #     'companyID',
        #     'parentID',
        #     'isPublic',
        #     'title',
        #     'count',
        # )


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

    def validate(self, attrs):

        pos = Position.objects.get(
            user=self.context["request"].user,
            company=self.context["request"].user.current_company
        )

        if self.partial :
            if str(attrs["id"]) == attrs['parentID']:
                raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": "Parent", "message": _("Invalid parent id")}]})
            if pos.id != attrs['positionID']:
                raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": "Hacked!", "message": _("Noway")}]})
            return super(InboxFolderSerializer, self).validate(attrs)


        if InboxFolder.objects.filter(title=attrs['title'], positionID=pos.id).count() > 0:
            raise serializers.ValidationError(
                {"status": "Bad request", "message": [{"name": "Name", "message": "This field should be unique"}]})
        return super(InboxFolderSerializer, self).validate(attrs)

    def startTreeView(self, data):
        output = {}
        varlist = []
        for d in data:
            if not d.parentID:
                output = {
                    "title": d.title,
                    "positionID": d.positionID,
                    "isPublic": d.isPublic,
                    "parentID": d.parentID,
                    "id": str(d.id),
                    "children": self.getTreeViewData(output, d.id, data)}
                varlist.append(output)
        return varlist

    def getTreeViewData(self, output, parentItem, data):
        subitems = data.filter(parentID=str(parentItem))
        v = []
        for item in subitems:
            v.append({
                "title": item.title,
                "positionID": item.positionID,
                "isPublic": item.isPublic,
                "parentID": item.parentID,
                "id": str(item.id),
                "children": self.getTreeViewData(output, item.id, data)})
        return v




