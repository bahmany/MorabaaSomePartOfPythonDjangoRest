'use strict';

angular.module('AniTheme').directive("callCurrentUserProfile", function () {
    return {
        //E = element, A = attribute, C = class, M = comment
        //restrict: "A",
        //require: "ngModel",
        link: function (scope, element, attrs) {
            $.get("/api/v1/profile/get-avatar").success(function (data) {
                $(element).attr("src",data.addr);
            });



        }
    };
});