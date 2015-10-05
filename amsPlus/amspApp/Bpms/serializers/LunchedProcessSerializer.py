import pickle
from bson import ObjectId
from rest_framework_mongoengine.serializers import *
from amspApp.Bpms.BpmEngine import BpmEngine
from amspApp.Bpms.models import LunchedProcess
from amspApp.CompaniesManagment.Positions.models import PositionsDocument


class LunchedProcessSerializer(DocumentSerializer):
    bpmn = serializers.CharField(label="bpmn",
                                 style={'template': 'forms/base-templates/selectAngular.html',
                                        'cssclass': 'col-md-12', 'ngmodel': 'lunchedProcess.bpmn',
                                        'ngoptions': 'obj.id as obj.name for obj in bpmns'})
    name = serializers.CharField(label="name", style={'template': 'forms/base-templates/input.html',
                                                      'cssclass': 'col-md-12',
                                                      'ngmodel': 'lunchedProcess.name'})
    bpmnName = serializers.CharField(source='bpmn.name', read_only=True)
    bpmnId = serializers.CharField(source='bpmn.id', read_only=True)


    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    def _get_default_field_names(self, *args, **kwargs):
        return self.get_field_names(*args, **kwargs)

    class Meta:
        model = LunchedProcess
        fields = (
            'id', 'user_id', 'bpmn', 'bpmnName', 'bpmnId', 'thisStep', 'thisPerformer', 'thisStatus', 'name',
            'formData')
        depth = 1

    def create(self, validated_data, **kwargs):
        validated_data['user_id'] = str(kwargs['request'].user.pk)
        validated_data['position_id'] = str(PositionsDocument.objects.get(userID=kwargs['request'].user.id,
                                                                      companyID=kwargs[
                                                                          'request'].user.current_company.id).id)
        new = LunchedProcess.objects.create(**validated_data)
        engineInstance = BpmEngine(new.bpmn.xml, new.bpmn.form, new.bpmn.userTasks, new.pk)
        new.engineInstance = pickle.dumps(engineInstance)
        new.save()
        engineInstance.run()
        return new
