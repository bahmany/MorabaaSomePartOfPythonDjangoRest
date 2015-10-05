'use strict';


angular.module('AniTheme').controller('companyTableCtrl', function ($scope,
                                                                    $translate,
                                                                    $rootScope,
                                                                    $modal,
                                                                    CompanyCRUDService) {


//$scope.CompanyCRUDService = $injector.get("CompanyCRUDService");
    $scope.timeouts = [];
    $scope.currentPage = 1;
    $scope.maxSize = 5;
    $scope.itemsPerPage = 14;
    $scope.getCompaniesList = function () {

        CompanyCRUDService.findPagedAll(
            "/myapi/companies/",
            $scope.currentPage,
            $scope.maxSize,
            $scope.itemsPerPage,
            $scope.searchInput
        ).success(function (data) {
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
            })
    };
    $scope.$watch("currentPage", function () {
        $scope.getCompaniesList();
    });
    $scope.$watch("itemsPerPage", function () {
        $scope.getCompaniesList();
    });
    $scope.clearAllTimeouts = function () {
        for (var i = 0; i < $scope.timeouts.length; i++) {
            clearTimeout($scope.timeouts[i])
        }
    };
    $scope.searchCompany = function () {
        $scope.clearAllTimeouts();
        $scope.timeouts.push(
            setTimeout($scope.getCompaniesList, 1500)
        );

    };
    $scope.createCompany = function () {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: 'GenericModalCompanyPost.html',
            controller: 'ModalCompanyPostInstanceCtrl',
            size: '',
            resolve: {
                company: function () {
                    return {};
                }
            }
        });
        modalInstance.result.then(function (res) {
            $scope.getCompaniesList();
        }, function () {

        });
    };
    $scope.companyEdit = function (companyID) {
        CompanyCRUDService.FindBy(
            "/api/v1/company/",
            companyID
        ).success(function (data) {
                $scope.company = data;
                var modalInstance = $modal.open({
                    animation: true,
                    templateUrl: 'GenericModalCompanyPost.html',
                    controller: 'ModalCompanyPostInstanceCtrl',
                    size: '',
                    resolve: {
                        company: function () {
                            return $scope.company;
                        }
                    }
                });
                modalInstance.result.then(function (res) {
                    $scope.getCompaniesList();
                }, function () {
                });
            });

    };
    $scope.companyDelete = function (companyID) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            cancelButtonText: "No, cancel plx!",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function (isConfirm) {
            if (isConfirm) {
                CompanyCRUDService.doDelete(
                    "/api/v1/company/" + companyID + "/").success(
                    function (data) {
                        swal("Deleted!", "Your imaginary file has been deleted.", "success");
                        $scope.getCompaniesList();
                    }).error(function (data) {
                        swal("Oops...", data.detail + " Default company is not deletable", "error");
                    });
            } else {
                swal("Cancelled", "Your imaginary file is safe :)", "error");
            }
        });

    };
});


angular.module('AniTheme').controller('ModalCompanyPostInstanceCtrl',
    function ($scope,
              $modalInstance,
              $translate,
              company,
              CompanyCRUDService) {
        $scope.company = company;
        $scope.saveCompany = function () {
            if (!$scope.company.hasOwnProperty("id")) { // new
                CompanyCRUDService.doInsert("/api/v1/company/", company)
                    .success(function () {
                        $modalInstance.close('u did it with success');
                    }).error(function (data) {
                        $scope.errors = data;
                    })
            } else { //edit
                CompanyCRUDService.doUpdate("/api/v1/company/" + $scope.company.id + "/", $scope.company)
                    .success(function () {
                        $modalInstance.close('u did it with success');
                    }).error(function (data) {
                        $scope.errors = data;
                    })
            }
        };
        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
    });

