'use strict';

angular.module('AniTheme')
	.directive('menubar',function(){

		return {
        templateUrl:'/scripts/directives/sidebar/menu-bar/',
        restrict: 'E',
        replace: true
    }
});
