'use strict';


angular.module('AniTheme')
    .controller('userTableCtrl', function ($scope, $http, $translate, $rootScope, $modal) {

        $scope.users = {};
        $scope.user = {};
        $scope.oldUser = {};
        $scope.timeouts = [];
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.itemsPerPage = 14;

        //it's for get edit form field data
        $scope.userFunc = function (username) {
            $http.get('/api/v1/users/' + username + '/').success(function (data) {
                $scope.user.username = data['username'];
                $scope.user.email = data['email'];
                $scope.user.is_active = data['is_active'];
                $scope.user.user_permissions = data['user_permissions'];
                $scope.user.groups = data['groups'];
                $scope.oldUser.username = data['username'];
            });
        };
        $scope.userEdit = function (username) {

            $scope.userFunc(username);

            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalUserEdit.html',
                controller: 'ModalUserEditInstanceCtrl',
                size: '',
                resolve: {
                    user: function () {
                        return $scope.user;
                    },
                    userOld: function () {
                        return $scope.oldUser;
                    }
                }
            });

            modalInstance.result.then(function (res) {
                $scope.getUsersList();
            }, function () {

            });
        };
        $scope.userDelete = function (username) {

            $scope.userFunc(username);
            $scope.user.action = 'delete';
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalAreYouSure.html',
                controller: 'ModalAreYouSureInstanceCtrl',
                size: '',
                resolve: {

                }
            });
            modalInstance.result.then(function (selectedItem) {
                $http.put('/api/v1/users/' + username + '/', $scope.user).success(function (data) {
                    $scope.user.action = '';

                    $scope.getUsersList();

                }).error(function (data) {
                    var modalInstance = $modal.open({
                        animation: true,
                        templateUrl: 'GenericModalPermissionDenied.html',
                        controller: 'ModalPermissionDeniedInstanceCtrl',
                        size: '',
                        resolve: {

                        }
                    });
                });

            }, function () {
            });


        };
        $scope.passEdit = function (username) {

            $scope.userFunc(username);

            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalPassEdit.html',
                controller: 'ModalPassInstanceCtrl',
                size: '',
                resolve: {
                    user: function () {
                        return $scope.user;
                    }
                }
            });

            modalInstance.result.then(function (res) {
            }, function () {

            });
        };
        $scope.userPassive = function (username) {

            $scope.userFunc(username);
            $scope.user.action = 'passive/active';
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'GenericModalAreYouSure.html',
                controller: 'ModalAreYouSureInstanceCtrl',
                size: '',
                resolve: {

                }
            });
            modalInstance.result.then(function (selectedItem) {

                $http.put('/api/v1/users/' + username + '/', $scope.user).success(function (data) {
                    $scope.user.action = '';

                    $scope.getUsersList();

                }).error(function (data) {
                    var modalInstance = $modal.open({
                        animation: true,
                        templateUrl: 'GenericModalPermissionDenied.html',
                        controller: 'ModalPermissionDeniedInstanceCtrl',
                        size: '',
                        resolve: {

                        }
                    });
                });
            }, function () {
            });


        };
        $scope.getUsersList = function () {
            $http.get('/myapi/users/?page=' + $scope.currentPage + '&query=' + $scope.searchInput + '&itemPerPage=' + $scope.itemsPerPage).success(function (data) {
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
            $scope.getUsersList();
        });
        $scope.$watch("itemsPerPage", function () {
            $scope.getUsersList();
        });

        $scope.clearAllTimeouts = function () {
            for (var i = 0; i < $scope.timeouts.length; i++) {
                clearTimeout($scope.timeouts[i])
            }
        };
        $scope.searchUsers = function () {
            $scope.clearAllTimeouts();
            $scope.timeouts.push(
                setTimeout($scope.getUsersList, 1500)
            );

        };
    });
angular.module('AniTheme').controller('ModalUserEditInstanceCtrl', function ($scope, $modalInstance, $http, user, userOld) {
    $scope.user = user;
    $scope.userOld = userOld;
    $scope.timeouts = [];
    $scope.permissionsFunc = function () {
        $http.get('/myapi/permission/?query=' + $scope.permissionSearchInput).success(function (data) {
            $scope.permissionOptions = data;
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

    $scope.groupsFunc = function () {
        $http.get('/myapi/groups/?query=' + $scope.groupSearchInput + '&page=1&itemPerPage=50').success(function (data) {
            $scope.groupOptions = data['results'];
        });
    };
    $scope.searchGroups = function () {
        $scope.clearAllTimeouts();
        $scope.timeouts.push(
            setTimeout($scope.groupsFunc, 1500)
        );

    };
    $scope.permissionsFunc();
    $scope.groupsFunc();

    $scope.saveUserEdit = function () {
           $scope.user.actoin='';
        $http.put('/api/v1/users/' + $scope.userOld.username + '/', $scope.user).success(function (data) {
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
angular.module('AniTheme').controller('ModalPassInstanceCtrl', function ($scope, $modalInstance, $http, user) {
    $scope.user = user;

    $scope.savePassEdit = function () {
        $scope.user.actoin='';
        $http.put('/api/v1/users/' + $scope.user.username + '/', $scope.user).success(function (data) {
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
