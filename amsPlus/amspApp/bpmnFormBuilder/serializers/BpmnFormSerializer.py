import uuid
from rest_framework_mongoengine.validators import *
from amspApp.BpmnModeler.models import Bpmn
from rest_framework_mongoengine.serializers import *

class BpmnSerializer(DocumentSerializer):
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()
    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

    name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    xml = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_valid_form = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Bpmn
        fields = ('xml', 'description', 'user_id', 'name', 'id', 'is_valid_form')


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
        instance.save()

        return instance

