'use strict';

angular.module('AniTheme').filter('jalaliDate', function () {
    return function (inputDate, format) {
        if (inputDate) {
            inputDate = new Date(inputDate);
            var date = moment(inputDate);
            //return date.fromNow()+" "+date.format(format);
            return date.format(format);
        }
    }
});
angular.module('AniTheme').filter('jalaliDateFromNow', function () {
    return function (inputDate, format) {
        if (inputDate) {
            inputDate = new Date(inputDate);
            var date = moment(inputDate);
            return date.fromNow();
            //return date.format(format);
        }
    }
});
