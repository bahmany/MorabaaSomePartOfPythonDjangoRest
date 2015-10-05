'use strict';

angular.module('AniTheme')
.directive('topnav',function(){
		return {
	    templateUrl:'/scripts/directives/topnav/',
	    restrict: 'E',
	    replace: true,
	    controller: function($scope){

        	$scope.showMenu = function(){

		        $('.dashboard-page').toggleClass('push-right');

        	}
        	$scope.changeTheme = function(setTheme){

				$('<link>')
				  .appendTo('head')
				  .attr({type : 'text/css', rel : 'stylesheet'})
				  .attr('href', '{% static "ani-theme/styles/app-'+setTheme+'.css" %}');

				// $.get('/api/change-theme?setTheme='+setTheme);

			}
			$scope.rightToLeft = function(){
				$('body').toggleClass('rtl');

				// var t = $('body').hasClass('rtl');
				// console.log(t);
				
				if($('body').hasClass('rtl')) {
					$('.stat').removeClass('hvr-wobble-horizontal');
				}
				

			}


			
        }
	}
});
