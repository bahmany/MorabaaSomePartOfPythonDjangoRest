'use strict';


angular.module('AniTheme').controller('GroupEditModalInstanceCtrl', function ($scope,
                                                                              $modalInstance,
                                                                              $http,
                                                                              $translate,
                                                                              LetterInboxService,
                                                                              oldGroup,
                                                                              InboxGroupService) {
    $scope.group = oldGroup;
    $scope.finalList = [];
//------------------------------------------------------
//------------------------------------------------------
//------------------------------------------------------
    memberInbox($scope, $http);
//------------------------------------------------------
//------------------------------------------------------
//------------------------------------------------------
    chartInbox($scope, $http);
//--------------------------------------------------
//--------------------------------------------------
//--------------------------------------------------
    zoneInbox($scope, $http);
//-------------------------------------------------
//-------------------------------------------------
//-------------------------------------------------
    groupInbox($scope, $http);
//-------------------------------------------------
//-------------------------------------------------
//-------------------------------------------------

    $scope.saveGroup = function () {
        var finalSent = {
            group: $scope.group,
            members: $scope.selects
        };
        InboxGroupService.editGroup(
            finalSent).success(function (data) {
                $modalInstance.close(data);
            }).error(function (data) {
                swal('Error', data.title, "error");
            });
    };
    $scope.listMember = function () {
        InboxGroupService.listGroupMembers($scope.group.id, $scope.MembersSearchText).success(function (data) {
            $scope.selects = data.members;
        }).error(function (data) {

        });
        //$scope.member = $scope.group.members
    };
    $scope.listMember();
    $scope.cancelGroup = function () {
        $modalInstance.dismiss('cancel');
    };

});