'use strict';


angular.module('AniTheme')
	.directive('sidebarProfile',function(){
		return {
        templateUrl:'/scripts/directives/sidebar/sidebarwidgets/sidebarprofile',
        restrict: 'E',
        replace: true,
    	}
	});
