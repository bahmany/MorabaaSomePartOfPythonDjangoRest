'use strict';

angular
    .module('AniTheme')
    .service('InboxGroupService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {
            this.createGroup = function (group) {
                return $http.post("/api/v1/inboxGroups/", group)
            };
            this.editGroup = function (group) {
                return $http.put("/api/v1/inboxGroups/UpdateGroup/", group)
            };
            this.listGroupMembers = function (group, search) {
                return $http.get("/api/v1/inboxGroups/" + group + "/GetGroupMember/?q=" + search)
            };
        }]);
