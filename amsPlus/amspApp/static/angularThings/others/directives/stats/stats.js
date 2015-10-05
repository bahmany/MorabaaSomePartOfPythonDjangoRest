'use strict';

angular.module('AniTheme')
  .directive('stats',function(){
    return {
        templateUrl:'scripts/directives/stats/',
        restrict: 'E',
        replace: true,
        scope: {
          'icon': '@',
          'value': '@',
          'text': '@',
          'bgclass': '@' ,
          'link': '@',
          'progressValue': '@'
        }
      }
  });


