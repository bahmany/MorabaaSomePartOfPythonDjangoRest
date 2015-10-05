'use strict';
angular.module('AniTheme').controller('ModalAreYouSureInstanceCtrl', function ($scope, $modalInstance, $http) {

    $scope.yes = function () {
        $modalInstance.close('yes');


    };

    $scope.no = function () {
        $modalInstance.dismiss('no');
    };
});