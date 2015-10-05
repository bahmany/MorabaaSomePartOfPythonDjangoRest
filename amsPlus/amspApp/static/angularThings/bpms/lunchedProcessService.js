'use strict';

angular
    .module('AniTheme')
    .service('LunchedProcessService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {

            this.listUsers = function (companyId, chartId) {
                return $http.get("/api/v1/companies/" + companyId + "/chart/" + chartId + "/PositionsList/");
            };
            this.listCharts = function (companyId) {
                return $http.get("/api/v1/companies/" + companyId + "/chart/");
            };
            this.retrieveLunchedProcess = function (id) {
                return $http.get("/api/v1/LunchedProcess/" + id + "/");
            };
            this.listLunchedProcess = function (currentPage, searchInput, itemsPerPage, listUrl) {
                if (listUrl == undefined) {
                    listUrl = '';
                }
                return $http.get('/api/v1/LunchedProcess/' + listUrl + '/?page=' + currentPage + '&query=' + searchInput + '&itemPerPage=' + itemsPerPage);
            };
            this.createLunchedProcess = function (obj) {
                return $http.post('api/v1/LunchedProcess/', obj);
            };
            this.updateLunchedProcess = function (id, obj) {
                return $http.put('api/v1/LunchedProcess/' + id + '/', obj);
            };
            this.completeJob = function (id, obj) {
                return $http.patch('api/v1/LunchedProcess/' + id + '/CompleteJob/', obj);
            };
            this.deleteLunchedProcess = function (id) {
                return $http.delete('/api/v1/LunchedProcess/' + id + '/');
            };

        }]);






