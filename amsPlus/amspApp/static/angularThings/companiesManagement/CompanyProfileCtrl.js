'use strict';


angular.module('AniTheme')
    .directive("loadMoreData", [function () {
        return {
            restrict: 'ACE',
            link: function ($scope, element, attrs, ctrl) {
                var raw = element[0];
                element.scroll(function () {
                    console.log("hiiii");
                    if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
                        $scope.$apply("loadMoreData()");
                    }
                });
            }
        };

    }]);


angular.module('AniTheme')
    .controller('CompanyProfileCtrl', function ($scope, $http, $q, $translate, $rootScope, $stateParams, $location, $modal, companiesManagmentService) {
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
            resize_maxHeight: 300,
            height: 185

        };


        $scope.GetCompanyProfile = function (item) {


            companiesManagmentService.GetCompanyProfile(item).success(function (data) {
                $scope.Profile = data[0];
            });
        };

        $scope.GetCompanyProfile($stateParams.companyid);
        $scope.UpdateProfile = function () {

            var defer = $q.defer();

            var res = companiesManagmentService.UpdateProfile($scope.Profile);

            res.success(function (data) {
                $scope.GetCompanyProfile($stateParams.companyid);
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
