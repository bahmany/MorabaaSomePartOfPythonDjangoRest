'use strict';

angular.module('AniTheme')
	.directive('sidebarwidgets',function(){
		return {
        templateUrl:'/scripts/directives/sidebar/sidebarwidgets/',
        restrict: 'E',
        replace: true,
	}
});
