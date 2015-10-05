# -*- coding: utf-8
from copy import copy
import io
import pickle

import sys, os
from SpiffWorkflow.bpmn.BpmnWorkflow import BpmnWorkflow
from SpiffWorkflow.bpmn.parser.ValidationException import ValidationException
from SpiffWorkflow.bpmn.parser.util import *
from amspApp.Bpms.MyPackager import MyPackager

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../lib'))

from SpiffWorkflow.specs import *

from SpiffWorkflow import Task, Workflow
from SpiffWorkflow.storage import XmlSerializer

from SpiffWorkflow.bpmn.storage.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.bpmn.storage.Packager import Packager
from SpiffWorkflow.bpmn.specs.UserTask import UserTask as UserTaskSpecBpmn
from SpiffWorkflow.bpmn.specs.EndEvent import EndEvent as EndEventSpecBpmn
from amspApp.Bpms.models import LunchedProcess


class BpmEngine(object):
    def __init__(self, xml, forms, userTasks, taskObjId):
        self.serializer = BpmnSerializer()
        self.package = io.BytesIO()
        self.forms = forms
        self.taskObjId = taskObjId
        self.userTasks = userTasks
        package = MyPackager(self.package, 'Process_1')
        self.xml = xml
        package.add_bpmn_file(self.xml)
        package.create_package_xml()
        self.wf_spec = self.serializer.deserialize_workflow_spec(self.package)
        # self.taken_path = self.track_workflow(self.wf_spec)
        self.workflow = BpmnWorkflow(self.wf_spec)

    Sorry Skipped
