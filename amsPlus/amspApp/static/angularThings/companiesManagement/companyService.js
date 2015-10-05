(function () {
    'use strict';

    angular
        .module('AniTheme')
        .service('CompanyCRUDService',
        ['$cookies', '$http', '$location',
            function ($cookies, $http, $location) {


            this.findByUrl = "";
            this.doUpdateUrl = "";
            this.doInsertUrl = "";
            this.doDeleteUrl = "";


            this.FindBy = function (url, id) {
                return $http.get(url+id+"/")

            };

            this.findPagedAll = function (url,currentPage,maxSize,itemPerPage,query) {
                return $http.get(
                    url +
                    '?page=' + currentPage +
                    '&query=' + query +
                    '&itemPerPage=' + itemPerPage) };

            this.doInsert = function (url, newObj) {
                return $http.post(url, newObj)
            };
            this.doUpdate = function (url, newObj) {
                return $http.put(url, newObj)
            };

            this.doDelete = function (url) {
                return $http.delete(url)
            };

        }]);





})();



