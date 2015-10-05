'use strict';
var globalxml = '';


angular.module('AniTheme')
    .controller('CompanyProcessCtrl', function ($scope, $http, $translate, $rootScope,$state,$stateParams, $modal, $location,bpmnService) {

        $scope.bpmns = {};
        $scope.bpmn = {};
        $scope.oldBpmn = {};
        $scope.timeouts = [];
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.itemsPerPage = 14;
        $('#newbpmn').click(function () {
            $rootScope.bpmnRoot = '';
            $rootScope.bpmnRoot = {};
            globalxml = '';


        });
        // it's for get edit form field data
        $scope.createBpmn = function () {
            $state.go("company.process.new", {companyid:$stateParams.companyid});
        };

        $scope.retrieveBpmn = function (id) {
            bpmnService.retrieveBpmn($stateParams.companyid,id).success(function (data) {
                $scope.bpmn.name = data['name'];
                $scope.bpmn.xml = data['xml'];
                $scope.bpmn.description = data['description'];
                $scope.bpmn.id = data['id'];
                globalxml = data['xml'];
            });
        };
        $scope.bpmnEdit = function (id) {
            $state.go("company.process.edit", {companyid:$stateParams.companyid, processId:id});

        };
        $scope.buildForm = function (id) {
            $rootScope.id = id;
            $state.go("company.process.setup", {companyid:$stateParams.companyid,processId:id});

        };
        $scope.bpmnDelete = function (id) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalAreYouSure.html',
                controller: 'ModalAreYouSureInstanceCtrl',
                size: '',
                resolve: {}
            });
            modalInstance.result.then(function (selectedItem) {
                bpmnService.bpmnDelete($stateParams.companyid,id).success(function (data) {

                    $scope.getBpmnsList();
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

        $scope.getBpmnsList = function () {
            bpmnService.listBpmns($stateParams.companyid,$scope.currentPage, $scope.searchInput, $scope.itemsPerPage).success(function (data) {
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
            $scope.getBpmnsList();
        });
        $scope.$watch("itemsPerPage", function () {
            $scope.getBpmnsList();
        });

        $scope.clearAllTimeouts = function () {
            for (var i = 0; i < $scope.timeouts.length; i++) {
                clearTimeout($scope.timeouts[i])
            }
        };
         //$('.sidenav-outer').perfectScrollbar();

        $scope.searchBpmn = function () {
            $scope.clearAllTimeouts();
            $scope.timeouts.push(
                setTimeout($scope.getBpmnsList, 1500)
            );

        };
    });
