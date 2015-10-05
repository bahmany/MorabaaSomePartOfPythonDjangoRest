'use strict';

angular.module('AniTheme')
    .controller('LunchedProcessDoCtrl', function ($scope, $http, $translate, $rootScope, $stateParams, $state, $modal, $location, LunchedProcessService, bpmnService) {
        $scope.sendingData = {};
        $scope.completeIt = function () {
            LunchedProcessService.completeJob($stateParams.lunchedProcessId, $scope.sendingData).success(function (data) {

                swal({
                    title: "Youi did it",
                    text: "now it send to next step" ,
                    type: "success"
                }, function () {
                    $state.go("process.inbox");
                });

            });
        };
        $scope.current = {};
        $scope.renderForm = function () {
            LunchedProcessService.retrieveLunchedProcess($stateParams.lunchedProcessId).success(function (data) {
                bpmnService.getCurrent(0).success(function (dataCurrnet) {
                    $scope.current = dataCurrnet;
                    bpmnService.retrieveBpmn($scope.current.company, data['bpmnId']).success(function (dataBpmn) {

                        dataBpmn['form'].some(function (element, index, array) {
                            if (element["bpmnObjID"] == data["thisStep"]) {
                                $scope.formSchema = element['schema'];

                            }
                        });
                        $scope.sendingData.formData = data.formData;

                    });
                });

            });
        };

        $scope.renderForm();
    });

