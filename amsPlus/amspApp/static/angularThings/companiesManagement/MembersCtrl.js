'use strict';


angular.module('AniTheme')
    .controller('CompanyMembersCtrl', function ($scope, $http, $stateParams, $translate, $rootScope, $location, $modal, CompanyMembersService) {

        $scope.Members = [];
        $scope.MemberSearchText = '';
        $scope.SelectedPersonID = "";
        $scope.ChartCompanyID = $stateParams.companyid;
        $scope.ChartSimpleList = [];
        $scope.SearchChartList = "";
        $scope.SelectedPerson = {};
        $scope.SelectedNewChart = {};
        $scope.isSearchCallbackCompleted = true;

        $scope.GetMembers = function (companyId) {
            $scope.isSearchCallbackCompleted = false;
            CompanyMembersService.searchMembers(companyId, $scope.MemberSearchText).success(function (data) {
                $scope.Members = data;
                $scope.isSearchCallbackCompleted = true;
            }).error(function (data) {
                $scope.isSearchCallbackCompleted = true;

            });
        };

        $scope.$watch("MemberSearchText", function () {
            $scope.GetMembers($stateParams.companyid);
        });
        $scope.GetMembers($stateParams.companyid);

        $scope.ForceOut = function (item) {

            swal({
                title: "Are you sure?",
                text: "This user access to his inbox will be lost",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, remove it!",
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            }, function () {
                $scope.SelectedPerson = item;
                CompanyMembersService.ForceOutSrv($stateParams.companyid, {
                    profileID: $scope.SelectedPerson.id,
                    chartID: $scope.SelectedPerson.chartID,
                    userID: $scope.SelectedPerson.userID,
                    positionID: $scope.SelectedPerson.positionID,
                    companyID: $scope.SelectedPerson.companyID
                }).success(function (data) {
                    $scope.GetMembers($stateParams.companyid);
                    swal("Removed!", "Selected users removed from the selected chart.", "success");
                });
            });
        };

        $scope.RemoveInbox = function (item) {
            swal({
                title: "Danger!!",
                text: "By removing this, old letter in the inbox will be gone forever",
                type: "warning",
                showCancelButton: true,
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            }, function () {
                console.log(item);
                CompanyMembersService.RemoveFromInbox($stateParams.companyid, item).success(function () {
                    $scope.GetMembers($stateParams.companyid);
                    swal("Removed!", "Successfully removed", "success");

                })


            });
        }


        //----------------------------------------------------------------------------------
        $scope.GetCompanyChartList = function (companyID, searchStr) {
            $scope.isSearchCallbackCompleted = false;
            CompanyMembersService.GetCompanyChartList(companyID, searchStr, 1).success(function (data) {
                $scope.isSearchCallbackCompleted = true;
                $scope.ChartSimpleList = data;
            }).error(function () {
                $scope.isSearchCallbackCompleted = true;
            });
        };
        $scope.$watch("SearchChartList", function () {
            $scope.GetCompanyChartList($scope.ChartCompanyID, $scope.SearchChartList)
        });
        $scope.ChartPageTo = function (PageUrl) {
            CompanyMembersService.GetCompanyChartListByPager($scope.SearchChartList, PageUrl).success(function (data) {
                $scope.ChartSimpleList = data;
                for (var i = 0; $scope.ChartSimpleList.results.length > i; i++) {
                    if ($scope.ChartSimpleList.results[i].id == $scope.SelectedPerson.chartID &&
                        $scope.ChartSimpleList.results[i].isEmpty != $scope.SelectedPerson.isEmpty
                    ) {
                        $scope.ChartSimpleList.results[i].selected = true;

                    } else {
                        $scope.ChartSimpleList.results[i].selected = false;
                    }
                }
            });
        };
        $scope.SelectDeselectChart = function (chart) {
            if (chart.selected) {
                $scope.SelectedNewChart = chart;
            } else {
                $scope.SelectedNewChart.selected = false;
            }
            for (var i = 0; $scope.ChartSimpleList.results.length > i; i++) {
                if ($scope.ChartSimpleList.results[i].id != chart.id) {
                    $scope.ChartSimpleList.results[i].selected = false;
                }
            }
        };
        $scope.LoadChart = function (person) {
            $scope.SelectedPerson = person;
            CompanyMembersService.GetCompanyChartList($scope.ChartCompanyID, "", 1).success(function (data) {
                $scope.ChartSimpleList = data;
                for (var i = 0; $scope.ChartSimpleList.results.length > i; i++) {
                    if ($scope.ChartSimpleList.results[i].id == $scope.SelectedPerson.chartID) {
                        $scope.ChartSimpleList.results[i].selected = true;

                    } else {
                        $scope.ChartSimpleList.results[i].selected = false;
                    }
                }
                $("#companyChart").show();
            });
        };
        $scope.PostPostionSelect = function () {
            if ($scope.SelectedNewChart.selected == false) {
                swal("Not Selected", "Please Select a chart item to apply", "error");
                return;
            }
            swal({
                title: "Are ready ?",
                text: "After changing position, previous account will not be able to see this charts letter",
                type: "info",
                showCancelButton: true,
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            }, function () {
                CompanyMembersService.UpdatePosition(
                    $scope.ChartCompanyID,
                    $scope.SelectedPerson.userID,
                    $scope.SelectedNewChart.id,
                    $scope.SelectedPerson.chartID,
                    $scope.SelectedPerson.id
                ).success(function (data) {
                        $scope.GetMembers($scope.ChartCompanyID);
                        swal("Updated", "success", "success");
                        $("#companyChart").fadeOut(100)
                    });
            });
        };

        $scope.CancelPostionSelect = function () {
            $("#companyChart").fadeOut(100);
        };
        //----------------------------------------------------------------------------------


    }
)
;
