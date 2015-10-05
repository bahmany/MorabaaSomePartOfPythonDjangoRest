# -*- coding: utf-8
import io

import sys, os
from SpiffWorkflow.bpmn.BpmnWorkflow import BpmnWorkflow
from SpiffWorkflow.bpmn.parser.ValidationException import ValidationException
from SpiffWorkflow.bpmn.parser.util import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../lib'))

from SpiffWorkflow.specs import *
from SpiffWorkflow import Task, Workflow
from SpiffWorkflow.storage import XmlSerializer

from SpiffWorkflow.bpmn.storage.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.bpmn.storage.Packager import Packager

bpmn_file = 'case1.bpmn'
bpmn_packaged = io.BytesIO()
bpmn_serializer = BpmnSerializer()




class QuestionWorkflow(object):
    def __init__(self):
        self.seriailizer=bpmn_serializer
        self.amir=1
    def set_up(self, filename):
        # Test patterns that are defined in XML format.
        package = Packager(bpmn_packaged, 'Process_1')
        package.add_bpmn_file(bpmn_file)
        package.create_package()
        self.wf_spec = bpmn_serializer.deserialize_workflow_spec(bpmn_packaged)

        self.workflow = BpmnWorkflow(self.wf_spec)

        # self.wf_spec = WorkflowSpec.deserialize(XmlSerializer(), xml, filename = filename)
        # self.taken_path = self.track_workflow(self.wf_spec)


    def run(self, UserSelection, restart=False):

        if restart:
            self.workflow = Workflow(self.wf_spec)

        workflow = self.workflow
        condition_keys = []
        if UserSelection is None:
            UserSelection = {}

        task_data_dict = UserSelection.copy()

        while not workflow.is_completed():
            tasks = workflow.get_tasks(Task.READY)

            for t in tasks:
                print("Ready:", t.task_spec.description ,t.task_spec.name)
                if hasattr(t.task_spec, "cond_task_specs"):
                    for cond, name in t.task_spec.cond_task_specs:
                        for cond_unit in cond.args:
                            if hasattr(cond_unit, "name"):
                                condition_keys.append(cond_unit.name)

            flag_keys_in_user_select = True
            for cond_key in condition_keys:
                if not task_data_dict.has_key(cond_key):
                    print(cond_key)
                    flag_keys_in_user_select = False
                    break

            if not flag_keys_in_user_select:
                # some tast's condition's key not in input userselect dict
                return

            for t in tasks:
                t.set_data(**task_data_dict)

            workflow.complete_next()

ali=QuestionWorkflow()
ali.set_up(bpmn_file)
user_selct = {'man':1, 'house': '2'}
ali.run(user_selct)
ali = ali