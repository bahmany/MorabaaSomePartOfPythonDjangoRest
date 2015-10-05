'use strict';

/**
 * @ngdoc overview
 * @name AniTheme
 * @description
 * # AniTheme
 *
 * Main module of the application.
 */
window.app_version = 1.11;

angular
    .module(
    'AniTheme', [

        'ui.router',
        'ngAnimate',
        'angularTreeview',
        //'infinite-scroll',
        //'ui.calendar',
        //'chart.js',
        'textAngular',
        //'gridshore.c3js.chart',
        //'angular-growl',
        //'growlNotifications',
        'angular-loading-bar',
        'angular-progress-button-styles',
        'pascalprecht.translate',
        'ui.bootstrap',
        'ngCookies',
        'ng',
        'ui.tree',
        'ngFileUpload',
        'picker',
        'oc.lazyLoad',
        'ngCkeditor',
        'fg'

    ])
    .config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
        cfpLoadingBarProvider.latencyThreshold = 5;
        cfpLoadingBarProvider.includeSpinner = false;
    }])
    .config(function ($interpolateProvider, $httpProvider) {

        $interpolateProvider.startSymbol('//');
        $interpolateProvider.endSymbol('//');

//        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
//        $httpProvider.defaults.headers.post['X-CSRFToken'] = $.cookie('csrftoken');
//        $httpProvider.defaults.headers.put['X-CSRFToken'] = $.cookie('csrftoken');
//        $httpProvider.defaults.headers.delete['X-CSRFToken'] = $.cookie('csrftoken');

// we can change above setting with buttom
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    })
    .config(function (progressButtonConfigProvider) {
        progressButtonConfigProvider.profile('login', {
            style: 'shrink',
            direction: 'vertical'
        });
    })

    .config(function ($translateProvider) {
        $translateProvider.useStaticFilesLoader({
            prefix: '/static/languages/',
            suffix: '.json'
        });
        $translateProvider.preferredLanguage('en');

    }).config(function ($provide) {

        $provide.decorator('taOptions', ['taRegisterTool', '$delegate', '$modal', function (taRegisterTool, taOptions, $modal) {
            taRegisterTool('uploadImage', {
                buttontext: 'Upload Image',
                iconclass: "fa fa-image",
                action: function (deferred, restoreSelection) {
                    $modal.open({
                        controller: 'UploadImageModalInstance',
                        templateUrl: 'page/generic/upload.html'
                    }).result.then(
                        function (result) {
                            restoreSelection();
                            document.execCommand('insertImage', true, result);
                            deferred.resolve();
                        },
                        function () {
                            deferred.resolve();
                        }
                    );
                    return false;
                }
            });
            taOptions.toolbar[1].push('uploadImage');
            return taOptions;
        }]);
    })
    .config(function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.when('/dashboard', '/dashboard/home');
        $urlRouterProvider.otherwise('/dashboard/home');

        $stateProvider
            .state('base', {
                abstract: true,
                url: '',
                templateUrl: '/page/base',
                controller: 'DashboardCtrl'
            })
            .state('login', {
                url: '/login',
                parent: 'base',
                controller: 'LoginCtrl',
                controllerAs: 'vm',
                templateUrl: '/page/login'
            })
            .state('signup', {
                url: '/signup',
                parent: 'base',
                controller: 'RegisterCtrl',
                controllerAs: 'vm',
                templateUrl: '/page/signup'

            })
            .state('forget', {
                url: '/forget',
                parent: 'base',
                controller: 'ForgetCtrl',
                controllerAs: 'vm',
                templateUrl: '/page/forget',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'AniTheme.ForgetPass',
                            files: [
                                '/static/angularThings/authentication/forgetCtrl.js',
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('resetpass', {
                url: '/ResetPassword/:q/',
                parent: 'base',
                controller: 'ForgetCtrl',
                controllerAs: 'vm',
                templateUrl: '/myapi/resetpass/',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'AniTheme.ForgetPass',
                            files: [
                                '/static/angularThings/authentication/forgetCtrl.js',
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('404-page', {
                url: '/page/404-page',
                parent: 'base',
                templateUrl: '/404-page'
            })
            .state('dashboard', {
                url: '/dashboard',
                parent: 'base',
                templateUrl: '/page/dashboard'

            })
            .state('home', {
                url: '/home',
                parent: 'dashboard',
                templateUrl: '/page/home',
                controller: 'HomeCtrl'
            })
            .state('newbpmn', {
                url: '/newbpmn',
                parent: 'dashboard',
                templateUrl: '/page/newbpmn'
            })
            //.state('buildForm', {
            //    url: '/buildForm',
            //    parent: 'dashboard',
            //    templateUrl: '/page/buildForm'
            //})
            .state('friends', {
                url: '/Friends',
                parent: 'dashboard',
                templateUrl: '/page/friends/',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'OCfriends',
                            files: [
                                '/static/angularThings/friends/friendsService.js',
                                '/static/angularThings/friends/friendsCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }
            })
            .state('companies', {
                url: '/Companies',
                parent: 'dashboard',
                templateUrl: '/page/companies/',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'OCcompanies',
                            files: [
                                '/static/angularThings/companiesManagement/companiesManagmentCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }
            })
            .state('company', {
                url: '/Company/:companyid',
                parent: 'dashboard',
                templateUrl: '/page/comopbase',
                controller: 'CompanyCtrl',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany',
                            files: [
                                '/static/angularThings/companiesManagement/CompanyCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.chart', {
                url: '/Chart',
                parent: 'company',
                templateUrl: '/page/company/chart',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.chart',
                            files: [
                                '/static/angularThings/companiesManagement/CompanyChartCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.members', {
                url: '/Members',
                parent: 'company',
                templateUrl: '/page/company/members',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.members',
                            files: [
                                '/static/angularThings/companiesManagement/MembersService.js',
                                '/static/angularThings/companiesManagement/MembersCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.secretariats', {
                url: '/Secretariats',
                parent: 'company',
                templateUrl: '/page/company/secretariats',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.secretariats',
                            files: [
                                '/static/angularThings/companiesManagement/SecretaraitsService.js',
                                '/static/angularThings/companiesManagement/SecretaraitsCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.profile', {
                url: '/Profile',
                parent: 'company',
                templateUrl: '/page/company/profile',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.profile',
                            files: [
                                '/static/angularThings/companiesManagement/CompanyProfileCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.products', {
                url: '/Products',
                parent: 'company',
                templateUrl: '/page/company/products',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.products',
                            files: [
                                '/static/angularThings/companiesManagement/CompanyProductsCtrl.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.process', {
                url: '/Process',
                parent: 'company',
                templateUrl: '/page/company/process',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.process',
                            files: [
                                '/static/angularThings/companiesManagement/CompanyProcessCtrl.js',
                                '/static/angularThings/companiesManagement/bpmnService.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.process.new', {
                url: '/Process/New',
                parent: 'company',
                templateUrl: '/page/company/newProcess',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.process.new',
                            files: [
                                '/static/angularThings/companiesManagement/bpmnModelerCtrl.js',
                                '/static/angularThings/companiesManagement/bpmnService.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.process.edit', {
                url: '/Process/:processId/Edit',
                parent: 'company',
                templateUrl: '/page/company/newProcess',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.process.edit',
                            files: [
                                '/static/angularThings/companiesManagement/bpmnModelerCtrl.js',
                                '/static/angularThings/companiesManagement/bpmnService.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('company.process.setup', {
                url: '/Process/:processId/setup',
                parent: 'company',
                templateUrl: '/page/company/setupProcess',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCcompany.process.setup',
                            files: [
                                '/static/angularThings/companiesManagement/bpmnSetupCtrl.js',
                                '/static/angularThings/companiesManagement/bpmnService.js'
                            ],
                            catch: true
                        }).then(
                            function () {
                            }
                        )
                    }]
                }

            })
            .state('chart', {
                url: '/chart',
                parent: 'companies-management',
                templateUrl: '/page/companies-managment/chart'
                //resolve:{
                //    d3loader:[
                //        "$ocLazyLoad", function ($ocLazyLoad) {
                //            return $ocLazyLoad.load({
                //                name:"AniTheme.D3",
                //                files:[
                //                    '/static/bower_components/d3/d3.min.js'
                //                ],
                //                catch:true
                //            }).then(
                //                function () {
                //
                //                }
                //            )
                //        }
                //    ]}
            })
            .state('myProfile', {
                url: '/MyProfile',
                parent: 'dashboard',
                templateUrl: '/page/myProfile',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        //console.log("perparing to get scripts");
                        return $ocLazyLoad.load({
                            name: 'OCmyProfile',
                            files: [
                                '/static/angularThings/myProfile/myProfileService.js',
                                '/static/angularThings/myProfile/myProfileCrtl.js'
                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {
                                //console.log("Loading Completed !");
                                //debugger;
                            }
                        )
                    }]
                }

            })
            .state('letter', {
                url: '/Letter',
                parent: 'dashboard',
                templateUrl: '/page/letterBase',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCletter',
                            files: [
                                '/static/angularThings/Letter/LetterInboxService.js',
                                '/static/angularThings/Letter/LetterInboxCtrl.js',
                                '/static/angularThings/Letter/Sidebar/classSetupSideBar.js',
                                '/static/angularThings/Letter/Compose/LetterComposeService.js',
                                '/static/angularThings/Letter/Compose/LetterComposeCtrl.js'

                            ],
                            catch: true
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })
            .state('letter.inbox', {
                url: '/Inbox',
                parent: 'letter',
                templateUrl: '/page/letter/inbox',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCletterInbox',
                            files: [
                                '/static/angularThings/Letter/LetterInboxService.js',
                                '/static/angularThings/Letter/LetterInboxCtrl.js',

                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })

            .state('process', {
                url: '/Process',
                parent: 'dashboard',
                templateUrl: '/page/processBase',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCprocess',
                            files: [
                                '/static/angularThings/bpms/lunchedProcessService.js'

                            ],
                            catch: true
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })
            .state('process.inbox', {
                url: '/Inbox',
                parent: 'process',
                templateUrl: '/page/process/inbox',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCprocessInbox',
                            files: [
                                '/static/angularThings/bpms/lunchedProcessService.js',
                                '/static/angularThings/companiesManagement/bpmnService.js',
                                '/static/angularThings/bpms/lunchedProcessInboxCtrl.js'
                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })
            .state('process.myProcess', {
                url: '/MyProcess',
                parent: 'process',
                templateUrl: '/page/process/myProcess',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCprocessMyProcess',
                            files: [
                                '/static/angularThings/bpms/lunchedProcessService.js',
                                '/static/angularThings/companiesManagement/bpmnService.js',
                                '/static/angularThings/bpms/lunchedProcessMyProcessCtrl.js'
                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })
            //.state('process.myProcess', {
            //    url: '/MyProcess',
            //    parent: 'process',
            //    templateUrl: '/page/process/myProcess',
            //    resolve: {
            //        deps: ["$ocLazyLoad", function ($ocLazyLoad) {
            //            return $ocLazyLoad.load({
            //                name: 'OCprocessMyProcess',
            //                files: [
            //                    '/static/angularThings/bpms/lunchedProcessService.js',
            //                    '/static/angularThings/companiesManagement/bpmnService.js',
            //                    '/static/angularThings/bpms/lunchedProcessMyProcessCtrl.js'
            //                ],
            //                catch: false // because i have to renew js file
            //            }).then(
            //                function () {
            //
            //
            //                }
            //            )
            //        }]
            //    }
            //
            //})
            .state('process.myDoneProcess', {
                url: '/MyDoneProcess',
                parent: 'process',
                templateUrl: '/page/process/myDoneProcess',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCprocessMyDoneProcess',
                            files: [
                                '/static/angularThings/bpms/lunchedProcessService.js',
                                '/static/angularThings/companiesManagement/bpmnService.js',
                                '/static/angularThings/bpms/lunchedProcessMyDoneProcessCtrl.js'
                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            })
            .state('process.do', {
                url: '/:lunchedProcessId/Do',
                parent: 'process',
                templateUrl: '/page/process/do',
                resolve: {
                    deps: ["$ocLazyLoad", function ($ocLazyLoad) {
                        return $ocLazyLoad.load({
                            name: 'OCprocessDo',
                            files: [
                                //'/static/angularThings/bpms/LunchedProcessDoService.js',
                                '/static/angularThings/companiesManagement/bpmnService.js',
                                '/static/angularThings/bpms/LunchedProcessDoCtrl.js'

                            ],
                            catch: false // because i have to renew js file
                        }).then(
                            function () {


                            }
                        )
                    }]
                }

            });


    }).run(function ($rootScope, $location, $state, Authentication) {


        $rootScope.$on('$stateChangeStart', function (e, toState, toParams, fromState, fromParams) {

                var userInfo = Authentication.isAuthenticated();
                var isLogin = toState.name === "login";
                var signup = toState.name === "signup";
                var forget = toState.name === "forget";
                var ResetPassword = toState.name === "resetpass";
                if (!userInfo) {
                    if ((isLogin ) || (signup) || (forget) || (ResetPassword)) {
                        return; // no need to redirect
                    } else {
                        $location.url('/login'); // go to login
                    }
                }
                if (userInfo) {
                    if ((isLogin ) || (signup )) {
                        $location.url('/dashboard/home'); // go to login
                    }
                }

            }
        );
    });


(function (f) {
    f.module("angularTreeview", []).directive("treeModel", function ($compile) {

        return {
            restrict: "A", link: function (b, h, c) {
                var a = c.treeId, g = c.treeModel, e = c.nodeLabel || "label", d = c.nodeChildren || "children", e = '<ul><li data-ng-repeat="node in ' + g + '"><i class="collapsed" data-ng-show="node.' + d + '.length && node.collapsed" data-ng-click="' + a + '.selectNodeHead(node)"></i><i class="expanded" data-ng-show="node.' + d + '.length && !node.collapsed" data-ng-click="' + a + '.selectNodeHead(node)"></i><i class="normal" data-ng-hide="node.' +
                    d + '.length"></i> <span data-ng-class="node.selected" data-ng-click="' + a + '.selectNodeLabel(node)">//node.' + e + '//</span> <button style="font-size:10px;" data-ng-if="(node.selected)&&(node.isEditable)" type="button" class="btn btn-xs btn-danger fa fa-trash" data-ng-click="deleteFolder(node)"></button><button style="font-size:10px;" data-ng-if="(node.selected)&&(node.isEditable)" type="button" class="btn btn-xs btn-info fa fa-pencil" data-ng-click="editFolder(node)"></button><button style="font-size:10px;" data-ng-if="(node.selected)&&(node.isEditable)" type="button" data-ng-click="newFolder(node)" class="btn btn-xs btn-primary fa fa-plus"></button>  <div data-ng-hide="node.collapsed" data-tree-id="' + a + '" data-tree-model="node.' + d + '" data-node-id=' + (c.nodeId || "id") + " data-node-label=" + e + " data-node-children=" + d + "></div></li></ul>";
                a && g && (c.angularTreeview && (b[a] = b[a] || {}, b[a].selectNodeHead = b[a].selectNodeHead || function (a) {
                    a.collapsed = !a.collapsed
                }, b[a].selectNodeLabel = b[a].selectNodeLabel || function (c) {
                    b[a].currentNode && b[a].currentNode.selected &&
                    (b[a].currentNode.selected = void 0);
                    c.selected = "selected";
                    b[a].currentNode = c
                }), h.html('').append($compile(e)(b)))

            }
        }
    })
})(angular);
