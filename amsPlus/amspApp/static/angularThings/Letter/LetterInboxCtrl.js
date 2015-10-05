'use strict';


angular.module('AniTheme').controller(
    'LetterInboxCtrl',
    function ($scope,
              $translate,
              $q,
              $rootScope,
              $modal,
              $http,
              LetterInboxService) {

        setUpSideBar($scope, $http, $modal);

        $scope.Compose = function () {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'page/letter/compose',
                controller: 'LetterComposeCtrl',
                size: '',
                resolve: {

                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'AniTheme.ForgetPass',
                            files: [
                                '/static/angularThings/Letter/Compose/LetterComposeCtrl.js',
                                '/static/angularThings/Letter/Compose/LetterComposeService.js',
                                '/static/angularThings/Letter/Sidebar/Groups/classChart.js',
                                '/static/angularThings/Letter/Sidebar/Groups/classGroup.js',
                                '/static/angularThings/Letter/Sidebar/Groups/classMember.js',
                                '/static/angularThings/Letter/Sidebar/Groups/classZone.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]

                }
            });
            modalInstance.result.then(function (res) {
                //swal('You add:', res.title, "success");
                //$scope.listLabel();
            }, function () {

            });

        };


    });






