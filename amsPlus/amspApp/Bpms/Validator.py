from SpiffWorkflow.bpmn.parser.util import xpath_eval


class Validator(object):
    def __init__(self, bpmn):
        self.errors = []
        self.xpath = xpath_eval(bpmn)

    def validate_diagram(self):
        self.validate_diagram_end_events()
        self.validate_diagram_exclusive_getway()
        self.validate_diagram_start_events()
        self.validate_diagram_task()
        return self.errors

    def validate_diagram_start_events(self):

        if not self.xpath('.//bpmn:startEvent'):
            self.errors.append({'obj': 'StartEvent', 'message': 'Process should have 1 start at least.'})
        else:
            for catch_event in self.xpath('.//bpmn:startEvent'):
                incoming = self.xpath('.//bpmn:sequenceFlow[@targetRef="%s"]' % catch_event.get('id'))
                if incoming:
                    self.errors.append(
                        {'obj': 'StartEvent', 'message': 'Start Event doesn\' suppoer incoming sequence flow.'})
                outgoing = self.xpath('.//bpmn:sequenceFlow[@sourceRef="%s"]' % catch_event.get('id'))
                if not outgoing or len(outgoing) != 1:
                    self.errors.append({'obj': 'StartEvent', 'message': 'StartEvent should have 1 outgoing (only 1).'})
        return self.errors

    def validate_diagram_end_events(self):

        if not self.xpath('.//bpmn:endEvent'):
            self.errors.append({'obj': 'EndEvent', 'message': 'Process should have 1 end at least.'})
        else:
            for catch_event in self.xpath('.//bpmn:endEvent'):
                incoming = self.xpath('.//bpmn:sequenceFlow[@targetRef="%s"]' % catch_event.get('id'))
                if not incoming or len(incoming) != 1:
                    self.errors.append({'obj': 'EndEvent', 'message': 'EndEvent just support 1 incoming.'})
                outgoing = self.xpath('.//bpmn:sequenceFlow[@sourceRef="%s"]' % catch_event.get('id'))
                if outgoing:
                    self.errors.append({'obj': 'EndEvent', 'message': 'EndEvent doesn\'t support outgoing.'})
        return self.errors

    def validate_diagram_exclusive_getway(self):

        for catch_event in self.xpath('.//bpmn:exclusiveGateway'):
            incoming = self.xpath('.//bpmn:sequenceFlow[@targetRef="%s"]' % catch_event.get('id'))
            if not incoming:
                self.errors.append(
                    {'obj': 'exclusiveGateway', 'message': 'exclusiveGateway should have 1 incoming at least.'})
            outgoing = self.xpath('.//bpmn:sequenceFlow[@sourceRef="%s"]' % catch_event.get('id'))
            if not outgoing:
                self.errors.append(
                    {'obj': 'exclusiveGateway', 'message': 'exclusiveGateway should have 1 outgoing at least.'})
        return self.errors

    def validate_diagram_task(self):

        for catch_event in self.xpath('.//bpmn:task'):
            incoming = self.xpath('.//bpmn:sequenceFlow[@targetRef="%s"]' % catch_event.get('id'))
            if not incoming:
                self.errors.append({'obj': 'task', 'message': 'task should have 1 incoming at least.'})

            outgoing = self.xpath('.//bpmn:sequenceFlow[@sourceRef="%s"]' % catch_event.get('id'))
            if not outgoing or len(outgoing) != 1:
                self.errors.append({'obj': 'task', 'message': 'task should have just 1 outgoing.'})
        return self.errors

