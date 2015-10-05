'use strict';

angular.module('AniTheme').controller('RegisterCtrl', function ($location, $scope,$rootScope, Authentication) {

    var vm = this;

    vm.register = register;


    function register() {
        var res = Authentication.register(vm.email, vm.password, vm.password2, vm.username);
        res.error(function (data) {
            $scope.errors= data.message;
        }).success(function (data) {
           var res = Authentication.login(vm.username, vm.password,vm.remember);

        res.error(function(data){
            $scope.errors = data.message;

        }).success(function (data) {
             Authentication.setAuthenticatedUser(data,vm.remember);
            $rootScope.remember = vm.remember;

            $location.path('/dashboard/home');
            window.location.reload();
        });
        });


    }


});

