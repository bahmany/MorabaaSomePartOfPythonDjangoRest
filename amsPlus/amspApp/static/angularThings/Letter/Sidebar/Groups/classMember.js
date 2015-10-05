'use strict';


function memberInbox($scope, $http) {


//-------------------------------- services
    var listMember = function (companyId, query) {
        return $http.get("/search/company/members?cid=" + companyId + "&q=" + query)
    };
    var MembersPageTo = function (SearchChartList, PagerUrl) {
        var qurl = PagerUrl + "&q=" + SearchChartList;

        if (qurl.split("?").length == 1) {
            qurl = qurl.replace("&", "?");
        }
        return $http.get(qurl);
    };
//--------------------------------


    $scope.members = [];
    $scope.MembersSearchText = "";
    $scope.isSearchCallbackCompleted = true;
    $scope.getMembersList = function () {
        $scope.isSearchCallbackCompleted = false;
        listMember('drede23fa', $scope.MembersSearchText).success(function (data) {
            $scope.members = data;
            $scope.isSearchCallbackCompleted = true;
        }).error(function (data) {
            $scope.isSearchCallbackCompleted = true;
        })
    };
    $scope.getMembersList();
    $scope.$watch("MembersSearchText", function () {
        $scope.getMembersList();
    });
    $scope.selects = [];
    $scope.addToSelected = function (member) {
        var hasBefore = false;
        for (var i = 0; $scope.selects.length > i; i++) {
            if ($scope.selects[i].id == member.id) {
                hasBefore = true;
            }
        }
        if (!hasBefore) {
            $scope.selects.push(member);
        }
    };
    $scope.removeSelected = function (member, index) {
        $scope.selects.splice(index, 1);
    };
    $scope.OpenSearch = function (name) {
        $(".searchmem").hide();
        $("#" + name).show();
    };
    $scope.OpenSearch("companymemberselectdiv");
    $scope.MemberPageTo = function (PageUrl) {
        $scope.isSearchCallbackCompleted = false;
        MembersPageTo($scope.ProfileSearch, PageUrl).success(function (data) {
            $scope.isSearchCallbackCompleted = true;
            $scope.SearchPersons = data;
        }).error(function (data) {
            $scope.isSearchCallbackCompleted = true;
        });
    };
}