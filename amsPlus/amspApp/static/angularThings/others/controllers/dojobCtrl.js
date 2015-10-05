'use strict';

angular.module('AniTheme')
    .controller('dojobCtrl', function ($scope, $http, $translate, $rootScope, $stateParams, $modal, $location, taskService, bpmnService) {
        $scope.sendingData={};
        $scope.completeTask = function () {
            taskService.completeJob($stateParams.taskId,$scope.sendingData).success(function (data) {
                console.log(data);
            });

        };

        $scope.renderForm = function () {
            taskService.retrieveTask($stateParams.taskId).success(function (data) {
                bpmnService.retrieveBpmn(data['bpmnId']).success(function (dataBpmn) {

                    dataBpmn['form'].some(function (element, index, array) {
                        if (element["bpmnObjID"] == data["thisStep"]) {
                            $scope.formSchema = element['schema'];

                        }
                    });
                });
            });
        };

        $scope.renderForm();
    });

