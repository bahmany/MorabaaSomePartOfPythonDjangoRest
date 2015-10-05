'use strict';

/**
 * @ngdoc function
 * @name AniTheme.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of AniTheme
 */
angular.module('AniTheme').controller('PaginationCtrl', function ($scope, $log) {
  $scope.totalItems = 64;
  $scope.currentPage = 4;
alert('sdf');
  $scope.setPage = function (pageNo) {
    $scope.currentPage = pageNo;
      alert('sdf');
  };
 $scope.electPage = function (pageNo) {
    $scope.currentPage = pageNo;
      alert('sdf');
  };
  $scope.pageChanged = function() {
    $log.log('Page changed to: ' + $scope.currentPage);
  };

  $scope.maxSize = 7;
  $scope.bigTotalItems = 175;
  $scope.bigCurrentPage = 1;
});