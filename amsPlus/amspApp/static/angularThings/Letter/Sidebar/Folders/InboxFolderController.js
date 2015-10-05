angular.module('AniTheme').controller('FolderEditModalInstanceCtrl', function (
    $scope,
    $modalInstance,
    $http, $translate,
    LetterInboxService,
    oldFolder,
    InboxFolderService
) {
    $scope.folder = {};
    $scope.listFolder = [];
    $scope.folder = oldFolder;


    $scope.ListFolders = function () {
        InboxFolderService.listFolder().success(function (data) {
            $scope.listFolder = data;
        }).error(function (data) {

        });
    };
    $scope.ListFolders();

    $scope.saveFolder = function () {
        InboxFolderService.createFolder($scope.folder).success(function (data) {
            $modalInstance.close(data);
        });
    }
    $scope.cancelFolder = function () {
        $modalInstance.dismiss('cancel');
    };
});
