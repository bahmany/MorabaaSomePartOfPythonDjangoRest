'use strict';

angular.module('AniTheme').directive('htmlText', function(){
  return {
    'restrict': 'A',
    'require': 'ngModel',
    'link': function(scope,element,attrs,model) {
      model.$formatters.push(function(val){
        return val.htmlField;
      });

      model.$parsers.push(function(val){
        model.$modelValue.htmlField = val;
      });
    } 
  };
});