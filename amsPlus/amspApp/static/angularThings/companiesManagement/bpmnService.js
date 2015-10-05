'use strict';

angular
    .module('AniTheme')
    .service('bpmnService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {

                this.getCurrent = function (returnWithDetails) {
                    return $http.get("/getCurrent?position=" + returnWithDetails)
                };

            this.listUsers = function (companyId,chartId) {
                return $http.get("/api/v1/companies/"+companyId+"/chart/"+chartId+"/PositionsList/");
            };
            this.listCharts = function (companyId) {
                return $http.get("/api/v1/companies/"+companyId+"/chart/");
            };
            this.retrieveBpmn = function (companyId,id) {
                return $http.get("/api/v1/companies/"+ companyId +"/process/" + id + "/");
            };
            this.listBpmns = function (companyId,currentPage, searchInput, itemsPerPage) {
                return $http.get('/api/v1/companies/'+companyId+'/process/?page=' + currentPage + '&query=' + searchInput + '&itemPerPage=' + itemsPerPage);
            };
            this.bpmnCreate = function (companyId,obj) {
                return $http.post('api/v1/companies/'+companyId+'/process/', obj);
            };
            this.bpmnUpdate = function (companyId,id, obj) {
                return $http.put('api/v1/companies/'+companyId+'/process/' + id + '/', obj);
            };
            this.bpmnDelete = function (companyId,id) {
                return $http.delete('api/v1/companies/'+companyId+'/process/' + id + '/');
            };

        }]);






