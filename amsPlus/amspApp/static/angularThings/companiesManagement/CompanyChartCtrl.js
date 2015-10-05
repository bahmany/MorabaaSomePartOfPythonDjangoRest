'use strict';
angular.module('AniTheme')
    .controller('CompanyChartCtrl', function ($scope, $http, $translate, $rootScope, $stateParams, $location, $modal,
                                              companiesManagmentService) {


        $scope.ChartSimpleList = [];
        $scope.Zone = {};
        $scope.Zones = [];
        $scope.SelectedZones = [];
        $scope.SelectedChartID = 0;
        $scope.SecratraitsList = [];
        $scope.SelectedCompanyID = $stateParams.companyid;



        $scope.GetZoneList = function () {
            //debugger;
            companiesManagmentService.GetZones($scope.SelectedCompanyID, selectedItem.id).success(function (data) {
                $scope.Zones = data;
            })
        };

        $scope.UpdatePerSec = function (item) {

            companiesManagmentService.UpdateSecPer($scope.SelectedCompanyID,$scope.SelectedChartID, item).success(function (data) {

            })
        }

        $scope.UpdatePerSecWithSelect = function (item,ii, index) {
            item.perm[index] = ii;
            $scope.UpdatePerSec(item);

        }



        $scope.CheckOtherSecPer = function (item) {
            for (var i=0; $scope.SecratraitsList.length > i;i++){
                if (item.Id != $scope.SecratraitsList[i].Id){
                    $scope.SecratraitsList[i].default = false;
                }
            }

            $scope.UpdatePerSec(item);



        };

        $scope.GetSecList = function (chartID) {
            companiesManagmentService.GetSecByChartPos($scope.SelectedCompanyID,chartID).success(function (data) {
                $scope.SecratraitsList = data;
            })
        };

        $scope.OpenCompanyChart = function (item) {

            $scope.SelectedCompanyID = item;
            companiesManagmentService.GetChart(item);
            companiesManagmentService.GetZones($scope.SelectedCompanyID, "0").success(function (data) {
                $scope.Zones = data;
            })


        };



        $scope.GetCompanyChartList = function (companyID) {
            companiesManagmentService.GetCompanyChartList(companyID).success(function (data) {
                $scope.ChartSimpleList = data;
            });
        };
        $scope.OpenCompanyChart($stateParams.companyid);

        $scope.NewZone = function () {

            swal(
                {
                    title: "New Zone",
                    text: "Enter your new zone name",
                    type: "input",
                    showCancelButton: true,
                    closeOnConfirm: false,
                    animation: "slide-from-top",
                    inputPlaceholder: "Write Zone Name"
                },
                function (inputValue) {
                    if (inputValue === false)
                        return false;
                    if (inputValue === "") {
                        swal.showInputError("Zone name is require");
                        return false
                    }
                    $scope.Zone.title = inputValue;
                    $scope.Zone.company = $scope.SelectedCompanyID.toString();
                    companiesManagmentService.PostZone($scope.SelectedCompanyID, $scope.Zone).success(
                        function (data) {
                            $scope.GetZoneList();
                            swal(
                                "Nice!",
                                "" + data.name + " added !",
                                "success");
                        }
                    ).error(
                        function (err) {
                            swal.showInputError(err.name[0]);
                        }
                    )

                });
        };

        $scope.DeleteZone = function (zone, index) {
            swal({
                title: "Are you sure?",
                text: "You will not be able to recover this imaginary file!",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, delete it!",
                showLoaderOnConfirm: true,
                closeOnConfirm: false
            }, function () {
                companiesManagmentService.DeleteZone($scope.SelectedCompanyID, zone.selectedChartID, zone.id).success(function (data) {
                    $scope.Zones.results.splice(index, 1);
                    swal("Deleted!", "Your imaginary file has been deleted.", "success");
                });


            });
        };

        $scope.ChangeZonesChart = function (zone) {
            //debugger;
            zone.selectedChartID = selectedItem.id;
            companiesManagmentService.ChangeZone(zone.selectedChartID, zone).success(function (data) {

            });
        };


        $scope.EditZone = function (zone, index) {
            swal({
                title: "An input!",
                text: "Write something interesting:",
                type: "input",
                inputValue: zone.title,
                showCancelButton: true,
                closeOnConfirm: false,
                animation: "slide-from-top",
                inputPlaceholder: "Write something"
            }, function (inputValue) {
                if (inputValue === false) return false;
                if (inputValue === "") {

                    swal.showInputError("You need to write something!");
                    return false
                }
                zone.title = inputValue;
                companiesManagmentService.EditZone($scope.SelectedCompanyID, zone).success(function (data) {
                    swal("Nice!", "You wrote: " + inputValue, "success");

                });
            });
        };

    });
