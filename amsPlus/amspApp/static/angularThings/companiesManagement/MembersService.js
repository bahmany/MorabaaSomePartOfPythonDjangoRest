(function () {
    'use strict';
    angular
        .module('AniTheme')
        .service('CompanyMembersService',
        ['$cookies', '$http', '$location',
            function ($cookies, $http, $location) {


                this.ForceOutSrv = function (companyID, items) {
                    return $http.post("/api/v1/companies/" + companyID + "/chart/0/ForceOut/", items);
                };
                this.RemoveFromInbox = function (companyID, items) {
                    return $http.post("/api/v1/companies/" + companyID + "/chart/0/RemoveFromInbox/", items);
                };

                // if returnWithDetails is true response will have current positionID and current position mongoID
                // if returnWithDetails = true then return currentCompany, currentPositionID, currentPositionIDMongo
                // if returnWithDetails = false then return only current Company
                // returnWithDetails is boolean

                this.getCurrent = function (returnWithDetails) {
                    return $http.get("/getCurrent?position=" + returnWithDetails)
                };


                this.searchMembers = function (companyID, items) {
                    return $http.get("/search/company/members?cid=" + companyID + "&q=" + items)
                };

//$scope.ChartCompanyID, $scope.SearchChartList, PageID
                //------------------------------------------------------------------------
                // this is for chart area ................................................
                this.GetCompanyChartList = function (companyID, SearchChartList, PageID) {
                    var qstr = "q=" + SearchChartList + "&page=" + PageID;
                    return $http.get("/api/v1/companies/" + companyID + "/chart/?" + qstr);
                };
                this.GetCompanyChartListByPager = function (SearchChartList, PagerUrl) {
                    var qurl = PagerUrl + "&q=" + SearchChartList;

                    if (qurl.split("?").length == 1) {
                        qurl = qurl.replace("&", "?");
                    }
                    return $http.get(qurl);
                };
                this.UpdatePosition = function (CompanyID, PersonID, NewPositionID, oldPositionID, oldPositionObjID) {
                    var qst = {
                        CompanyID: CompanyID,
                        UserID: PersonID,
                        NewPositionID: NewPositionID,
                        OldPositionID: oldPositionID,
                        OldPositionObjID: oldPositionObjID
                    };
                    return $http.post("/api/v1/companies/" + CompanyID + "/chart/0/UpdatePost/", qst);
                };
                //------------------------------------------------------------------------


            }]);
})();



