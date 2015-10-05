'use strict';


angular.module('AniTheme').controller(
    'FriendsCtrl',
    function ($scope,
              $translate,
              $q,
              $rootScope,
              $modal,
              FriendsService) {


        $scope.GetProfiles = function () {
            $scope.isSearchCallbackCompleted = false;
            FriendsService.GetProfiles($scope.ProfileSearchText).success(function (data) {
                $scope.SearchPersons = data;
                $scope.isSearchCallbackCompleted = true;
            }).error(function (data) {
                $scope.isSearchCallbackCompleted = true;
            })
        };
        $scope.ProfileSearch = "";

        $scope.ProfilePageTo = function (PageUrl) {
            $scope.isSearchCallbackCompleted = false;

            FriendsService.GetProfileListByPager($scope.ProfileSearch, PageUrl).success(function (data) {
                $scope.isSearchCallbackCompleted = true;
                $scope.SearchPersons = data;
            }).error(function (data) {
                $scope.isSearchCallbackCompleted = true;
            });
        };


        $scope.GetProfiles();


        $scope.isSearchCallbackCompleted = true;


        $scope.$watch("ProfileSearchText", function () {
            $scope.GetProfiles();
        });


        $scope.SelectedPerson = {};
        $scope.OpenInviteModal = function (person) {
            $scope.SelectedPerson = person;
            // here i have some points
            // when i click on a user
            // i can see all of my invitations !!
            // so invitations is not company based
            FriendsService.GetMemberInvitations(person.id).success(function (data) {
                $("#profileList").removeClass("col-md-12").addClass("col-md-7");
                $("#invList").removeClass("hide").addClass("show");
                $scope.GetUserInvitations();
            })
        };
        $scope.SearchPersons = {};
        $scope.GetCompanyMembers = function (companyID) {
            FriendsService.GetCompanyMembers(companyID).success(function (data) {
                $scope.SearchPersons = data.results;
            });
        };
        $scope.CloseInvModal = function () {
            $("#invList").removeClass("show").addClass("hide");
            $("#profileList").removeClass("col-md-7").addClass("col-md-12");
        }
        $scope.ChartSimpleList = {};
        $scope.ChartSearch = "";
        $scope.GetCompanyChartList = function () {
            FriendsService.GetAllChartList($scope.ChartSearch).success(function (data) {
                $scope.ChartSimpleList = data;
            });
        };
        $scope.$watch("ChartSearch", function () {
            $scope.GetCompanyChartList();
        });
        $scope.GetCompanyChartList();
        $scope.ChartPageTo = function (PageUrl) {
            FriendsService.GetChartListByPager($scope.ChartSearch, PageUrl).success(function (data) {
                $scope.ChartSimpleList = data;
            });
        };

        $scope.OpenCompanyMembers = function (item) {
            $scope.SelectedCompanyID = item;
            $scope.GetCompanyMembers(item);
            $scope.GetCompanyChartList(item);
        };

        $scope.SearchChart = "";

        $scope.$watch("InvitationsSearch", function () {
            $scope.GetUserInvitations();
        });

        $scope.GetUserInvitations = function (searchStr) {
            FriendsService.GetUserInvitations(
                $scope.SelectedPerson.id, $scope.InvitationsSearch
            ).success(function (data) {
                    $scope.Invitations = data;

                    for (var j = 0; j < $scope.ChartSimpleList.results.length; j++) {
                        $scope.ChartSimpleList.results[j].selected = false;
                    }


                    for (var i = 0; i < data.results.length; i++) {
                        for (var j = 0; j < $scope.ChartSimpleList.results.length; j++) {
                            if (
                                data.results[i].chart == $scope.ChartSimpleList.results[j].id
                            ) {
                                if (
                                    data.results[i].isEmpty == $scope.ChartSimpleList.results[j].isEmpty &&
                                    data.results[i].positionID == $scope.ChartSimpleList.results[j].positionID
                                ) {
                                    $scope.ChartSimpleList.results[j].selected = true;
                                } else {
                                    if
                                    (data.results[i].positionID == undefined) {
                                        $scope.ChartSimpleList.results[j].selected = true;
                                    }
                                }
                            }
                        }
                    }

                })
        };
        $scope.Invitations = [];
        $scope.RemoveInvitation = function (inv) {
            swal({
                title: "Are you sure?",
                text: "Are you ready to remove this invitation ?",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, delete it!",
                closeOnConfirm: false, showLoaderOnConfirm: true
            }, function () {
                FriendsService.RemoveInvitation($scope.SelectedPerson.id, inv.id).success(function (data) {
                    $scope.GetUserInvitations();
                    swal("Deleted!", "Your imaginary file has been deleted.", "success");

                });
            });

        };
        $scope.SelectedChart = {};
        $scope.SelectDeselectChart = function (chart) {
            $scope.SelectedChart = chart;
            $scope.InvitationsSearch = "";
            FriendsService.SelectDeselectChart(
                parseInt(chart.CompanyID),
                chart.id,
                $scope.SelectedPerson.id,
                chart.selected,
                chart.isEmpty,
                chart.positionID
            ).success(function (data) {
                    $scope.GetUserInvitations();
                });
        };


        $scope.ApproveInvitation = function (invitation) {
            FriendsService.ApproveInvitation(
                invitation.id
            ).success(function (data) {
                    $scope.GetUserInvitations();
                    $scope.GetCompanyChartList()
                    swal("Updated", "Completed..", "success");
                }).error(function (data) {
                    swal("Error", data.message, "error");
                });
        };


    });