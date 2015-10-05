'use strict';

angular
    .module('AniTheme')
    .service('InboxLabelService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {

            this.createLabel = function (label) {
                return $http.post("/api/v1/inboxLabels/", label)
            };

            this.editLabel = function (id, label) {
                return $http.put("/api/v1/inboxLabels/" + id + "/", label)
            };




        }]);