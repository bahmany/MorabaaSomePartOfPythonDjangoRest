'use strict';


angular.module('AniTheme').controller(
    'companiesManagmentCtrl',
    function ($scope,
              $translate,
              $rootScope,
              $modal,
              companiesManagmentService) {

        $scope.Companies = [];
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
            height: 100

        };
        $scope.PageTo = function (PagerAddress) {
            companiesManagmentService.GetCompaniesList(PagerAddress).success(
                function (data) {
                    $scope.Companies = data;
                }
            )
        };
        $scope.SelectedCompanyID = -1;
        $scope.Profile = [];
        $scope.Productions = [];
        $scope.GetCompaniesList = function () {
            companiesManagmentService.GetCompaniesList().success(
                function (data) {
                    $scope.Companies = data;
                }
            )
        };
        $scope.CreateNewCompany = function () {

            swal(
                {
                    title: "New Company",
                    text: "Enter your new company name",
                    type: "input",
                    showCancelButton: true,
                    closeOnConfirm: false,
                    animation: "slide-from-top",
                    inputPlaceholder: "Write something"
                },
                function (inputValue) {

                    if (inputValue === false)
                        return false;
                    if (inputValue === "") {
                        swal.showInputError("You need to write something!");
                        return false
                    }
                    companiesManagmentService.doInsert(inputValue).success(
                        function (data) {
                            $scope.GetCompaniesList();
                            swal(
                                "Nice!",
                                "You wrote: " + data.name,
                                "success");
                        }
                    ).error(
                        function (err) {
                            swal.showInputError(err.name[0]);
                        }
                    )

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
        $scope.GetCompaniesList();
    });


