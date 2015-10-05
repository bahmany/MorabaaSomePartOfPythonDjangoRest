'use strict';

var globalxml = "";
angular.module('AniTheme')
    .controller('bpmnModelerCtrl', function ($scope, $http, $translate, $rootScope, $state, $stateParams, $location, $modal, bpmnService) {

        $scope.groups = {};
        $scope.group = {};
        $scope.newGroup = {};
        $scope.oldGroup = {};

        $scope.timeouts = [];
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.itemsPerPage = 14;
        $scope.bpmn = {};

        if ($stateParams.processId) {
            bpmnService.retrieveBpmn($stateParams.companyid, $stateParams.processId).success(function (data) {
                $scope.bpmn.name = data['name'];
                $scope.bpmn.xml = data['xml'];
                $scope.bpmn.description = data['description'];
                $scope.bpmn.id = data['id'];
                globalxml = data['xml'];
            });
        }
        $scope.saveBpmn = function (xml) {
            $scope.bpmn.xml = '<?xml version="1.0" encoding="UTF-8"?>' +
            '<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' +
            'xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" ' +
            'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" ' +
            'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" ' +
            'targetNamespace="http://bpmn.io/schema/bpmn" ' +
            'id="Definitions_1">' +
            '<bpmn:process id="Process_1" isExecutable="false">' +
            '<bpmn:startEvent id="StartEvent_1"/>' +
            '</bpmn:process>' +
            '<bpmndi:BPMNDiagram id="BPMNDiagram_1">' +
            '<bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">' +
            '<bpmndi:BPMNShape id="_BPMNShape_StartEvent_2" bpmnElement="StartEvent_1">' +
            '<dc:Bounds height="36.0" width="36.0" x="173.0" y="102.0"/>' +
            '</bpmndi:BPMNShape>' +
            '</bpmndi:BPMNPlane>' +
            '</bpmndi:BPMNDiagram>' +
            '</bpmn:definitions>';
            if (xml != undefined) {
                $scope.bpmn.xml = xml;
            }
            if ($scope.bpmn.id) {
                
                if ($('#start-edite-div').is(':visible')) {
                    $scope.bpmn.xml = globalxml;
                }

                bpmnService.bpmnUpdate($stateParams.companyid, $scope.bpmn.id, $scope.bpmn).success(function (data) {
                    $scope.bpmn = data;
                    $state.go("company.process", {companyid: $stateParams.companyid});

                }).error(function (data) {
                    $scope.errors = data;
                });
            } else {

                bpmnService.bpmnCreate($stateParams.companyid, $scope.bpmn).success(function (data) {
                    $scope.bpmn = data;
                    $state.go("company.process", {companyid: $stateParams.companyid});

                }).error(function (data) {
                    $scope.errors = data;
                    $scope.errors = $scope.errors.message;
                });
            }
        }
    });
