'use strict';

/**
 * @ngdoc function
 * @name AniTheme.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of AniTheme
 */
angular.module('AniTheme').controller('sidenavCtrl', function ($scope, $location) {
    $scope.selectedMenu = 'dashboard';
    $scope.collapseVar = 0;

    $scope.check = function (x) {

        if (x == $scope.collapseVar)
            $scope.collapseVar = 0;
        else
            $scope.collapseVar = x;
    };
    $scope.multiCheck = function (y) {

        if (y == $scope.multiCollapseVar)
            $scope.multiCollapseVar = 0;
        else
            $scope.multiCollapseVar = y;
    };

});
