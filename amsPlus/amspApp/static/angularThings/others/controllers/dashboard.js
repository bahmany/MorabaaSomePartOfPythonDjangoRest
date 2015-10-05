'use strict';

/**
 * @ngdoc function
 * @name AniTheme.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of AniTheme
 */
angular.module('AniTheme')
    .controller('DashboardCtrl', function ($scope, $state, $translate, $rootScope, $http) {

        $scope.$state = $state;

        $scope.date = new Date();
        $scope.layoutToggler = function (y) {

            if (y == $scope.multiCollapseVar)
                $scope.multiCollapseVar = 0;
            else
                $scope.multiCollapseVar = y;
        };

        $scope.load = (function () {
            $http.get("/api/v1/gettimezone/").success(function (data) {
                var newLoc = data;
                if (data.timezone == "Asia/Tehran") {
                    $scope.changeLanguage("fa");
                }
                if (data.timezone == "Europe/London") {
                    $scope.changeLanguage("en");
                }
            });
        });
        $scope.load();
        $scope.changeLanguage = (function (l) {
            // time to change localization
            var cc = "Asia/Tehran";

            if (l == "fa") {
                cc = "Asia/Tehran";
            }
            if (l == "en") {
                cc = "Europe/London";
            }

            $http.post("/api/v1/timezone/", {
                timezone: cc
            });

            if (l == 'fa') {
                if ($('body').hasClass('rtl')) {
                    $('.stat').removeClass('hvr-wobble-horizontal');
                } else {
                    $('body').addClass('rtl');

                    $('.stat').removeClass('hvr-wobble-horizontal');
                }
            } else {
                $('body').removeClass('rtl');
            }
            $translate.use(l);
        });

    });
angular.module('AniTheme')
    .controller('CurrentCompanyCtrl', function ($scope, $http, $state, $stateParams, $templateCache, $translate, $location, $rootScope, companiesManagmentService) {

        $scope.currentCompany = {};

        $scope.PageTo = function (PagerAddress) {
            companiesManagmentService.GetCompaniesList(PagerAddress).success(
                function (data) {
                    $scope.Companies = data;
                });
        };

        $scope.GetCompaniesList = function () {
            companiesManagmentService.companiesForCurrent().success(
                function (data) {
                    $scope.companies = data;
                });
        };
        $scope.initCurrentCompany = function (CurrentCompanyId, CurrentCompanyName) {
            $scope.currentCompany.name = CurrentCompanyName;
            $scope.currentCompany.id = CurrentCompanyId;
        };
        $scope.setAsCurrent = function (userId, companyId) {
            companiesManagmentService.setAsCurrentService(userId, companyId).success(
                function (data) {

                    window.location.reload();

                });
        };
    });
