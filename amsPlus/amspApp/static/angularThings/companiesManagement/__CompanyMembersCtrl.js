'use strict';
angular.module('AniTheme')
    .controller('CompanyMembersCtrl', function ($scope,$stateParams, $http, $translate, $rootScope, $location, $modal, companiesManagmentService) {

        $scope.SelectedPerson = {};
        $scope.OpenInviteModal = function (person) {
            $scope.SelectedPerson = person;
            // here i have some points
            // when i click on a user
            // i can see all of my invitations !!
            // so invitations is not company based
            companiesManagmentService.GetMemberInvitations(person.id).success(function (data) {
                $scope.GetUserInvitations();

            })
        };
        $scope.SearchPersons = [];
        $scope.GetCompanyMembers = function (companyID) {
            companiesManagmentService.GetCompanyMembers(companyID).success(function (data) {
                $scope.SearchPersons = data.results;


            });
        };
        $scope.ChartSimpleList = [];
        $scope.GetCompanyChartList = function (companyID) {
            companiesManagmentService.GetCompanyChartList(companyID).success(function (data) {
                $scope.ChartSimpleList = data;
            });
        };
        $scope.OpenCompanyMembers = function (item) {

            $scope.SelectedCompanyID = item;
            $scope.GetCompanyMembers(item);
            $scope.GetCompanyChartList(item);
        };
        $scope.OpenCompanyMembers($stateParams.companyid);
        $scope.SearchChart = "";
        $scope.$watch("SearchChart", function () {
            console.log("Hiiii");
        });
        $scope.GetUserInvitations = function (searchStr) {
            companiesManagmentService.GetUserInvitations(
                $scope.SelectedPerson.id, searchStr
            ).success(function (data) {
                    $scope.Invitations = data;
                    for (var j = 0; j < $scope.ChartSimpleList.results.length; j++) {
                        $scope.ChartSimpleList.results[j].selected = false;
                    }
                    for (var i = 0; i < data.results.length; i++) {

                        for (var j = 0; j < $scope.ChartSimpleList.results.length; j++) {
                            if (data.results[i].chart == $scope.ChartSimpleList.results[j].id) {
                                $scope.ChartSimpleList.results[j].selected = true;

                            }
                        }
                    }

                })
        };
        $scope.Invitations = [];
        $scope.RemoveInvitation = function (inv) {
            companiesManagmentService.RemoveInvitation($scope.SelectedPerson.id, inv.id).success(function (data) {
                $scope.GetUserInvitations();
            });
        };
        $scope.SelectDeselectChart = function (chart) {
            companiesManagmentService.SelectDeselectChart(
                $scope.SelectedCompanyID,
                chart.id,
                $scope.SelectedPerson.id,
                chart.selected
            ).success(function (data) {
                    $scope.GetUserInvitations();
                    //$scope.SearchPersons = data.results;
                });
        };


    });
