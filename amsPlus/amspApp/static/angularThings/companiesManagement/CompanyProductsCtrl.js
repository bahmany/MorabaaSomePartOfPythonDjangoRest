'use strict';
angular.module('AniTheme')
    .controller('CompanyProductsCtrl', function ($scope, $http, $translate, $rootScope,$stateParams, $location, $modal, companiesManagmentService) {
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
        $scope.GetProductionsList = function (companyID) {
            companiesManagmentService.GetProductions(companyID).success(function (data) {
                $scope.Productions = data;
            });
        };
        $scope.GetProductionsList($stateParams.companyid);

        $scope.NewProduction = {};
        $scope.ResetNewProduction = function () {
            $scope.NewProduction = {};
            $scope.NewProduction.extra = {};
            $scope.NewProduction.extra.DefaultProductionImage = "/static/images/default_pic_production.png";

        };
        $scope.AddNewProduction = function () {
            $scope.ResetNewProduction();

            $("#pnlProductionList").fadeOut(100, function () {
                $("#divAddNewProduction").fadeIn(100);

            });
        };
        $scope.CancelProduction = function () {
            $scope.ResetNewProduction();
            $("#divAddNewProduction").fadeOut(100, function () {
                $("#pnlProductionList").fadeIn(100);

            });

        };
         $scope.DeleteThisCompamy = function (product, index) {
            swal({
                title: "Are you sure?",
                text: "By deleting this product every thing about this will be gone for ever",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Yes, delete it!",
                closeOnConfirm: false
            }, function () {
                companiesManagmentService.DeleteProduction($stateParams.companyid, product.id).success(function () {
                    $scope.Productions.results.splice(index, 1);
                    $scope.GetProductionsList($stateParams.companyid);
                    swal("Deleted!", "the product deleted.", "success");
                });

            });
        };
        $scope.EditThisProduct = function (product) {
            $scope.ResetNewProduction();

            $scope.$on("ckeditor.ready", function (event) {
                $scope.isReady = true;
            });

            $scope.NewProduction = product;
            $("#pnlProductionList").fadeOut(100, function () {
                $("#divAddNewProduction").fadeIn(100);
                //$scope.$apply();

            });

            //companiesManagmentService.EditProduct($scope.MyProfile.companyID, product.id).success(function (data) {
            //
            //});
        };
        $scope.SaveProduction = function () {
            //$scope.NewProduction.companyProfile = $scope.MyProfile.id;
            if (!$scope.NewProduction.name) {
                sweetAlert("Ooops..", "Production Name is require, does not left it blank", "error");
                return;
            }
            companiesManagmentService.SaveProductionService(
                $stateParams.companyid,
                $scope.NewProduction).success(function (data) {
                    $scope.GetProductionsList($stateParams.companyid);
                    $("#divAddNewProduction").fadeOut(100, function () {
                        $("#pnlProductionList").fadeIn(100);

                    });
                });

        };

    });
