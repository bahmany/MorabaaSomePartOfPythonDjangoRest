
  'use strict';

  angular
    .module('AniTheme')
    .controller('LogoutCtrl', function ($scope, Authentication) {

 var vm = this;

    vm.logout = logout;

    /**
    * @name logout
    * @desc Log the user out
    */
    function logout() {
      Authentication.logout();
    }


  });