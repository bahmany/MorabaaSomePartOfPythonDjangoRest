'use strict';

angular
    .module('AniTheme')
    .service('InboxFolderService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {


            this.listFolder = function () {
                return $http.get("/api/v1/inboxFolders/");
            }
            this.createFolder = function (folder) {
                if (folder.hasOwnProperty("id")) {
                    return $http.patch("/api/v1/inboxFolders/" + folder.id + "/", folder)
                } else {
                    return $http.post("/api/v1/inboxFolders/", folder)
                }
            };
        }]);