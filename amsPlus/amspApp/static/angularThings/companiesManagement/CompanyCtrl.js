'use strict';
angular.module('AniTheme')
    .controller('CompanyCtrl', function ($scope, $http, $translate, $rootScope,$stateParams, $location, $modal, companiesManagmentService) {
        $scope.companyId=$stateParams.companyid;

    });
