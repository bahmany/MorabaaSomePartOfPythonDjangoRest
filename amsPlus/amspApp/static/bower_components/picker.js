(function() {
  /*jshint eqnull:true lastsemic:true */
  /*globals angular:true */
  'use strict';

  angular.module('picker', ['ng'])

    .directive('picker', function() {
      return {
        require: ['ngModel', 'picker'],
        compile: function($element, $attrs, ctrls) {
          return {
            pre: function($scope, $element, $attrs, ctrls) {
              var model = ctrls[0],
                  picker = ctrls[1],
                  items = {},
                  lastSetViewValue;

              picker.addItem = addItem;
              picker.updateItem = updateItem;

              // NOTE: model.$viewChangeListeners hook doesn't fire when the model is
              // changed externally
              $scope.$watch(function() { return model.$viewValue },
                viewValueChanged, true /* objectEquality */);

              function addItem(key, notify) {
                var a = items[key] = items[key] || [];
                a.push(notify);
                notify(test(key));
                return unlink;

                function unlink() {
                  a.splice(a.indexOf(notify), 1);
                }
              }

              function updateItem(key, state) {
                var viewValue = angular.copy(model.$viewValue) || [],
                    i = viewValue.length,
                    found;
                while (i--) {
                  if (state && viewValue[i] == key) {
                    found = true;
                    break;
                  }
                  if (!state && viewValue[i] == key)
                    viewValue.splice(i, 1);
                }
                if (state && !found)
                  viewValue.push(key);

                notifyKey(key, state);

                lastSetViewValue = viewValue;
                model.$setViewValue(viewValue);
              }

              function notifyKey(key, state) {
                if (items[key] != null)
                  angular.forEach(items[key], function(notify) { notify(state) });
              }

              function viewValueChanged() {
                if (model.$viewValue === lastSetViewValue)
                  return;
                angular.forEach(items, function(a, key) {
                  notifyKey(key, test(key));
                });
              }

              function test(key) {
                var state = false;
                angular.forEach(model.$viewValue, function(v, i) {
                  if (v == key)
                    state = true;
                });
                return state;
              }
            }};
        },
        controller: function() {}
      };
    })

    .directive('pickerItem', function($timeout) {
      return {
        require: '^picker',
        link: function($scope, $element, $attrs, picker) {
          if ($attrs.value != null)
            init($attrs.value);
          else
            $attrs.$observe('value', once(init));

          function init(value) {
            $element.bind('$destroy', picker.addItem(value, notify));
            $element.bind('change', function() {
              $timeout(function() {
                picker.updateItem(value, $element.prop('checked'));
              });
            });
          }

          function notify(state) {
            $element.prop('checked', state);
          }

          function once(fn) {
            var done;
            return function() {
              if (done)
                return;
              done = true;
              return fn.apply(this, arguments);
            };
          }
        }
      };
    })

    ;
})();