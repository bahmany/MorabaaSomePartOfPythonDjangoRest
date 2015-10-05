'use strict';


angular.module('AniTheme')
    .controller('groupTableCtrl', function ($scope, $http, $translate, $rootScope, $modal) {

        $scope.groups = {};
        $scope.group = {};
        $scope.newGroup = {};
        $scope.oldGroup = {};
        $scope.timeouts = [];
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.itemsPerPage = 14;

        //it's for get edit form field data
        $scope.groupFunc = function (username) {
            $http.get('/api/v1/groups/' + username + '/').success(function (data) {

                $scope.group.name = data['name'];
                $scope.group.permissions = data['permissions'];
                $scope.group.user_set = data['user_set'];
                $scope.oldGroup.name = data['name'];
            });
        };
        $scope.groupEdit = function (username) {

            $scope.groupFunc(username);

            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalGroupEdit.html',
                controller: 'ModalGroupEditInstanceCtrl',
                size: '',
                resolve: {
                    group: function () {
                        return $scope.group;
                    },
                    groupOld: function () {
                        return $scope.oldGroup;
                    }
                }
            });

            modalInstance.result.then(function (res) {
                $scope.getGroupsList();
            }, function () {

            });
        };


        $scope.createGroup = function () {


            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalGroupCreate.html',
                controller: 'ModalGroupCreateInstanceCtrl',
                size: '',
                resolve: {}
            });

            modalInstance.result.then(function (res) {
                $scope.getGroupsList();
            }, function () {

            });
        };


        $scope.groupDelete = function (username) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalAreYouSure.html',
                controller: 'ModalAreYouSureInstanceCtrl',
                size: '',
                resolve: {}
            });
            modalInstance.result.then(function (selectedItem) {
                $http.delete('/api/v1/groups/' + username + '/').success(function (data) {
                    $scope.getGroupsList();
                }).error(function (data) {
                    var modalInstance = $modal.open({
                        animation: true,
                        templateUrl: 'GenericModalPermissionDenied.html',
                        controller: 'ModalPermissionDeniedInstanceCtrl',
                        size: '',
                        resolve: {}
                    });
                });

            }, function () {
            });

        };


        $scope.getGroupsList = function () {
            $http.get('/myapi/groups/?page=' + $scope.currentPage + '&query=' + $scope.searchInput + '&itemPerPage=' + $scope.itemsPerPage).success(function (data) {
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
            });
        };
        $scope.$watch("currentPage", function () {
            $scope.getGroupsList();
        });
        $scope.$watch("itemsPerPage", function () {
            $scope.getGroupsList();
        });

        $scope.clearAllTimeouts = function () {
            for (var i = 0; i < $scope.timeouts.length; i++) {
                clearTimeout($scope.timeouts[i])
            }
        };
        $scope.searchGroup = function () {
            $scope.clearAllTimeouts();
            $scope.timeouts.push(
                setTimeout($scope.getGroupsList, 1500)
            );

        };
    });
angular.module('AniTheme').controller('ModalGroupEditInstanceCtrl', function ($scope, $modalInstance, $http, $translate, group, groupOld) {
    $scope.group = group;
    $scope.groupOld = groupOld;
    $scope.timeouts = [];

    $scope.permissionsFunc = function () {
        $http.get('/myapi/permission/?query=' + $scope.permissionSearchInput).success(function (data) {
            $scope.permissionsOptions = data;
        });
    };
    $scope.clearAllTimeouts = function () {
        for (var i = 0; i < $scope.timeouts.length; i++) {
            clearTimeout($scope.timeouts[i])
        }
    };
    $scope.searchPermissions = function () {
        $scope.clearAllTimeouts();
        $scope.timeouts.push(
            setTimeout($scope.permissionsFunc, 1500)
        );

    };
    $scope.usersFunc = function () {
        $http.get('/myapi/users/?query=' + $scope.userSearchInput + '&itemPerPage=50&page=1').success(function (data) {
            $scope.userOptions = data['results'];
        });
    };
    $scope.searchUsers = function () {
        $scope.clearAllTimeouts();
        $scope.timeouts.push(
            setTimeout($scope.usersFunc, 1500)
        );

    };

    $scope.permissionsFunc();
    $scope.usersFunc();


    $scope.saveGroupEdit = function () {
        $http.put('/api/v1/groups/' + $scope.groupOld.name + '/', $scope.group).success(function (data) {
            if ((data.id) || (data.id != 'undefined') || (data.id != '')) {

                $modalInstance.close('u did it with success');
            }

        }).error(function (data) {
            $scope.errors = data;
        });

    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
});
angular.module('AniTheme').controller('ModalGroupCreateInstanceCtrl', function ($scope, $modalInstance, $http, $translate) {

    $scope.saveGroup = function () {

        $http.post('/api/v1/groups/', $scope.group).success(function (data) {
            $modalInstance.close('u did it with success');

        }).error(function (data) {
            $scope.errors = data;
        });
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
});
