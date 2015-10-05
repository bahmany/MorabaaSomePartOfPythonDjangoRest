import uuid
from rest_framework_mongoengine.serializers import *
from amspApp.CompaniesManagment.Processes.models import Bpmn


class BpmnSerializer(DocumentSerializer):
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()
    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

    name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    xml = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_valid_form = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    form = serializers.ListField(required=False, allow_null=True)
    processObjs = serializers.ListField(required=False, allow_null=True)
    userTasks= serializers.ListField(required=False, allow_null=True)

    class Meta:
        model = Bpmn
        fields = ('xml', 'description', 'user_id', 'company_id', 'name', 'id', 'is_valid_form','form','processObjs','userTasks')


    def create(self, validated_data, **kwargs):
        validated_data['user_id'] = kwargs['request'].user.pk
        if Bpmn.objects.filter(user_id=validated_data['user_id'],name=validated_data['name']).count() > 0:
            raise serializers.ValidationError({"message":{"name":["name must be unique"]},"status":"Bad request"})

        return Bpmn.objects.create(**validated_data)
    def update(self, instance, validated_data):
        datas = Bpmn.objects.filter(user_id=instance['user_id'],name=validated_data['name'])
        counts=datas.count()
        if counts == 1:
            for obj in datas:
                if obj.name != instance.name:
                    raise serializers.ValidationError({"status":"Bad request","message":{"name":["name must be unique"]}})
        if counts > 1:
            raise serializers.ValidationError({"status":"Bad request","message":{"name":["name must be unique"]}})
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.xml = validated_data.get('xml', instance.xml)
        instance.is_valid_form = validated_data.get('is_valid_form', instance.is_valid_form)
        if 'form' in validated_data.keys():
            for frm in validated_data["form"]:
                if '$_invalid' in frm["schema"].keys():
                    frm["schema"].pop('$_invalid',None)

                for obj in frm["schema"]["fields"]:
                    if '$_invalid' in obj.keys():
                        obj.pop('$_invalid',None)
                    if '$_displayProperties' in obj.keys():
                        obj.pop('$_displayProperties',None)
                    if '$_isDragging' in obj.keys():
                        obj.pop('$_isDragging',None)
            instance.form = validated_data.get('form', instance.form)
        if 'processObjs' in validated_data.keys():
            for itm in validated_data["processObjs"]:
                if '$_invalid' in itm:
                    itm.pop('$_invalid',None)
                if '$_displayProperties' in itm:
                    itm.pop('$_displayProperties',None)
                if '$_isDragging' in itm:
                    itm.pop('$_isDragging',None)
            instance.processObjs = validated_data.get('processObjs', instance.processObjs)
        instance.userTasks = validated_data.get('userTasks', instance.userTasks)
        instance.save()

        return instance

