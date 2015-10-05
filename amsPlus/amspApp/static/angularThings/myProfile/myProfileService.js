'use strict';

angular
    .module('AniTheme')
    .service('ProfileService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {





            this.ChangeProfileTopHeaderBackground = function (newImageID) {
                return $http.post("/api/v1/profile/change-header-background/",
                    {
                        imageID: newImageID
                    });
            };




            this.updateProfile = function (updatedProfile) {
                return $http.put("/api/v1/profile/1/",
                    updatedProfile);
            };

            this.retrieveProfile = function () {
                return $http.get("/api/v1/profile/1/");
            };







            this.createPost = function (post) {
                return $http.post("/api/v1/posts/", post)
            };


            this.deletePost = function (postID) {
                return $http.delete("/api/v1/posts/"+postID+"/")
            };

            this.updatePost = function (postID, item) {
                return $http.put("/api/v1/posts/"+postID+"/", item)
            };

            this.listPosts = function () {
                return $http.get("api/v1/posts/")
            };
            this.listPostsByUrl = function (url) {
                return $http.get(url)
            };






        }]);






