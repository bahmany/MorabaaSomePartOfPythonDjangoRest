'use strict';

angular
    .module('AniTheme')
    .controller('LoginCtrl', function ($location, $scope, $cookies, $timeout, $q, Authentication, $rootScope) {


        $scope.authenticate = function () {

            var defer = $q.defer();

            $timeout(function () {

                defer.resolve();

                $timeout(function () {

                }, 600);

            }, 1100);

            return defer.promise;

        };
        var vm = this;
        vm.login = login;
        vm.sendreset = SendReset;
        activate();
        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                $location.path('/');
            }
        }

        function SendReset() {
            console.log($scope.ForgetEmail);
        }

        /**
         * @name login
         * @desc Log the user in
         */
        function login() {
            var res = Authentication.login(vm.username, vm.password, vm.remember);
            var defer = $q.defer();
            res.error(function (data) {
                $scope.errors = data.message;
                return defer.resolve(res);
            }).success(function (data) {
                Authentication.setAuthenticatedUser(data, vm.remember);
                $rootScope.remember = vm.remember;
                $location.url('/dashboard/home');
                return defer.resolve();
            });
            return defer.promise;
        }

    });