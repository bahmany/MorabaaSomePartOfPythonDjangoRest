'use strict';
var currentChartUrl = "";
angular
    .module('AniTheme')
    .service('companiesManagmentService',
    ['$cookies', '$http', '$location',
        function ($cookies, $http, $location) {
            this.GetCompaniesList = function (addressWithParam) {
                if (addressWithParam == undefined) {
                    addressWithParam = "/api/v1/companies/"
                }
                return $http.get(addressWithParam);
            };
            this.companiesForCurrent = function (addressWithParam) {
                if (addressWithParam == undefined) {
                    addressWithParam = "/api/v1/companies/1/positions/CompaniesForCurrent/"
                }
                return $http.get(addressWithParam);
            };

            this.setAsCurrentService = function (userId,companyId) {
                return $http.patch("/api/v1/users/" + userId + "/", {
                    current_company: companyId
                })
            };

            this.GetChart = function (companyId) {
                currentChartUrl = "/api/v1/companies/" + companyId + "/chart/";
                loadChart("/api/v1/companies/" + companyId + "/chart/jsonRecursiveChart/")
            };

            this.GetSecByChartPos = function (companyId, chartID) {
                return $http.get("/api/v1/companies/" + companyId + "/chart/" + chartID + "/getSecWithChartPerm/")
            };

            this.SelectDeselectChart = function (companyID, chartID, receiver, selected) {
                return $http.post("/api/v1/companies/" + companyID + "/invite/", {
                    company: companyID,
                    chart: chartID,
                    receiver: receiver,
                    selected: selected,
                    seen: false
                })
            };

            this.UpdateSecPer = function (SelectedCompanyID, chartID, item) {
                return $http.post("/api/v1/companies/" + SelectedCompanyID + "/chart/" + chartID + "/updateSecPerm/", item)
            }

            this.RemoveInvitation = function (SelectedUserID, invitaionID) {
                return $http.get("/api/v1/profile/" + SelectedUserID + "/RemoveInvitations/?q=" + invitaionID)
            };

            this.GetUserInvitations = function (SelectedUserID, searchStr) {
                return $http.get("/api/v1/profile/" + SelectedUserID + "/GetUserInvitations/")
            };

            this.PostZone = function (companyId, zone) {
                return $http.post("/api/v1/companies/" + companyId + "/chart-zone/", zone)
            };
            this.EditZone = function (companyId, zone) {
                return $http.put("/api/v1/companies/" + companyId + "/chart-zone/" + zone.id + "/", zone)
            };

            this.GetZones = function (companyId, chartID) {
                if (chartID == "") {
                    return $http.get("/api/v1/companies/" + companyId + "/chart-zone/0/GetListWithSelected/")
                }
                return $http.get("/api/v1/companies/" + companyId + "/chart-zone/" + chartID + "/GetListWithSelected/")
            };

            this.GetCompanyChartList = function (companyID) {
                return $http.get("/api/v1/companies/" + companyID + "/chart/")
            };





            this.GetCompanyMembers = function (companyID) {
                return $http.get("/api/v1/profile/SearchProfiles/?page=1")
            };

            this.GetMemberInvitations = function (personID) {
                return $http.get("/api/v1/profile/GetMyInvitations/")
            };


            this.FindBy = function (url, id) {
                return $http.get(url + id + "/")
            };

            this.ChangeZone = function (selectedChartID, zone) {
                return $http.post(
                    "/api/v1/companies/" + zone.company +
                    "/chart-zone/" + selectedChartID + "/ToggleZone/",
                    zone);
            };

            this.DeleteZone = function (SelectedCompanyID, selectedChartID, ZoneID) {
                return $http.delete("/api/v1/companies/" + SelectedCompanyID + "/chart-zone/" + ZoneID + "/")
            };

            this.findPagedAll = function (url, currentPage, maxSize, itemPerPage, query) {
                return $http.get(
                    url +
                    '?page=' + currentPage +
                    '&query=' + query +
                    '&itemPerPage=' + itemPerPage)
            };

            this.doInsert = function (companyName) {

                return $http.post("api/v1/companies/", {
                    name: companyName
                })
            };
            this.doUpdate = function (url, newObj) {
                return $http.put(url, newObj)
            };

            this.doDelete = function (url) {
                return $http.delete(url)
            };


            this.GetCompanyProfile = function (companyID) {
                return $http.get(
                    "api/v1/companies/" + companyID + "/profile/"
                )
            };

            this.UpdateProfile = function (profile) {
                return $http.put("api/v1/companies/" + profile.companyID + "/profile/" + profile.id + "/", profile)
            };

            this.SaveProductionService = function (companyID, production) {
                if (production.id) {
                    return $http.put(
                        "api/v1/companies/" + companyID + "/products/" + production.id + "/",
                        production
                    )
                } else {
                    return $http.post(
                        "api/v1/companies/" + companyID + "/products/",
                        production
                    )
                }
            };

            this.GetProductions = function (companyID) {
                return $http.get("api/v1/companies/" + companyID + "/products/")
            };

            this.EditProduct = function (companyID, productionID) {
                return $http.get("api/v1/companies/" + companyID + "/products/" + productionID + "/")
            };
            this.DeleteProduction = function (companyID, productionID) {
                return $http.delete("api/v1/companies/" + companyID + "/products/" + productionID + "/")
            }


        }]);




