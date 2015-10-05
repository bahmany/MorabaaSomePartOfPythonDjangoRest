/**
 * Created by mohammad on 10/4/15.
 */
function setUpSideBar($scope, $http, $modal) {


//------------------------------- services
    var listLabel = function () {
        return $http.get("/api/v1/inboxLabels/")
    }
    var deleteLabel = function (id) {
        return $http.delete("/api/v1/inboxLabels/" + id + "/")

    }
    var listFolderTreeView = function () {
        return $http.get("/api/v1/inboxFolders/listFolderTreeView/")

    }
    var createFolder = function (folder) {
        if (folder.hasOwnProperty("id")) {
            return $http.patch("/api/v1/inboxFolders/" + folder.id + "/", folder)
        } else {
            return $http.post("/api/v1/inboxFolders/", folder)
        }
    }
    var listGroup = function () {
        return $http.get("/api/v1/inboxGroups/GetListForBar/")
    }
    var deleteFolder = function (id) {
        return $http.delete("/api/v1/inboxFolders/" + id + "/")

    }
    var deleteGroup = function (id) {
        return $http.delete("/api/v1/inboxGroups/" + id + "/")
    }
//----------------------------------- end service


    $scope.treedata = [];
    $scope.labels = {};
    $scope.listFolder = [];
//---------------------------------------
//----------------------------------------------------------------
//----------------------------------------------------------------
//--------- Labels ---------
    $scope.newLabel = {};
    $scope.listLabel = function () {
        listLabel().success(function (data) {
            $scope.labels = data;
        }).error(function (data) {

        });
    };
    $scope.createLabel = function () {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: 'labelCreateModal',
            controller: 'ModalLabelCreateInstanceCtrl',
            size: '',
            resolve: {
                oldLabel: function () {
                    return false;
                }
            },

            deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                //console.log("perparing to get scripts");
                return $ocLazyLoad.load({
                    name: 'AniTheme.LabelModal',
                    files: [
                        '/static/angularThings/Letter/Sidebar/Labels/InboxLabelService.js',
                        '/static/angularThings/Letter/Sidebar/Labels/InboxLabelController.js',
                    ],
                    catch: true
                }).then(
                    function () {
                    }
                )
            }]
        });


        modalInstance.result.then(function (res) {
            swal('You add:', res.title, "success");
            $scope.listLabel();
        }, function () {

        });

    };
    $scope.editLabel = function (label) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: 'labelCreateModal',
            controller: 'ModalLabelCreateInstanceCtrl',
            size: '',
            resolve: {
                oldLabel: function () {
                    return label;
                },

                deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                    //console.log("perparing to get scripts");
                    return $ocLazyLoad.load({
                        name: 'AniTheme.ForgetPass',
                        files: [
                            '/static/angularThings/Letter/Sidebar/Labels/InboxLabelService.js',
                            '/static/angularThings/Letter/Sidebar/Labels/InboxLabelController.js',
                        ],
                        catch: true
                    }).then(
                        function () {
                        }
                    )
                }]
            }
        });

        modalInstance.result.then(function (res) {
            swal('You edit:', res.title, "success");
            $scope.listLabel();
        }, function () {

        });

    };
    $scope.deleteLabel = function (obj) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            showLoaderOnConfirm: true,
            closeOnConfirm: false
        }, function () {

            deleteLabel(obj.id).success(function (data) {
                swal("Deleted!", "Your imaginary file has been deleted", "success");
                $scope.listLabel();

            });
        });
    };
    $scope.newObj = {};
