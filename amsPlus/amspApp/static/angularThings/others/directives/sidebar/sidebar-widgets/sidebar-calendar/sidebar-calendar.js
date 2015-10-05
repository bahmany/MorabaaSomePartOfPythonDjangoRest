'use strict';


angular.module('AniTheme')
	.directive('sidebarCalendar',function(){
		return {
        templateUrl:'scripts/directives/sidebar/sidebar-widgets/sidebar-calendar/sidebar-calendar',
        restrict: 'E',
        replace: true,
    	}
	});
