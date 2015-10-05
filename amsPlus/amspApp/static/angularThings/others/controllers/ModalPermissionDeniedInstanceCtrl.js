'use strict';

angular.module('AniTheme').controller('ModalPermissionDeniedInstanceCtrl', function ($scope, $modalInstance, $http) {

    $scope.ok = function () {
        $modalInstance.dismiss('ok');

    };
});