//----------------------------------------------------------------
//----------------------------------------------------------------
//--------- Folders ---------
    $scope.listFolder = [];
    $scope.listFolderTreeView = function () {
        listFolderTreeView().success(function (data) {
            $scope.treedata = data;
        }).error(function (data) {

        });

    };
    $scope.openFolderModal = function (folder) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: 'FolderModal',
            controller: 'FolderEditModalInstanceCtrl',
            size: '',

            resolve: {
                oldFolder: function () {
                    return folder;
                },

                deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                    //console.log("perparing to get scripts");
                    return $ocLazyLoad.load({
                        name: 'AniTheme.ForgetPass',
                        files: [
                            '/static/angularThings/Letter/Sidebar/Folders/InboxFolderService.js',
                            '/static/angularThings/Letter/Sidebar/Folders/InboxFolderController.js',
                        ],
                        catch: true
                    }).then(
                        function () {
                        }
                    )
                }]
            }
        });
        modalInstance.result.then(function (res) {
            $scope.listFolderTreeView();
        }, function () {
        });
    };
    $scope.editFolderModal = function (folder) {
        $scope.openFolderModal(folder);
    };
    $scope.newFolder = function (parentObj) {
        if (parentObj) {
            var newObj = {"title": $scope.newObj.title, "parentID": parentObj.id, positionID: 1, "children": []};
        } else {
            var newObj = {"title": "", positionID: 1, "children": []};
        }
        swal({
            title: "An input!",
            text: "Write something interesting:",
            type: "input",
            inputValue: $scope.newObj.title,
            showCancelButton: true,
            closeOnConfirm: false,
            animation: "slide-from-top",
            inputPlaceholder: "Write something"
        }, function (inputValue) {
            if (inputValue === false) return false;
            if (inputValue === "") {
                swal.showInputError("You need to write something!");
                return false
            }
            newObj.title = inputValue;
            createFolder(newObj).success(function (data) {
                swal("Nice!", "You added: " + data.title, "success");
                $scope.listFolderTreeView();
            }).error(function (data) {
                swal('title', data.title, "error");
            });
        });
    };
    $scope.deleteFolder = function (obj) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            showLoaderOnConfirm: true,
            closeOnConfirm: false
        }, function () {
            if (obj.children.length != 0) {

                swal("Error", "you should delete children first", "error");
                return false
            }
            deleteFolder(obj.id).success(function (data) {
                swal("Deleted!", "Your imaginary file has been deleted", "success");
                $scope.listFolderTreeView();

            });
        });
    };
//################################################################
//################################################################
//----------------------------------------------------------------
//----------------------------------------------------------------
//---------------Groups---------------------------------------
    $scope.group = {};
    $scope.groups = [];
    $scope.listGroup = function () {
        listGroup().success(function (data) {
            $scope.groups = data;
        }).error(function (data) {

        });
    };
    $scope.createGroup = function () {
        swal({
            title: "An input!",
            text: "Write something interesting:",
            type: "input",
            inputValue: $scope.group.title,
            showCancelButton: true,
            closeOnConfirm: false,
            animation: "slide-from-top",
            inputPlaceholder: "Write something"
        }, function (inputValue) {
            if (inputValue === false) return false;
            if (inputValue === "") {
                swal.showInputError("You need to write something!");
                return false
            }
            $scope.group.title = inputValue;
            $scope.group.positionID = 2;
            LetterInboxService.createGroup($scope.group).success(function (data) {
                swal("Nice!", "You added: " + data.title, "success");
                $scope.listGroup();
            }).error(function (data) {
                swal('title', data.title, "error");
            });
        });
    };
    $scope.editGroup = function (group) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: 'GroupEditModal',
            controller: 'GroupEditModalInstanceCtrl',
            size: '',
            resolve: {
                oldGroup: function () {
                    return group;
                },

                deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                    //console.log("perparing to get scripts");
                    return $ocLazyLoad.load({
                        name: 'AniTheme.ForgetPass',
                        files: [
                            '/static/angularThings/Letter/Sidebar/Groups/InboxGroupService.js',
                            '/static/angularThings/Letter/Sidebar/Groups/InboxGroupController.js',
                            '/static/angularThings/Letter/Sidebar/Groups/classChart.js',
                            '/static/angularThings/Letter/Sidebar/Groups/classGroup.js',
                            '/static/angularThings/Letter/Sidebar/Groups/classMember.js',
                            '/static/angularThings/Letter/Sidebar/Groups/classZone.js'
                        ],
                        catch: true
                    }).then(
                        function () {
                        }
                    )
                }]
            }
        });

        modalInstance.result.then(function (res) {
            swal('You edit:', res.title, "success");
            $scope.listGroup();
        }, function () {

        });

    };
    $scope.deleteGroup = function (obj) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            showLoaderOnConfirm: true,
            closeOnConfirm: false
        }, function () {

            deleteGroup(obj.id).success(function (data) {
                swal("Deleted!", "Your imaginary file has been deleted", "success");
                $scope.listGroup();

            });
        });
    };
//################################################################
//################################################################
    $scope.listGroup();
    $scope.listLabel();
    $scope.listFolderTreeView();
    $scope.$on('ngRepeatFinished', function (ngRepeatFinishedEvent) {
        $(".inbox-dynamic-items").hover(function () {
            $(this).find(".btnss").fadeIn(70);
        }, function () {
            $(this).find(".btnss").fadeOut(20);
        });
    });


}