'use strict';
//angular.module('AniTheme').controller('UploadImageModalInstance', function ($scope, $modalInstance, Upload) {
//
//    $scope.image = 'img/default.png';
//
//    $scope.progress = 0;
//    $scope.files = [];
//
//    $scope.upload = function () {
//        Upload.upload({
//            url: 'api/upload',
//            fields: {'dir': 'img/uploads/'},
//            file: $scope.files[0],
//            method: 'POST'
//        }).progress(function (evt) {
//            $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
//        }).success(function (data) {
//            $scope.progress = 0;
//            $scope.image = data.dir + data.filename;
//        });
//    };
//    $scope.insert = function () {
//        $modalInstance.close($scope.image);
//    };
//});


angular.module('AniTheme').controller(
    'LetterComposeCtrl',
    function ($scope,
              $translate,
              $q,
              $http,
              $rootScope,
              $modal,
              LetterInboxService,
              LetterComposeService) {

        $scope.finalList = [];


        $scope.loadRecieverPanel = function () {
            memberInbox($scope, $http);
            chartInbox($scope, $http);
            zoneInbox($scope, $http);
            groupInbox($scope, $http);
        };

        $scope.loadPanel = function (panelName) {
            $(".hideIt").hide();
            $("#"+panelName).show();

        }

        $scope.selectPositions = function () {
            $scope.loadPanel("divSelects");
            $scope.loadRecieverPanel();
        }


    });
