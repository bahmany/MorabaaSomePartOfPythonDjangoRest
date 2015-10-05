'use strict';


function groupInbox($scope, $http) {

//------------------------------ service
    var listGroupsWithMembers = function (companyId, query) {
        return $http.get("/search/groups/members?cid=" + companyId + "&q=" + query)
    };
    var GroupsPageTo = function (SearchChartList, PagerUrl) {
        var qurl = PagerUrl + "&q=" + SearchChartList;

        if (qurl.split("?").length == 1) {
            qurl = qurl.replace("&", "?");
        }
        return $http.get(qurl);
    };
//------------------------------

    $scope.groups = [];
    $scope.GroupSearchText = "";
    $scope.getGroupsList = function () {
        $scope.isSearchCallbackCompleted = false;
        listGroupsWithMembers("0", $scope.GroupsSearchText).success(function (data) {
            $scope.groups = data;
            $scope.isSearchCallbackCompleted = true;
        }).error(function (data) {
            $scope.isSearchCallbackCompleted = true;
        })
    };
    $scope.getGroupsList();
    $scope.$watch("GroupsSearchText", function () {
        $scope.getGroupsList();
    });
    $scope.addGroupToSelected = function (group) {
        for (var i = 0; group.members.length > i; i++) {
            $scope.addToSelected(group.members[i])
        }

    };
    $scope.GroupsPageTo = function (PageUrl) {
        $scope.isSearchCallbackCompleted = false;
        GroupsPageTo($scope.ProfileSearch, PageUrl).success(function (data) {
            $scope.isSearchCallbackCompleted = true;
            $scope.SearchPersons = data;
        }).error(function (data) {
            $scope.isSearchCallbackCompleted = true;
        });
    };
}