'use strict';

angular.module('AniTheme')
    .directive('sidebar', function () {
        return {
            templateUrl: '/scripts/directives/sidebar/',
            restrict: 'E',
            replace: true,

            controller: function ($scope) {
                $(function () {
                    Calendar.setup({
                        inputField: "date_input_7",
                        displayArea: "display_area_1",
                        flat: "flat_calendar_1",   // id of the input field
                        ifFormat: "%Y-%m-%d",       // format of the input field
                        dateType: 'jalali',
                        weekNumbers: true
                    });
                });
                setTimeout(function () {
                    $('.sidenav-outer').perfectScrollbar();
                }, 100);

            }


        }
    });
