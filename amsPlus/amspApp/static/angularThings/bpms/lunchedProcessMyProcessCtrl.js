'use strict';
var globalxml = '';


angular.module('AniTheme')
    .controller('lunchedProcessMyProcessCtrl', function ($scope, $http, $translate, $rootScope, $modal, $location, LunchedProcessService, bpmnService) {

        $scope.bpmns = {};
        $scope.current = {};
        $scope.bpmn = {};
        $scope.oldBpmn = {};
        $scope.timeouts = [];
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.itemsPerPage = 14;

        // it's for get edit form field data
        $scope.createLunchedProcess = function () {

            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalTaskCreate.html',
                controller: 'ModalLunchedProcessCreateInstanceCtrl',
                size: '',
                resolve: {}
            });

            modalInstance.result.then(function (res) {
                $scope.getLunchedProcessList();
            }, function () {

            });
        };

        $scope.doJob = function (LunchedProcessId) {
            $location.url('/dashboard/dojob/' + LunchedProcessId);
        };

        $scope.retrieveLunchedProcess = function (id) {
            bpmnService.retrieveLunchedProcess(id).success(function (data) {
                $scope.bpmn.name = data['name'];
                $scope.bpmn.xml = data['xml'];
                $scope.bpmn.description = data['description'];
                $scope.bpmn.id = data['id'];
                globalxml = data['xml'];
            });
        };

        $scope.buildForm = function (id) {
            $rootScope.id = id;
            $location.url('/dashboard/buildForm');
        };
        $scope.lunchedProcessDelete = function (id) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalAreYouSure.html',
                controller: 'ModalAreYouSureInstanceCtrl',
                size: '',
                resolve: {}
            });
            modalInstance.result.then(function (selectedItem) {
                bpmnService.lunchedProcessDelete(id).success(function (data) {

                    $scope.getLunchedProcessList();
                }).error(function (data) {
                    var modalInstance = $modal.open({
                        animation: true,
                        templateUrl: 'GenericModalPermissionDenied.html',
                        controller: 'ModalPermissionDeniedInstanceCtrl',
                        size: '',
                        resolve: {}
                    });
                });

            }, function () {
            });

        };

        $scope.getLunchedProcessList = function () {
            LunchedProcessService.listLunchedProcess($scope.currentPage, $scope.searchInput, $scope.itemsPerPage, "MyProcess").success(function (data) {
                $scope.data = data;
                $scope.totalItems = data.count;
                if (($scope.searchInput == undefined) || ($scope.searchInput == '')) {
                    $scope.totalItemsCount = data.count;
                }
                $scope.itemsFrom = ($scope.currentPage - 1) * $scope.itemsPerPage;

                $scope.itemsFrom += 1;

                $scope.itemsTo = $scope.itemsFrom + $scope.itemsPerPage - 1;
                if ($scope.itemsTo > $scope.totalItems) {
                    $scope.itemsTo = $scope.totalItems;
                }

                $scope.foundedItemsCount = data.count;
            });
        };
        $scope.$watch("currentPage", function () {
            $scope.getLunchedProcessList();
        });
        $scope.$watch("itemsPerPage", function () {
            $scope.getLunchedProcessList();
        });

        $scope.clearAllTimeouts = function () {
            for (var i = 0; i < $scope.timeouts.length; i++) {
                clearTimeout($scope.timeouts[i])
            }
        };
        $scope.searchLunchedProcess = function () {
            $scope.clearAllTimeouts();
            $scope.timeouts.push(
                setTimeout($scope.getLunchedProcessList, 1500)
            );

        };
    });
angular.module('AniTheme').controller('ModalLunchedProcessCreateInstanceCtrl', function ($scope, $modalInstance, $http,bpmnService, $translate, LunchedProcessService) {

    $scope.bpmns = {};
    $scope.current= {};
    $scope.lunchedProcess = {};
           bpmnService.getCurrent(0).success(function (data) {
                $scope.current = data;

            });
            bpmnService.listBpmns( $scope.current.company,1,undefined,99).success(function (data) {
                $scope.bpmns = data['results'];

            });    $scope.saveLunchedProcess = function () {
        LunchedProcessService.createLunchedProcess($scope.lunchedProcess).success(function (data) {
            $modalInstance.close('u did it with success');
        }).error(function (data) {
            $scope.errors = data.message;
        });
    };
    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
});