'use strict';


angular.module('AniTheme').controller(
    'profileCtrl',
    function ($scope,
              $translate,
              $q,
              $rootScope,
              $modal,
              ProfileService) {

        $scope.Profile = {};
        $scope.editorOptions = {
            language: 'en',
            toolbar: [
                {
                    name: 'document',
                    items: [
                        'Source',
                        '-',
                        'NewPage',
                        'Preview',
                        '-',
                        'Templates',
                        'Image',
                        'Table',
                        'Bold',
                        'Italic'
                    ]
                },
                ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']
            ],
            extraPlugins: 'lineutils,notification,uploadwidget,uploadimage',
            removePlugins: 'sourcearea',
            filebrowserUploadUrl: '/api/v1/file/upload',
            resize_maxHeight: 250,
            height: 200

        };


        //it is for timeline pagination
        $scope.loadMore = function (element) {
            if ($scope.Posts.next == null) {
                $(element.target).addClass('disabled');
            } else {
                ProfileService.listPostsByUrl($scope.Posts.next).success(function (data) {
                    for (var i = 0; data.results.length > i; i++) {
                        $scope.Posts.results.push(data.results[i]);
                    }

                    $scope.Posts.next = data.next;

                });
            }
        };

        $scope.GetProfile = function () {
            ProfileService.retrieveProfile().success(function (data) {
                $scope.Profile = data;
            })
        };
        $scope.GetProfile();


        $scope.Post = {};

        $scope.Posts = [];
        $scope.ListPosts = function () {
            ProfileService.listPosts().success(function (data) {
                $scope.Posts = data;
                $("#imgPostAvatar").attr("src", $scope.Profile.extra.profileAvatar.url);
                $(".fit-height").mCustomScrollbar({
                    theme: "minimal-dark",
                    alwaysShowScrollbar: 1
                });
                //(function ($) {
                //    $(window).load(function () {
                //
                //    });
                //})(jQuery);
            })
        };
        $scope.ListPosts();

        $scope.CreatePost = function () {
            var defer = $q.defer();

            var res =ProfileService.createPost($scope.Post);
                res.success(function (data) {
                $scope.ListPosts();
                return defer.resolve(res);

            }).error(function (data) {
                return defer.reject("");

            });
            return defer.promise;

        };

        $scope.UpdatePost = function (item) {
            ProfileService.updatePost(item.id, item).success(function (data) {
                item.isItEditing = false;

            })
        };

        $scope.ShowUpdatePanel = function (post) {
            post.isItEditing = true;
        }
        $scope.CancelUpdatePost = function (post) {
            post.isItEditing = false;
        }

        $scope.DeletePost = function (item, $index) {
            swal({
                title: "Are you sure?",
                text: "After deleting the phone number, You can not recover that",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, delete it!",
                closeOnConfirm: false
            }, function () {

                ProfileService.deletePost(item.id).success(
                    function (data) {
                        $scope.ListPosts();
                        swal("Deleted!", "Your post successfully deleted", "success");
                        item.splice(index, 1);
                        $scope.$apply();
                    });
            });
        };

        $scope.AddPhone = function (profile) {
            $scope.Profile.extra.Phones.push({
                tel: "enter your number here ...",
                security: 1,
                phoneORemail: 1
            })
        };
        $scope.RemovePhone = function (item, index) {
            swal({
                title: "Are you sure?",
                text: "After deleting the phone number, You can not recover that",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, delete it!",
                closeOnConfirm: false
            }, function () {
                item.splice(index, 1);
                $scope.$apply()
                swal("Deleted!", "Your phone successfully deleted, press save button to commit your changes", "success");
            });
        }
        $scope.ChangeAccessPhone = function (item) {
            item.security += 1;
            if (item.security == 5) {
                item.security = 1;
            }
        };
        $scope.ChangeAccessPhoneType = function (item) {
            item.phoneORemail += 1;
            if (item.phoneORemail == 3) {
                item.phoneORemail = 1;
            }
        };


        $scope.UpdateProfile = function () {
            var defer = $q.defer();
            var res = ProfileService.updateProfile($scope.Profile);
            res.success(function (data) {
                return defer.resolve(res);
            }).error(function (data) {
                data.message.forEach(function (err) {
                    swal(err.name, err.message, "error");
                });
                return defer.reject("");
            });

            return defer.promise;
        };


    });

