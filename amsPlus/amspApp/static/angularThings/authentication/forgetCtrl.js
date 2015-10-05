'use strict';

angular.module('AniTheme').controller('ForgetCtrl', function ($q, $location, $http, $scope, $stateParams, $rootScope, Authentication) {

    var vm = this;
    //$scope.ForgetEmail = "";

    vm.forgetpass = ForgetPass;
    vm.changepass = ChangePass;
    vm.errors = [];
    vm.NewPass = "";
    vm.ConfirmNewPass = "";


    function ForgetPass() {
        var defer = $q.defer();
        var ccc = $http.post("/myapi/forgetpass/", {
            email: vm.ForgetEmail
        });
        ccc.success(function (data) {
            swal("Recovery Process Done!", "We sent your password reset link in 10 min ...", "success");
            $location.path("/");
            return defer.resolve();
        });
        ccc.error(function (data) {
            return defer.reject("");
        });
        return defer.promise;
    }


    function ChangePass() {
        var defer = $q.defer();
        var dataToPost = {
            newPass: vm.NewPass,
            ConfnewPass: vm.ConfirmNewPass,
            hashed: $stateParams.q
        };

        var ccc = $http.post("/myapi/resetpass/", dataToPost);
        ccc.success(function (data) {
            swal("Recovery Process Done!", "Your password has been changed ...", "success")
            $location.path("/");
            return defer.resolve();
        });
        ccc.error(function (data) {
            swal("Error !!", data.message, "error")

            return defer.reject("");
        });
        return defer.promise;
    }
});

