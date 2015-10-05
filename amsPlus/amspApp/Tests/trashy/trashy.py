aa = """
Targets
    Occurrences of 'translate' in Directory /var/www/amsPlus/
Found Occurrences  (4,353 usages found)
    Unclassified occurrence  (3,465 usages found)
        amsPlus  (3,465 usages found)
            amspApp/static/angularThings  (3 usages found)
                app.js  (3 usages found)
                    (66: 24) .config(function ($translateProvider) {
                    (67: 10) $translateProvider.useStaticFilesLoader({
                    (71: 10) $translateProvider.preferredLanguage('en');
            amspApp/static/angularThings/bpms  (2 usages found)
                bpmnFormBuilderCtrl.js  (1 usage found)
                    (4: 66) .controller('bpmnFormBuilderCtrl', function ($scope, $http, $translate, $rootScope, $location, $modal, bpmnService) {
                bpmnTableCtrl.js  (1 usage found)
                    (6: 60) .controller('bpmnTableCtrl', function ($scope, $http, $translate, $rootScope, $modal, $location,bpmnService) {
            amspApp/static/angularThings/companiesManagement  (14 usages found)
                __CompanyMembersCtrl.js  (1 usage found)
                    (3: 78) .controller('CompanyMembersCtrl', function ($scope,$stateParams, $http, $translate, $rootScope, $location, $modal, companiesManagmentService) {
                bpmnModelerCtrl.js  (1 usage found)
                    (5: 62) .controller('bpmnModelerCtrl', function ($scope, $http, $translate, $rootScope,$state,$stateParams,$location, $modal,bpmnService) {
                bpmnSetupCtrl.js  (1 usage found)
                    (4: 60) .controller('bpmnSetupCtrl', function ($scope, $http, $translate, $rootScope,$state,$stateParams, $location, $modal, bpmnService) {
                companiesManagmentCtrl.js  (1 usage found)
                    (7: 16) $translate,
                CompanyChartCtrl.js  (1 usage found)
                    (3: 63) .controller('CompanyChartCtrl', function ($scope, $http, $translate, $rootScope, $stateParams, $location, $modal,
                CompanyCtrl.js  (1 usage found)
                    (3: 58) .controller('CompanyCtrl', function ($scope, $http, $translate, $rootScope,$stateParams, $location, $modal, companiesManagmentService) {
                CompanyDashboardCtrl.js  (1 usage found)
                    (3: 67) .controller('CompanyDashboardCtrl', function ($scope, $http, $translate, $rootScope, $location, $modal, bpmnService) {
                CompanyProcessCtrl.js  (1 usage found)
                    (6: 65) .controller('CompanyProcessCtrl', function ($scope, $http, $translate, $rootScope,$state,$stateParams, $modal, $location,bpmnService) {
                CompanyProductsCtrl.js  (1 usage found)
                    (3: 66) .controller('CompanyProductsCtrl', function ($scope, $http, $translate, $rootScope,$stateParams, $location, $modal, companiesManagmentService) {
                CompanyProfileCtrl.js  (1 usage found)
                    (23: 69) .controller('CompanyProfileCtrl', function ($scope, $http, $q, $translate, $rootScope, $stateParams, $location, $modal, companiesManagmentService) {
                companyTableCtrl.js  (2 usages found)
                    (5: 70) $translate,
                    (132: 16) $translate,
                MembersCtrl.js  (1 usage found)
                    (5: 79) .controller('CompanyMembersCtrl', function ($scope, $http, $stateParams, $translate, $rootScope, $location, $modal, CompanyMembersService) {
                SecretaraitsCtrl.js  (1 usage found)
                    (3: 106) angular.module('AniTheme').controller('CompanySecretaraitsCtrl', function ($scope, $http, $stateParams, $translate, $rootScope, $location, $modal, CompanySecretiatsService) {
            amspApp/static/angularThings/friends  (1 usage found)
                friendsCtrl.js  (1 usage found)
                    (7: 16) $translate,
            amspApp/static/angularThings/Letter  (6 usages found)
                LetterComposeCtrl.js  (3 usages found)
                    (79: 16) $translate,
                    (344: 113) angular.module('AniTheme').controller('ModalLabelCreateInstanceCtrl', function ($scope, $modalInstance, $http, $translate, LetterInboxService, oldLabel) {
                    (382: 111) angular.module('AniTheme').controller('GroupEditModalInstanceCtrl', function ($scope, $modalInstance, $http, $translate, LetterInboxService, oldGroup) {
                LetterInboxCtrl.js  (3 usages found)
                    (7: 16) $translate,
                    (256: 113) angular.module('AniTheme').controller('ModalLabelCreateInstanceCtrl', function ($scope, $modalInstance, $http, $translate, LetterInboxService, oldLabel) {
                    (294: 111) angular.module('AniTheme').controller('GroupEditModalInstanceCtrl', function ($scope, $modalInstance, $http, $translate, LetterInboxService, oldGroup) {
            amspApp/static/angularThings/myProfile  (1 usage found)
                myProfileCrtl.js  (1 usage found)
                    (7: 16) $translate,
            amspApp/static/angularThings/others/controllers  (10 usages found)
                dashboard.js  (3 usages found)
                    (11: 61) .controller('DashboardCtrl', function ($scope, $state, $translate, $rootScope) {
                    (50: 14) $translate.use(l);
                    (56: 102) .controller('CurrentCompanyCtrl', function ($scope, $http, $state, $stateParams,$templateCache, $translate, $location, $rootScope, companiesManagmentService) {
                dojobCtrl.js  (1 usage found)
                    (4: 56) .controller('dojobCtrl', function ($scope, $http, $translate, $rootScope, $stateParams, $modal, $location, taskService, bpmnService) {
                groupTableCtrl.js  (3 usages found)
                    (5: 61) .controller('groupTableCtrl', function ($scope, $http, $translate, $rootScope, $modal) {
                    (138: 111) angular.module('AniTheme').controller('ModalGroupEditInstanceCtrl', function ($scope, $modalInstance, $http, $translate, group, groupOld) {
                    (194: 113) angular.module('AniTheme').controller('ModalGroupCreateInstanceCtrl', function ($scope, $modalInstance, $http, $translate) {
                taskTableCtrl.js  (2 usages found)
                    (6: 61) .controller('TasksTableCtrl', function ($scope, $http, $translate, $rootScope, $modal, $location, taskService, bpmnService) {
                    (127: 112) angular.module('AniTheme').controller('ModalTaskCreateInstanceCtrl', function ($scope, $modalInstance, $http, $translate, bpmns) {
                userTableCtrl.js  (1 usage found)
                    (5: 60) .controller('userTableCtrl', function ($scope, $http, $translate, $rootScope, $modal) {
            amspApp/static/angularThings/others/directives/to-do-list  (2 usages found)
                to-do.html  (2 usages found)
                    (4: 53) <h4><i class="fa fa-tasks"></i>&nbsp;{{ 'todo' | translate }}</h4>
                    (26: 87) <button class="btn btn-default" ng-click="addTodo()" type="submit">{{ 'add' | translate }}</button>
            amspApp/static/bower_components  (2 usages found)
                masonry.js  (2 usages found)
                    (9: 14198) getTranslate
                    (9: 14315) getTranslate
            amspApp/static/bower_components/angular-chart.js/examples  (6 usages found)
                bootstrap.css  (6 usages found)
                    (5105: 22) -webkit-transform: translate(0, -25%);
                    (5106: 22) -ms-transform: translate(0, -25%);
                    (5107: 22) transform: translate(0, -25%);
                    (5110: 22) -webkit-transform: translate(0, 0);
                    (5111: 22) -ms-transform: translate(0, 0);
                    (5112: 22) transform: translate(0, 0);
            amspApp/static/bower_components/angular-growl  (6 usages found)
                README.md  (6 usages found)
                    (12: 49) * automatic translation of messages if [angular-translate](https://github.com/PascalPrecht/angular-translate) filter is
                    (12: 100) * automatic translation of messages if [angular-translate](https://github.com/PascalPrecht/angular-translate) filter is
                    (13: 61) present, you only have to provide keys as messages, angular-translate will translate them
                    (13: 76) present, you only have to provide keys as messages, angular-translate will translate them
                    (97: 13) If [angular-translate](https://github.com/PascalPrecht/angular-translate) is present, its filter is automatically called for translating of messages, so you have to provide
                    (97: 64) If [angular-translate](https://github.com/PascalPrecht/angular-translate) is present, its filter is automatically called for translating of messages, so you have to provide
            amspApp/static/bower_components/angular-growl/build  (4 usages found)
                angular-growl.js  (4 usages found)
                    (113: 11) var translate;
                    (115: 9) translate = $filter('translate');
                    (119: 13) if (translate) {
                    (120: 26) message.text = translate(message.text);
            amspApp/static/bower_components/angular-progress-button-styles/dist  (64 usages found)
                angular-progress-button-styles.css  (32 usages found)
                    (94: 26) -webkit-transform: translateX(-50%);
                    (95: 18) transform: translateX(-50%); }
                    (97: 24) -webkit-transform: translateY(-100%);
                    (98: 16) transform: translateY(-100%); }
                    (112: 26) -webkit-transform: translateX(-50%);
                    (113: 18) transform: translateX(-50%); }
                    (115: 24) -webkit-transform: translateY(-100%);
                    (116: 16) transform: translateY(-100%); }
                    (131: 24) -webkit-transform: translateX(-50%);
                    (132: 16) transform: translateX(-50%); }
                    (139: 22) -webkit-transform: translateY(-100%);
                    (140: 14) transform: translateY(-100%); }
                    (155: 24) -webkit-transform: translateX(-50%);
                    (156: 16) transform: translateX(-50%); }
                    (163: 22) -webkit-transform: translateY(-100%);
                    (164: 14) transform: translateY(-100%); }
                    (240: 37) -webkit-transform: rotateX(90deg) translateZ(10px);
                    (241: 29) transform: rotateX(90deg) translateZ(10px); }
                    (255: 38) -webkit-transform: rotateX(-90deg) translateZ(10px);
                    (256: 30) transform: rotateX(-90deg) translateZ(10px); }
                    (271: 22) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (271: 53) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (272: 14) transform: translateX(50%) rotateY(90deg) translateZ(10px); }
                    (272: 45) transform: translateX(50%) rotateY(90deg) translateZ(10px); }
                    (287: 22) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (287: 55) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (288: 14) transform: translateX(-50%) rotateY(-90deg) translateZ(10px); }
                    (288: 47) transform: translateX(-50%) rotateY(-90deg) translateZ(10px); }
                    (348: 24) -webkit-transform: translateY(10px);
                    (349: 16) transform: translateY(10px); }
                    (369: 24) -webkit-transform: translateY(-10px);
                    (370: 16) transform: translateY(-10px); }
                angular-progress-button-styles.min.css  (32 usages found)
                    (1: 2348) translateX
                    (1: 2375) translateX
                    (1: 2572) translateY
                    (1: 2600) translateY
                    (1: 3080) translateX
                    (1: 3107) translateX
                    (1: 3300) translateY
                    (1: 3328) translateY
                    (1: 3760) translateX
                    (1: 3787) translateX
                    (1: 4207) translateY
                    (1: 4235) translateY
                    (1: 4773) translateX
                    (1: 4800) translateX
                    (1: 5212) translateY
                    (1: 5240) translateY
                    (1: 7173) translateZ
                    (1: 7215) translateZ
                    (1: 7621) translateZ
                    (1: 7664) translateZ
                    (1: 8093) translateX
                    (1: 8124) translateZ
                    (1: 8151) translateX
                    (1: 8182) translateZ
                    (1: 8623) translateX
                    (1: 8656) translateZ
                    (1: 8683) translateX
                    (1: 8716) translateZ
                    (1: 10252) translateY
                    (1: 10279) translateY
                    (1: 10734) translateY
                    (1: 10762) translateY
            amspApp/static/bower_components/angular-progress-button-styles/sass  (32 usages found)
                _fill-horizontal.scss  (4 usages found)
                    (16: 36) -webkit-transform: translateX(-50%);
                    (17: 28) transform: translateX(-50%);
                    (23: 36) -webkit-transform: translateY(-100%);
                    (24: 28) transform: translateY(-100%);
                _fill-vertical.scss  (4 usages found)
                    (15: 36) -webkit-transform: translateX(-50%);
                    (16: 28) transform: translateX(-50%);
                    (22: 36) -webkit-transform: translateY(-100%);
                    (23: 28) transform: translateY(-100%);
                _move-up.scss  (2 usages found)
                    (24: 28) -webkit-transform: translateY(-10px);
                    (25: 20) transform: translateY(-10px);
                _rotate-side.scss  (12 usages found)
                    (17: 47) -webkit-transform: rotateX(90deg) translateZ(10px);
                    (18: 39) transform: rotateX(90deg) translateZ(10px);
                    (38: 48) -webkit-transform: rotateX(-90deg) translateZ(10px);
                    (39: 40) transform: rotateX(-90deg) translateZ(10px);
                    (62: 32) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (62: 63) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (63: 24) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (63: 55) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (86: 32) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (86: 65) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (87: 24) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (87: 57) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                _shrink-horizontal.scss  (4 usages found)
                    (19: 36) -webkit-transform: translateX(-50%);
                    (20: 28) transform: translateX(-50%);
                    (34: 36) -webkit-transform: translateY(-100%);
                    (35: 28) transform: translateY(-100%);
                _shrink-vertical.scss  (4 usages found)
                    (19: 36) -webkit-transform: translateX(-50%);
                    (20: 28) transform: translateX(-50%);
                    (34: 36) -webkit-transform: translateY(-100%);
                    (35: 28) transform: translateY(-100%);
                _slide-down.scss  (2 usages found)
                    (24: 28) -webkit-transform: translateY(10px);
                    (25: 20) transform: translateY(10px);
            amspApp/static/bower_components/angular-translate  (175 usages found)
                angular-translate.js  (143 usages found)
                    (30: 11) .run(runTranslate);
                    (32: 13) function runTranslate($translate) {
                    (32: 24) function runTranslate($translate) {
                    (36: 14) var key = $translate.storageKey(),
                    (37: 16) storage = $translate.storage();
                    (40: 22) var preferred = $translate.preferredLanguage();
                    (42: 8) $translate.use(preferred);
                    (46: 25) storage.put(key, $translate.use());
                    (56: 8) $translate.use(storage.get(key))['catch'](fallbackFromIncorrectStorageValue);
                    (58: 32) } else if (angular.isString($translate.preferredLanguage())) {
                    (59: 6) $translate.use($translate.preferredLanguage());
                    (59: 21) $translate.use($translate.preferredLanguage());
                    (62: 4) runTranslate.$inject = ['$translate'];
                    (64: 4) runTranslate.displayName = 'runTranslate';
                    (74: 78) angular.module('pascalprecht.translate').provider('$translateSanitization', $translateSanitizationProvider);
                    (76: 11) function $translateSanitizationProvider () {
                    (323: 26) .provider('$translate', $translate);
                    (325: 11) function $translate($STORAGE_KEY, $windowProvider, $translateSanitizationProvider, pascalprechtTranslateOverrider) {
                    (325: 53) function $translate($STORAGE_KEY, $windowProvider, $translateSanitizationProvider, pascalprechtTranslateOverrider) {
                    (325: 96) function $translate($STORAGE_KEY, $windowProvider, $translateSanitizationProvider, pascalprechtTranslateOverrider) {
                    (377: 40) if (angular.isFunction(pascalprechtTranslateOverrider.getLocale)) {
                    (378: 26) return pascalprechtTranslateOverrider.getLocale();
                    (670: 6) $translateSanitizationProvider.useStrategy(value);
                    (1281: 12) var $translate = function (translationId, interpolateParams, interpolationId, defaultTranslationText) {
                    (1289: 15) var translateAll = function (translationIds) {
                    (1293: 17) var translate = function (translationId) {
                    (1300: 16) $translate(translationId, interpolateParams, interpolationId, defaultTranslationText).then(regardless, regardless);
                    (1304: 29) promises.push(translate(translationIds[i]));
                    (1312: 18) return translateAll(translationId);
                    (1409: 24) Storage.put($translate.storageKey(), $uses);
                    (1623: 11) var translateByHandler = function (translationId, interpolateParams) {
                    (1672: 30) deferred.resolve(translateByHandler(translationId, interpolateParams));
                    (1744: 14) $translate(translation.substr(2), interpolateParams, interpolationId, defaultTranslationText)
                    (1753: 52) missingTranslationHandlerTranslation = translateByHandler(translationId, interpolateParams);
                    (1810: 52) missingTranslationHandlerTranslation = translateByHandler(translationId, interpolateParams);
                    (1851: 8) $translate.preferredLanguage = function (langKey) {
                    (1868: 8) $translate.cloakClassName = function () {
                    (1884: 8) $translate.fallbackLanguage = function (langKey) {
                    (1899: 12) $translate.use($translate.use());
                    (1899: 27) $translate.use($translate.use());
                    (1921: 8) $translate.useFallbackLanguage = function (langKey) {
                    (1946: 8) $translate.proposedLanguage = function () {
                    (1960: 8) $translate.storage = function () {
                    (1986: 8) $translate.use = function (key) {
                    (2047: 8) $translate.storageKey = function () {
                    (2061: 8) $translate.isPostCompilingEnabled = function () {
                    (2075: 8) $translate.isForceAsyncReloadEnabled = function () {
                    (2108: 8) $translate.refresh = function (langKey) {
                    (2197: 8) $translate.instant = function (translationId, interpolateParams, interpolationId) {
                    (2209: 42) results[translationId[i]] = $translate.instant(translationId[i], interpolateParams, interpolationId);
                    (2252: 22) result = translateByHandler(translationId, interpolateParams);
                    (2269: 8) $translate.versionInfo = function () {
                    (2283: 8) $translate.loaderCache = function () {
                    (2288: 8) $translate.directivePriority = function () {
                    (2293: 8) $translate.statefulFilter = function () {
                    (2302: 12) $translate.use($translate.use());
                    (2302: 27) $translate.use($translate.use());
                    (2322: 15) return $translate;
                    (2326: 2) $translate.$inject = ['$STORAGE_KEY', '$windowProvider', '$translateSanitizationProvider', 'pascalprechtTranslateOverrider'];
                    (2328: 2) $translate.displayName = 'displayName';
                    (2345: 85) angular.module('pascalprecht.translate').factory('$translateDefaultInterpolation', $translateDefaultInterpolation);
                    (2347: 11) function $translateDefaultInterpolation ($interpolate, $translateSanitization) {
                    (2347: 57) function $translateDefaultInterpolation ($interpolate, $translateSanitization) {
                    (2351: 8) var $translateInterpolator = {},
                    (2365: 4) $translateInterpolator.setLocale = function (locale) {
                    (2379: 4) $translateInterpolator.getInterpolationIdentifier = function () {
                    (2387: 4) $translateInterpolator.useSanitizeValueStrategy = function (value) {
                    (2388: 6) $translateSanitization.useStrategy(value);
                    (2403: 4) $translateInterpolator.interpolate = function (string, interpolationParams) {
                    (2405: 28) interpolationParams = $translateSanitization.sanitize(interpolationParams, 'params');
                    (2408: 25) interpolatedText = $translateSanitization.sanitize(interpolatedText, 'text');
                    (2413: 11) return $translateInterpolator;
                    (2415: 2) $translateDefaultInterpolation.$inject = ['$interpolate', '$translateSanitization'];
                    (2417: 2) $translateDefaultInterpolation.displayName = '$translateDefaultInterpolation';
                    (2508: 25) .directive('translate', translateDirective);
                    (2509: 10) function translateDirective($translate, $q, $interpolate, $compile, $parse, $rootScope) {
                    (2509: 30) function translateDirective($translate, $q, $interpolate, $compile, $parse, $rootScope) {
                    (2529: 16) priority: $translate.directivePriority(),
                    (2532: 11) var translateValuesExist = (tAttr.translateValues) ?
                    (2532: 41) var translateValuesExist = (tAttr.translateValues) ?
                    (2533: 15) tAttr.translateValues : undefined;
                    (2535: 11) var translateInterpolation = (tAttr.translateInterpolation) ?
                    (2535: 43) var translateInterpolation = (tAttr.translateInterpolation) ?
                    (2536: 15) tAttr.translateInterpolation : undefined;
                    (2538: 11) var translateValueExist = tElement[0].outerHTML.match(/translate-value-+/i);
                    (2552: 21) if (iAttr.translateValues) {
                    (2553: 60) angular.extend(interpolateParams, $parse(iAttr.translateValues)(scope.$parent));
                    (2556: 15) if (translateValueExist) {
                    (2584: 30) translationIds.translate = $interpolate(interpolateMatches[2])(scope.$parent);
                    (2588: 34) translationIds.translate = newValue;
                    (2593: 30) translationIds.translate = iElement.text().replace(/^\s+|\s+$/g,'');
                    (2596: 28) translationIds.translate = translationId;
                    (2601: 53) var observeAttributeTranslation = function (translateAttr) {
                    (2602: 26) iAttr.$observe(translateAttr, function (translationId) {
                    (2603: 28) translationIds[translateAttr] = translationId;
                    (2619: 30) translationIds.translate = translationId;
                    (2626: 18) for (var translateAttr in iAttr) {
                    (2627: 36) if (iAttr.hasOwnProperty(translateAttr) && translateAttr.substr(0, 13) === 'translateAttr') {
                    (2627: 54) if (iAttr.hasOwnProperty(translateAttr) && translateAttr.substr(0, 13) === 'translateAttr') {
                    (2628: 41) observeAttributeTranslation(translateAttr);
                    (2636: 13) if (translateValuesExist) {
                    (2646: 13) if (translateValueExist) {
                    (2671: 42) var updateTranslation = function(translateAttr, translationId, scope, interpolateParams, defaultTranslationText) {
                    (2673: 14) $translate(translationId, interpolateParams, translateInterpolation, defaultTranslationText)
                    (2673: 58) $translate(translationId, interpolateParams, translateInterpolation, defaultTranslationText)
                    (2675: 60) applyTranslation(translation, scope, true, translateAttr);
                    (2677: 63) applyTranslation(translationId, scope, false, translateAttr);
                    (2681: 59) applyTranslation(translationId, scope, false, translateAttr);
                    (2685: 68) var applyTranslation = function (value, scope, successful, translateAttr) {
                    (2686: 15) if (translateAttr === 'translate') {
                    (2692: 36) var globallyEnabled = $translate.isPostCompilingEnabled();
                    (2693: 47) var locallyDefined = typeof tAttr.translateCompile !== 'undefined';
                    (2694: 58) var locallyEnabled = locallyDefined && tAttr.translateCompile !== 'false';
                    (2703: 45) var attributeName = iAttr.$attr[translateAttr];
                    (2713: 13) if (translateValuesExist || translateValueExist || iAttr.translateDefault) {
                    (2713: 37) if (translateValuesExist || translateValueExist || iAttr.translateDefault) {
                    (2713: 66) if (translateValuesExist || translateValueExist || iAttr.translateDefault) {
                    (2723: 21) if (iAttr.translate) {
                    (2724: 45) observeElementTranslation(iAttr.translate);
                    (2728: 26) } else if (iAttr.translate) {
                    (2730: 43) observeElementTranslation(iAttr.translate);
                    (2738: 1) translateDirective.$inject = ['$translate', '$q', '$interpolate', '$compile', '$parse', '$rootScope'];
                    (2740: 1) translateDirective.displayName = 'translateDirective';
                    (2764: 30) .directive('translateCloak', translateCloakDirective);
                    (2766: 10) function translateCloakDirective($rootScope, $translate) {
                    (2766: 47) function translateCloakDirective($rootScope, $translate) {
                    (2773: 28) tElement.addClass($translate.cloakClassName());
                    (2776: 31) tElement.removeClass($translate.cloakClassName());
                    (2787: 19) if (iAttr.translateCloak && iAttr.translateCloak.length) {
                    (2787: 43) if (iAttr.translateCloak && iAttr.translateCloak.length) {
                    (2789: 14) $translate(translationId).then(removeCloak, applyCloak);
                    (2796: 1) translateCloakDirective.$inject = ['$rootScope', '$translate'];
                    (2798: 1) translateCloakDirective.displayName = 'translateCloakDirective';
                    (2852: 22) .filter('translate', translateFilterFactory);
                    (2854: 10) function translateFilterFactory($parse, $translate) {
                    (2854: 42) function translateFilterFactory($parse, $translate) {
                    (2858: 7) var translateFilter = function (translationId, interpolateParams, interpolation) {
                    (2864: 13) return $translate.instant(translationId, interpolateParams, interpolation);
                    (2867: 8) if ($translate.statefulFilter()) {
                    (2868: 5) translateFilter.$stateful = true;
                    (2871: 10) return translateFilter;
                    (2873: 1) translateFilterFactory.$inject = ['$parse', '$translate'];
                    (2875: 1) translateFilterFactory.displayName = 'translateFilterFactory';
                angular-translate.min.js  (20 usages found)
                    (6: 14171) translateValues
                    (6: 14189) translateValues
                    (6: 14216) translateInterpolation
                    (6: 14241) translateInterpolation
                    (6: 14529) translateValues
                    (6: 14567) translateValues
                    (6: 15007) translate
                    (6: 15142) translate
                    (6: 15168) translate
                    (6: 15219) translate
                    (6: 15402) translate
                    (6: 16346) translateCompile
                    (6: 16380) translateCompile
                    (6: 16585) translateDefault
                    (6: 16700) translate
                    (6: 16712) translate
                    (6: 16728) translate
                    (6: 16743) translate
                    (6: 17021) translateCloak
                    (6: 17039) translateCloak
                README.md  (12 usages found)
                    (1: 11) # angular-translate (bower shadow repository)
                    (3: 52) This is the _Bower shadow_ repository for *angular-translate*.
                    (7: 68) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 86) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 124) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 142) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (14: 25) $ bower install angular-translate
                    (19: 59) Please have a look at https://cdnjs.com/libraries/angular-translate for specific versions.
                    (23: 50) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 68) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 106) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 124) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
            amspApp/static/bower_components/angular-translate-loader-static-files  (16 usages found)
                angular-translate-loader-static-files.js  (4 usages found)
                    (36: 42) .factory('$translateStaticFilesLoader', $translateStaticFilesLoader);
                    (38: 11) function $translateStaticFilesLoader($q, $http) {
                    (109: 2) $translateStaticFilesLoader.$inject = ['$q', '$http'];
                    (111: 2) $translateStaticFilesLoader.displayName = '$translateStaticFilesLoader';
                README.md  (12 usages found)
                    (1: 11) # angular-translate-loader-static-files (bower shadow repository)
                    (3: 52) This is the _Bower shadow_ repository for *angular-translate-loader-static-files*.
                    (7: 68) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 86) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 124) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 142) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (14: 25) $ bower install angular-translate-loader-static-files
                    (19: 59) Please have a look at https://cdnjs.com/libraries/angular-translate-loader-static-files for specific versions.
                    (23: 50) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 68) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 106) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 124) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
            amspApp/static/bower_components/angular-translate-loader-url  (16 usages found)
                angular-translate-loader-url.js  (4 usages found)
                    (40: 34) .factory('$translateUrlLoader', $translateUrlLoader);
                    (42: 11) function $translateUrlLoader($q, $http) {
                    (70: 2) $translateUrlLoader.$inject = ['$q', '$http'];
                    (72: 2) $translateUrlLoader.displayName = '$translateUrlLoader';
                README.md  (12 usages found)
                    (1: 11) # angular-translate-loader-url (bower shadow repository)
                    (3: 52) This is the _Bower shadow_ repository for *angular-translate-loader-url*.
                    (7: 68) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 86) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 124) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (7: 142) Please file any issues and bugs in our main repository at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate/issues).
                    (14: 25) $ bower install angular-translate-loader-url
                    (19: 59) Please have a look at https://cdnjs.com/libraries/angular-translate-loader-url for specific versions.
                    (23: 50) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 68) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 106) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
                    (23: 124) Licensed under MIT. See more details at [angular-translate/angular-translate](https://github.com/angular-translate/angular-translate).
            amspApp/static/bower_components/animate.css  (752 usages found)
                animate.css  (376 usages found)
                    (43: 24) -webkit-transform: translate3d(0,0,0);
                    (44: 16) transform: translate3d(0,0,0);
                    (50: 24) -webkit-transform: translate3d(0, -30px, 0);
                    (51: 16) transform: translate3d(0, -30px, 0);
                    (57: 24) -webkit-transform: translate3d(0, -15px, 0);
                    (58: 16) transform: translate3d(0, -15px, 0);
                    (62: 24) -webkit-transform: translate3d(0,-4px,0);
                    (63: 16) transform: translate3d(0,-4px,0);
                    (71: 24) -webkit-transform: translate3d(0,0,0);
                    (72: 16) transform: translate3d(0,0,0);
                    (78: 24) -webkit-transform: translate3d(0, -30px, 0);
                    (79: 16) transform: translate3d(0, -30px, 0);
                    (85: 24) -webkit-transform: translate3d(0, -15px, 0);
                    (86: 16) transform: translate3d(0, -15px, 0);
                    (90: 24) -webkit-transform: translate3d(0,-4px,0);
                    (91: 16) transform: translate3d(0,-4px,0);
                    (249: 24) -webkit-transform: translate3d(0, 0, 0);
                    (250: 16) transform: translate3d(0, 0, 0);
                    (254: 24) -webkit-transform: translate3d(-10px, 0, 0);
                    (255: 16) transform: translate3d(-10px, 0, 0);
                    (259: 24) -webkit-transform: translate3d(10px, 0, 0);
                    (260: 16) transform: translate3d(10px, 0, 0);
                    (266: 24) -webkit-transform: translate3d(0, 0, 0);
                    (267: 16) transform: translate3d(0, 0, 0);
                    (271: 24) -webkit-transform: translate3d(-10px, 0, 0);
                    (272: 16) transform: translate3d(-10px, 0, 0);
                    (276: 24) -webkit-transform: translate3d(10px, 0, 0);
                    (277: 16) transform: translate3d(10px, 0, 0);
                    (415: 24) -webkit-transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
                    (416: 16) transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
                    (420: 24) -webkit-transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
                    (421: 16) transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
                    (425: 24) -webkit-transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
                    (426: 16) transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
                    (430: 24) -webkit-transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
                    (431: 16) transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
                    (435: 24) -webkit-transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
                    (436: 16) transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
                    (452: 24) -webkit-transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
                    (453: 16) transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
                    (457: 24) -webkit-transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
                    (458: 16) transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
                    (462: 24) -webkit-transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
                    (463: 16) transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
                    (467: 24) -webkit-transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
                    (468: 16) transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
                    (472: 24) -webkit-transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
                    (473: 16) transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
                    (580: 24) -webkit-transform: translate3d(0, -3000px, 0);
                    (581: 16) transform: translate3d(0, -3000px, 0);
                    (586: 24) -webkit-transform: translate3d(0, 25px, 0);
                    (587: 16) transform: translate3d(0, 25px, 0);
                    (591: 24) -webkit-transform: translate3d(0, -10px, 0);
                    (592: 16) transform: translate3d(0, -10px, 0);
                    (596: 24) -webkit-transform: translate3d(0, 5px, 0);
                    (597: 16) transform: translate3d(0, 5px, 0);
                    (614: 24) -webkit-transform: translate3d(0, -3000px, 0);
                    (615: 16) transform: translate3d(0, -3000px, 0);
                    (620: 24) -webkit-transform: translate3d(0, 25px, 0);
                    (621: 16) transform: translate3d(0, 25px, 0);
                    (625: 24) -webkit-transform: translate3d(0, -10px, 0);
                    (626: 16) transform: translate3d(0, -10px, 0);
                    (630: 24) -webkit-transform: translate3d(0, 5px, 0);
                    (631: 16) transform: translate3d(0, 5px, 0);
                    (653: 24) -webkit-transform: translate3d(-3000px, 0, 0);
                    (654: 16) transform: translate3d(-3000px, 0, 0);
                    (659: 24) -webkit-transform: translate3d(25px, 0, 0);
                    (660: 16) transform: translate3d(25px, 0, 0);
                    (664: 24) -webkit-transform: translate3d(-10px, 0, 0);
                    (665: 16) transform: translate3d(-10px, 0, 0);
                    (669: 24) -webkit-transform: translate3d(5px, 0, 0);
                    (670: 16) transform: translate3d(5px, 0, 0);
                    (687: 24) -webkit-transform: translate3d(-3000px, 0, 0);
                    (688: 16) transform: translate3d(-3000px, 0, 0);
                    (693: 24) -webkit-transform: translate3d(25px, 0, 0);
                    (694: 16) transform: translate3d(25px, 0, 0);
                    (698: 24) -webkit-transform: translate3d(-10px, 0, 0);
                    (699: 16) transform: translate3d(-10px, 0, 0);
                    (703: 24) -webkit-transform: translate3d(5px, 0, 0);
                    (704: 16) transform: translate3d(5px, 0, 0);
                    (726: 24) -webkit-transform: translate3d(3000px, 0, 0);
                    (727: 16) transform: translate3d(3000px, 0, 0);
                    (732: 24) -webkit-transform: translate3d(-25px, 0, 0);
                    (733: 16) transform: translate3d(-25px, 0, 0);
                    (737: 24) -webkit-transform: translate3d(10px, 0, 0);
                    (738: 16) transform: translate3d(10px, 0, 0);
                    (742: 24) -webkit-transform: translate3d(-5px, 0, 0);
                    (743: 16) transform: translate3d(-5px, 0, 0);
                    (760: 24) -webkit-transform: translate3d(3000px, 0, 0);
                    (761: 16) transform: translate3d(3000px, 0, 0);
                    (766: 24) -webkit-transform: translate3d(-25px, 0, 0);
                    (767: 16) transform: translate3d(-25px, 0, 0);
                    (771: 24) -webkit-transform: translate3d(10px, 0, 0);
                    (772: 16) transform: translate3d(10px, 0, 0);
                    (776: 24) -webkit-transform: translate3d(-5px, 0, 0);
                    (777: 16) transform: translate3d(-5px, 0, 0);
                    (799: 24) -webkit-transform: translate3d(0, 3000px, 0);
                    (800: 16) transform: translate3d(0, 3000px, 0);
                    (805: 24) -webkit-transform: translate3d(0, -20px, 0);
                    (806: 16) transform: translate3d(0, -20px, 0);
                    (810: 24) -webkit-transform: translate3d(0, 10px, 0);
                    (811: 16) transform: translate3d(0, 10px, 0);
                    (815: 24) -webkit-transform: translate3d(0, -5px, 0);
                    (816: 16) transform: translate3d(0, -5px, 0);
                    (820: 24) -webkit-transform: translate3d(0, 0, 0);
                    (821: 16) transform: translate3d(0, 0, 0);
                    (833: 24) -webkit-transform: translate3d(0, 3000px, 0);
                    (834: 16) transform: translate3d(0, 3000px, 0);
                    (839: 24) -webkit-transform: translate3d(0, -20px, 0);
                    (840: 16) transform: translate3d(0, -20px, 0);
                    (844: 24) -webkit-transform: translate3d(0, 10px, 0);
                    (845: 16) transform: translate3d(0, 10px, 0);
                    (849: 24) -webkit-transform: translate3d(0, -5px, 0);
                    (850: 16) transform: translate3d(0, -5px, 0);
                    (854: 24) -webkit-transform: translate3d(0, 0, 0);
                    (855: 16) transform: translate3d(0, 0, 0);
                    (909: 24) -webkit-transform: translate3d(0, 10px, 0);
                    (910: 16) transform: translate3d(0, 10px, 0);
                    (915: 24) -webkit-transform: translate3d(0, -20px, 0);
                    (916: 16) transform: translate3d(0, -20px, 0);
                    (921: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (922: 16) transform: translate3d(0, 2000px, 0);
                    (928: 24) -webkit-transform: translate3d(0, 10px, 0);
                    (929: 16) transform: translate3d(0, 10px, 0);
                    (934: 24) -webkit-transform: translate3d(0, -20px, 0);
                    (935: 16) transform: translate3d(0, -20px, 0);
                    (940: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (941: 16) transform: translate3d(0, 2000px, 0);
                    (953: 24) -webkit-transform: translate3d(20px, 0, 0);
                    (954: 16) transform: translate3d(20px, 0, 0);
                    (959: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (960: 16) transform: translate3d(-2000px, 0, 0);
                    (967: 24) -webkit-transform: translate3d(20px, 0, 0);
                    (968: 16) transform: translate3d(20px, 0, 0);
                    (973: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (974: 16) transform: translate3d(-2000px, 0, 0);
                    (986: 24) -webkit-transform: translate3d(-20px, 0, 0);
                    (987: 16) transform: translate3d(-20px, 0, 0);
                    (992: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (993: 16) transform: translate3d(2000px, 0, 0);
                    (1000: 24) -webkit-transform: translate3d(-20px, 0, 0);
                    (1001: 16) transform: translate3d(-20px, 0, 0);
                    (1006: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (1007: 16) transform: translate3d(2000px, 0, 0);
                    (1018: 24) -webkit-transform: translate3d(0, -10px, 0);
                    (1019: 16) transform: translate3d(0, -10px, 0);
                    (1024: 24) -webkit-transform: translate3d(0, 20px, 0);
                    (1025: 16) transform: translate3d(0, 20px, 0);
                    (1030: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1031: 16) transform: translate3d(0, -2000px, 0);
                    (1037: 24) -webkit-transform: translate3d(0, -10px, 0);
                    (1038: 16) transform: translate3d(0, -10px, 0);
                    (1043: 24) -webkit-transform: translate3d(0, 20px, 0);
                    (1044: 16) transform: translate3d(0, 20px, 0);
                    (1049: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1050: 16) transform: translate3d(0, -2000px, 0);
                    (1087: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (1088: 16) transform: translate3d(0, -100%, 0);
                    (1101: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (1102: 16) transform: translate3d(0, -100%, 0);
                    (1120: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1121: 16) transform: translate3d(0, -2000px, 0);
                    (1134: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1135: 16) transform: translate3d(0, -2000px, 0);
                    (1153: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (1154: 16) transform: translate3d(-100%, 0, 0);
                    (1167: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (1168: 16) transform: translate3d(-100%, 0, 0);
                    (1186: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (1187: 16) transform: translate3d(-2000px, 0, 0);
                    (1200: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (1201: 16) transform: translate3d(-2000px, 0, 0);
                    (1219: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (1220: 16) transform: translate3d(100%, 0, 0);
                    (1233: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (1234: 16) transform: translate3d(100%, 0, 0);
                    (1252: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (1253: 16) transform: translate3d(2000px, 0, 0);
                    (1266: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (1267: 16) transform: translate3d(2000px, 0, 0);
                    (1285: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (1286: 16) transform: translate3d(0, 100%, 0);
                    (1299: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (1300: 16) transform: translate3d(0, 100%, 0);
                    (1318: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (1319: 16) transform: translate3d(0, 2000px, 0);
                    (1332: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (1333: 16) transform: translate3d(0, 2000px, 0);
                    (1380: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (1381: 16) transform: translate3d(0, 100%, 0);
                    (1392: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (1393: 16) transform: translate3d(0, 100%, 0);
                    (1409: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (1410: 16) transform: translate3d(0, 2000px, 0);
                    (1421: 24) -webkit-transform: translate3d(0, 2000px, 0);
                    (1422: 16) transform: translate3d(0, 2000px, 0);
                    (1438: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (1439: 16) transform: translate3d(-100%, 0, 0);
                    (1450: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (1451: 16) transform: translate3d(-100%, 0, 0);
                    (1467: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (1468: 16) transform: translate3d(-2000px, 0, 0);
                    (1479: 24) -webkit-transform: translate3d(-2000px, 0, 0);
                    (1480: 16) transform: translate3d(-2000px, 0, 0);
                    (1496: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (1497: 16) transform: translate3d(100%, 0, 0);
                    (1508: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (1509: 16) transform: translate3d(100%, 0, 0);
                    (1525: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (1526: 16) transform: translate3d(2000px, 0, 0);
                    (1537: 24) -webkit-transform: translate3d(2000px, 0, 0);
                    (1538: 16) transform: translate3d(2000px, 0, 0);
                    (1554: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (1555: 16) transform: translate3d(0, -100%, 0);
                    (1566: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (1567: 16) transform: translate3d(0, -100%, 0);
                    (1583: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1584: 16) transform: translate3d(0, -2000px, 0);
                    (1595: 24) -webkit-transform: translate3d(0, -2000px, 0);
                    (1596: 16) transform: translate3d(0, -2000px, 0);
                    (1614: 43) -webkit-transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -190deg);
                    (1615: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -190deg);
                    (1621: 43) -webkit-transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -170deg);
                    (1622: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -170deg);
                    (1651: 43) -webkit-transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -190deg);
                    (1652: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -190deg);
                    (1658: 43) -webkit-transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -170deg);
                    (1659: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -170deg);
                    (1924: 24) -webkit-transform: translate3d(100%, 0, 0) skewX(-30deg);
                    (1925: 16) transform: translate3d(100%, 0, 0) skewX(-30deg);
                    (1950: 24) -webkit-transform: translate3d(100%, 0, 0) skewX(-30deg);
                    (1951: 16) transform: translate3d(100%, 0, 0) skewX(-30deg);
                    (1987: 24) -webkit-transform: translate3d(100%, 0, 0) skewX(30deg);
                    (1988: 16) transform: translate3d(100%, 0, 0) skewX(30deg);
                    (1999: 24) -webkit-transform: translate3d(100%, 0, 0) skewX(30deg);
                    (2000: 16) transform: translate3d(100%, 0, 0) skewX(30deg);
                    (2430: 24) -webkit-transform: translate3d(0, 700px, 0);
                    (2431: 16) transform: translate3d(0, 700px, 0);
                    (2464: 24) -webkit-transform: translate3d(0, 700px, 0);
                    (2465: 16) transform: translate3d(0, 700px, 0);
                    (2480: 24) -webkit-transform: translate3d(-100%, 0, 0) rotate3d(0, 0, 1, -120deg);
                    (2481: 16) transform: translate3d(-100%, 0, 0) rotate3d(0, 0, 1, -120deg);
                    (2494: 24) -webkit-transform: translate3d(-100%, 0, 0) rotate3d(0, 0, 1, -120deg);
                    (2495: 16) transform: translate3d(-100%, 0, 0) rotate3d(0, 0, 1, -120deg);
                    (2519: 24) -webkit-transform: translate3d(100%, 0, 0) rotate3d(0, 0, 1, 120deg);
                    (2520: 16) transform: translate3d(100%, 0, 0) rotate3d(0, 0, 1, 120deg);
                    (2531: 24) -webkit-transform: translate3d(100%, 0, 0) rotate3d(0, 0, 1, 120deg);
                    (2532: 16) transform: translate3d(100%, 0, 0) rotate3d(0, 0, 1, 120deg);
                    (2573: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
                    (2574: 36) transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
                    (2581: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2582: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2591: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
                    (2592: 36) transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
                    (2599: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2600: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2614: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(-1000px, 0, 0);
                    (2615: 36) transform: scale3d(.1, .1, .1) translate3d(-1000px, 0, 0);
                    (2622: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(10px, 0, 0);
                    (2623: 42) transform: scale3d(.475, .475, .475) translate3d(10px, 0, 0);
                    (2632: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(-1000px, 0, 0);
                    (2633: 36) transform: scale3d(.1, .1, .1) translate3d(-1000px, 0, 0);
                    (2640: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(10px, 0, 0);
                    (2641: 42) transform: scale3d(.475, .475, .475) translate3d(10px, 0, 0);
                    (2655: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(1000px, 0, 0);
                    (2656: 36) transform: scale3d(.1, .1, .1) translate3d(1000px, 0, 0);
                    (2663: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(-10px, 0, 0);
                    (2664: 42) transform: scale3d(.475, .475, .475) translate3d(-10px, 0, 0);
                    (2673: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(1000px, 0, 0);
                    (2674: 36) transform: scale3d(.1, .1, .1) translate3d(1000px, 0, 0);
                    (2681: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(-10px, 0, 0);
                    (2682: 42) transform: scale3d(.475, .475, .475) translate3d(-10px, 0, 0);
                    (2696: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, 1000px, 0);
                    (2697: 36) transform: scale3d(.1, .1, .1) translate3d(0, 1000px, 0);
                    (2704: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2705: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2714: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, 1000px, 0);
                    (2715: 36) transform: scale3d(.1, .1, .1) translate3d(0, 1000px, 0);
                    (2722: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2723: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2774: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2775: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2782: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, 2000px, 0);
                    (2783: 36) transform: scale3d(.1, .1, .1) translate3d(0, 2000px, 0);
                    (2794: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2795: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (2802: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, 2000px, 0);
                    (2803: 36) transform: scale3d(.1, .1, .1) translate3d(0, 2000px, 0);
                    (2819: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(42px, 0, 0);
                    (2820: 42) transform: scale3d(.475, .475, .475) translate3d(42px, 0, 0);
                    (2825: 34) -webkit-transform: scale(.1) translate3d(-2000px, 0, 0);
                    (2826: 26) transform: scale(.1) translate3d(-2000px, 0, 0);
                    (2835: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(42px, 0, 0);
                    (2836: 42) transform: scale3d(.475, .475, .475) translate3d(42px, 0, 0);
                    (2841: 34) -webkit-transform: scale(.1) translate3d(-2000px, 0, 0);
                    (2842: 26) transform: scale(.1) translate3d(-2000px, 0, 0);
                    (2856: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(-42px, 0, 0);
                    (2857: 42) transform: scale3d(.475, .475, .475) translate3d(-42px, 0, 0);
                    (2862: 34) -webkit-transform: scale(.1) translate3d(2000px, 0, 0);
                    (2863: 26) transform: scale(.1) translate3d(2000px, 0, 0);
                    (2872: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(-42px, 0, 0);
                    (2873: 42) transform: scale3d(.475, .475, .475) translate3d(-42px, 0, 0);
                    (2878: 34) -webkit-transform: scale(.1) translate3d(2000px, 0, 0);
                    (2879: 26) transform: scale(.1) translate3d(2000px, 0, 0);
                    (2893: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2894: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2901: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -2000px, 0);
                    (2902: 36) transform: scale3d(.1, .1, .1) translate3d(0, -2000px, 0);
                    (2913: 50) -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2914: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (2921: 44) -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -2000px, 0);
                    (2922: 36) transform: scale3d(.1, .1, .1) translate3d(0, -2000px, 0);
                    (2937: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (2938: 16) transform: translate3d(0, -100%, 0);
                    (2943: 24) -webkit-transform: translate3d(0, 0, 0);
                    (2944: 16) transform: translate3d(0, 0, 0);
                    (2950: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (2951: 16) transform: translate3d(0, -100%, 0);
                    (2956: 24) -webkit-transform: translate3d(0, 0, 0);
                    (2957: 16) transform: translate3d(0, 0, 0);
                    (2968: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (2969: 16) transform: translate3d(-100%, 0, 0);
                    (2974: 24) -webkit-transform: translate3d(0, 0, 0);
                    (2975: 16) transform: translate3d(0, 0, 0);
                    (2981: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (2982: 16) transform: translate3d(-100%, 0, 0);
                    (2987: 24) -webkit-transform: translate3d(0, 0, 0);
                    (2988: 16) transform: translate3d(0, 0, 0);
                    (2999: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (3000: 16) transform: translate3d(100%, 0, 0);
                    (3005: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3006: 16) transform: translate3d(0, 0, 0);
                    (3012: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (3013: 16) transform: translate3d(100%, 0, 0);
                    (3018: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3019: 16) transform: translate3d(0, 0, 0);
                    (3030: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (3031: 16) transform: translate3d(0, 100%, 0);
                    (3036: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3037: 16) transform: translate3d(0, 0, 0);
                    (3043: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (3044: 16) transform: translate3d(0, 100%, 0);
                    (3049: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3050: 16) transform: translate3d(0, 0, 0);
                    (3061: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3062: 16) transform: translate3d(0, 0, 0);
                    (3067: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (3068: 16) transform: translate3d(0, 100%, 0);
                    (3074: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3075: 16) transform: translate3d(0, 0, 0);
                    (3080: 24) -webkit-transform: translate3d(0, 100%, 0);
                    (3081: 16) transform: translate3d(0, 100%, 0);
                    (3092: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3093: 16) transform: translate3d(0, 0, 0);
                    (3098: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (3099: 16) transform: translate3d(-100%, 0, 0);
                    (3105: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3106: 16) transform: translate3d(0, 0, 0);
                    (3111: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (3112: 16) transform: translate3d(-100%, 0, 0);
                    (3123: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3124: 16) transform: translate3d(0, 0, 0);
                    (3129: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (3130: 16) transform: translate3d(100%, 0, 0);
                    (3136: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3137: 16) transform: translate3d(0, 0, 0);
                    (3142: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (3143: 16) transform: translate3d(100%, 0, 0);
                    (3154: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3155: 16) transform: translate3d(0, 0, 0);
                    (3160: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (3161: 16) transform: translate3d(0, -100%, 0);
                    (3167: 24) -webkit-transform: translate3d(0, 0, 0);
                    (3168: 16) transform: translate3d(0, 0, 0);
                    (3173: 24) -webkit-transform: translate3d(0, -100%, 0);
                    (3174: 16) transform: translate3d(0, -100%, 0);
                animate.min.css  (376 usages found)
                    (6: 609) translate
                    (6: 638) translate
                    (6: 815) translate
                    (6: 848) translate
                    (6: 1025) translate
                    (6: 1058) translate
                    (6: 1103) translate
                    (6: 1135) translate
                    (6: 1338) translate
                    (6: 1367) translate
                    (6: 1544) translate
                    (6: 1577) translate
                    (6: 1754) translate
                    (6: 1787) translate
                    (6: 1832) translate
                    (6: 1864) translate
                    (6: 3856) translate
                    (6: 3885) translate
                    (6: 3942) translate
                    (6: 3975) translate
                    (6: 4032) translate
                    (6: 4064) translate
                    (6: 4130) translate
                    (6: 4159) translate
                    (6: 4216) translate
                    (6: 4249) translate
                    (6: 4306) translate
                    (6: 4338) translate
                    (6: 6514) translate
                    (6: 6568) translate
                    (6: 6634) translate
                    (6: 6686) translate
                    (6: 6750) translate
                    (6: 6804) translate
                    (6: 6870) translate
                    (6: 6922) translate
                    (6: 6986) translate
                    (6: 7039) translate
                    (6: 7207) translate
                    (6: 7261) translate
                    (6: 7327) translate
                    (6: 7379) translate
                    (6: 7443) translate
                    (6: 7497) translate
                    (6: 7563) translate
                    (6: 7615) translate
                    (6: 7679) translate
                    (6: 7732) translate
                    (6: 9410) translate
                    (6: 9445) translate
                    (6: 9502) translate
                    (6: 9534) translate
                    (6: 9578) translate
                    (6: 9611) translate
                    (6: 9656) translate
                    (6: 9687) translate
                    (6: 9951) translate
                    (6: 9986) translate
                    (6: 10043) translate
                    (6: 10075) translate
                    (6: 10119) translate
                    (6: 10152) translate
                    (6: 10197) translate
                    (6: 10228) translate
                    (6: 10578) translate
                    (6: 10613) translate
                    (6: 10670) translate
                    (6: 10702) translate
                    (6: 10746) translate
                    (6: 10779) translate
                    (6: 10824) translate
                    (6: 10855) translate
                    (6: 11119) translate
                    (6: 11154) translate
                    (6: 11211) translate
                    (6: 11243) translate
                    (6: 11287) translate
                    (6: 11320) translate
                    (6: 11365) translate
                    (6: 11396) translate
                    (6: 11747) translate
                    (6: 11781) translate
                    (6: 11837) translate
                    (6: 11870) translate
                    (6: 11915) translate
                    (6: 11947) translate
                    (6: 11991) translate
                    (6: 12023) translate
                    (6: 12289) translate
                    (6: 12323) translate
                    (6: 12379) translate
                    (6: 12412) translate
                    (6: 12457) translate
                    (6: 12489) translate
                    (6: 12533) translate
                    (6: 12565) translate
                    (6: 12917) translate
                    (6: 12951) translate
                    (6: 13007) translate
                    (6: 13040) translate
                    (6: 13085) translate
                    (6: 13117) translate
                    (6: 13161) translate
                    (6: 13193) translate
                    (6: 13238) translate
                    (6: 13267) translate
                    (6: 13484) translate
                    (6: 13518) translate
                    (6: 13574) translate
                    (6: 13607) translate
                    (6: 13652) translate
                    (6: 13684) translate
                    (6: 13728) translate
                    (6: 13760) translate
                    (6: 13805) translate
                    (6: 13834) translate
                    (6: 14572) translate
                    (6: 14604) translate
                    (6: 14662) translate
                    (6: 14695) translate
                    (6: 14751) translate
                    (6: 14785) translate
                    (6: 14857) translate
                    (6: 14889) translate
                    (6: 14947) translate
                    (6: 14980) translate
                    (6: 15036) translate
                    (6: 15070) translate
                    (6: 15241) translate
                    (6: 15273) translate
                    (6: 15328) translate
                    (6: 15363) translate
                    (6: 15446) translate
                    (6: 15478) translate
                    (6: 15533) translate
                    (6: 15568) translate
                    (6: 15741) translate
                    (6: 15774) translate
                    (6: 15830) translate
                    (6: 15864) translate
                    (6: 15947) translate
                    (6: 15980) translate
                    (6: 16036) translate
                    (6: 16070) translate
                    (6: 16232) translate
                    (6: 16265) translate
                    (6: 16324) translate
                    (6: 16356) translate
                    (6: 16411) translate
                    (6: 16446) translate
                    (6: 16517) translate
                    (6: 16550) translate
                    (6: 16609) translate
                    (6: 16641) translate
                    (6: 16696) translate
                    (6: 16731) translate
                    (6: 17055) translate
                    (6: 17088) translate
                    (6: 17218) translate
                    (6: 17251) translate
                    (6: 17464) translate
                    (6: 17499) translate
                    (6: 17634) translate
                    (6: 17669) translate
                    (6: 17890) translate
                    (6: 17923) translate
                    (6: 18053) translate
                    (6: 18086) translate
                    (6: 18299) translate
                    (6: 18334) translate
                    (6: 18469) translate
                    (6: 18504) translate
                    (6: 18726) translate
                    (6: 18758) translate
                    (6: 18888) translate
                    (6: 18920) translate
                    (6: 19136) translate
                    (6: 19170) translate
                    (6: 19305) translate
                    (6: 19339) translate
                    (6: 19560) translate
                    (6: 19592) translate
                    (6: 19719) translate
                    (6: 19751) translate
                    (6: 19955) translate
                    (6: 19989) translate
                    (6: 20121) translate
                    (6: 20155) translate
                    (6: 20552) translate
                    (6: 20584) translate
                    (6: 20676) translate
                    (6: 20708) translate
                    (6: 20886) translate
                    (6: 20920) translate
                    (6: 21017) translate
                    (6: 21051) translate
                    (6: 21237) translate
                    (6: 21270) translate
                    (6: 21363) translate
                    (6: 21396) translate
                    (6: 21575) translate
                    (6: 21610) translate
                    (6: 21708) translate
                    (6: 21743) translate
                    (6: 21931) translate
                    (6: 21963) translate
                    (6: 22056) translate
                    (6: 22088) translate
                    (6: 22270) translate
                    (6: 22304) translate
                    (6: 22402) translate
                    (6: 22436) translate
                    (6: 22623) translate
                    (6: 22656) translate
                    (6: 22747) translate
                    (6: 22780) translate
                    (6: 22951) translate
                    (6: 22986) translate
                    (6: 23082) translate
                    (6: 23117) translate
                    (6: 23481) translate
                    (6: 23557) translate
                    (6: 23723) translate
                    (6: 23799) translate
                    (6: 24510) translate
                    (6: 24586) translate
                    (6: 24752) translate
                    (6: 24828) translate
                    (6: 30353) translate
                    (6: 30399) translate
                    (6: 30680) translate
                    (6: 30726) translate
                    (6: 31187) translate
                    (6: 31232) translate
                    (6: 31339) translate
                    (6: 31384) translate
                    (6: 38725) translate
                    (6: 38758) translate
                    (6: 39437) translate
                    (6: 39470) translate
                    (6: 39618) translate
                    (6: 39675) translate
                    (6: 39825) translate
                    (6: 39882) translate
                    (6: 40116) translate
                    (6: 40171) translate
                    (6: 40282) translate
                    (6: 40337) translate
                    (6: 40813) translate
                    (6: 40866) translate
                    (6: 41073) translate
                    (6: 41129) translate
                    (6: 41345) translate
                    (6: 41398) translate
                    (6: 41605) translate
                    (6: 41661) translate
                    (6: 41957) translate
                    (6: 42010) translate
                    (6: 42217) translate
                    (6: 42273) translate
                    (6: 42489) translate
                    (6: 42542) translate
                    (6: 42749) translate
                    (6: 42805) translate
                    (6: 43102) translate
                    (6: 43154) translate
                    (6: 43360) translate
                    (6: 43417) translate
                    (6: 43635) translate
                    (6: 43687) translate
                    (6: 43893) translate
                    (6: 43950) translate
                    (6: 44248) translate
                    (6: 44300) translate
                    (6: 44506) translate
                    (6: 44563) translate
                    (6: 44778) translate
                    (6: 44830) translate
                    (6: 45036) translate
                    (6: 45093) translate
                    (6: 45715) translate
                    (6: 45772) translate
                    (6: 45972) translate
                    (6: 46024) translate
                    (6: 46320) translate
                    (6: 46377) translate
                    (6: 46577) translate
                    (6: 46629) translate
                    (6: 47008) translate
                    (6: 47064) translate
                    (6: 47129) translate
                    (6: 47174) translate
                    (6: 47345) translate
                    (6: 47401) translate
                    (6: 47466) translate
                    (6: 47511) translate
                    (6: 47766) translate
                    (6: 47823) translate
                    (6: 47889) translate
                    (6: 47933) translate
                    (6: 48106) translate
                    (6: 48163) translate
                    (6: 48229) translate
                    (6: 48273) translate
                    (6: 48529) translate
                    (6: 48585) translate
                    (6: 48784) translate
                    (6: 48837) translate
                    (6: 49132) translate
                    (6: 49188) translate
                    (6: 49387) translate
                    (6: 49440) translate
                    (6: 49779) translate
                    (6: 49812) translate
                    (6: 49877) translate
                    (6: 49906) translate
                    (6: 49970) translate
                    (6: 50003) translate
                    (6: 50068) translate
                    (6: 50097) translate
                    (6: 50244) translate
                    (6: 50277) translate
                    (6: 50342) translate
                    (6: 50371) translate
                    (6: 50435) translate
                    (6: 50468) translate
                    (6: 50533) translate
                    (6: 50562) translate
                    (6: 50710) translate
                    (6: 50742) translate
                    (6: 50806) translate
                    (6: 50835) translate
                    (6: 50900) translate
                    (6: 50932) translate
                    (6: 50996) translate
                    (6: 51025) translate
                    (6: 51173) translate
                    (6: 51205) translate
                    (6: 51269) translate
                    (6: 51298) translate
                    (6: 51360) translate
                    (6: 51392) translate
                    (6: 51456) translate
                    (6: 51485) translate
                    (6: 51627) translate
                    (6: 51656) translate
                    (6: 51716) translate
                    (6: 51748) translate
                    (6: 51816) translate
                    (6: 51845) translate
                    (6: 51905) translate
                    (6: 51937) translate
                    (6: 52091) translate
                    (6: 52120) translate
                    (6: 52180) translate
                    (6: 52213) translate
                    (6: 52282) translate
                    (6: 52311) translate
                    (6: 52371) translate
                    (6: 52404) translate
                    (6: 52560) translate
                    (6: 52589) translate
                    (6: 52649) translate
                    (6: 52681) translate
                    (6: 52750) translate
                    (6: 52779) translate
                    (6: 52839) translate
                    (6: 52871) translate
                    (6: 53026) translate
                    (6: 53055) translate
                    (6: 53115) translate
                    (6: 53148) translate
                    (6: 53215) translate
                    (6: 53244) translate
                    (6: 53304) translate
                    (6: 53337) translate
            amspApp/static/bower_components/animate.css/source/attention_seekers  (12 usages found)
                bounce.css  (4 usages found)
                    (4: 16) transform: translate3d(0,0,0);
                    (9: 16) transform: translate3d(0, -30px, 0);
                    (14: 16) transform: translate3d(0, -15px, 0);
                    (18: 16) transform: translate3d(0,-4px,0);
                shake.css  (3 usages found)
                    (3: 16) transform: translate3d(0, 0, 0);
                    (7: 16) transform: translate3d(-10px, 0, 0);
                    (11: 16) transform: translate3d(10px, 0, 0);
                wobble.css  (5 usages found)
                    (9: 16) transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
                    (13: 16) transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
                    (17: 16) transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
                    (21: 16) transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
                    (25: 16) transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
            amspApp/static/bower_components/animate.css/source/bouncing_entrances  (17 usages found)
                bounceInDown.css  (4 usages found)
                    (8: 16) transform: translate3d(0, -3000px, 0);
                    (13: 16) transform: translate3d(0, 25px, 0);
                    (17: 16) transform: translate3d(0, -10px, 0);
                    (21: 16) transform: translate3d(0, 5px, 0);
                bounceInLeft.css  (4 usages found)
                    (8: 16) transform: translate3d(-3000px, 0, 0);
                    (13: 16) transform: translate3d(25px, 0, 0);
                    (17: 16) transform: translate3d(-10px, 0, 0);
                    (21: 16) transform: translate3d(5px, 0, 0);
                bounceInRight.css  (4 usages found)
                    (8: 16) transform: translate3d(3000px, 0, 0);
                    (13: 16) transform: translate3d(-25px, 0, 0);
                    (17: 16) transform: translate3d(10px, 0, 0);
                    (21: 16) transform: translate3d(-5px, 0, 0);
                bounceInUp.css  (5 usages found)
                    (8: 16) transform: translate3d(0, 3000px, 0);
                    (13: 16) transform: translate3d(0, -20px, 0);
                    (17: 16) transform: translate3d(0, 10px, 0);
                    (21: 16) transform: translate3d(0, -5px, 0);
                    (25: 16) transform: translate3d(0, 0, 0);
            amspApp/static/bower_components/animate.css/source/bouncing_exits  (10 usages found)
                bounceOutDown.css  (3 usages found)
                    (3: 16) transform: translate3d(0, 10px, 0);
                    (8: 16) transform: translate3d(0, -20px, 0);
                    (13: 16) transform: translate3d(0, 2000px, 0);
                bounceOutLeft.css  (2 usages found)
                    (4: 16) transform: translate3d(20px, 0, 0);
                    (9: 16) transform: translate3d(-2000px, 0, 0);
                bounceOutRight.css  (2 usages found)
                    (4: 16) transform: translate3d(-20px, 0, 0);
                    (9: 16) transform: translate3d(2000px, 0, 0);
                bounceOutUp.css  (3 usages found)
                    (3: 16) transform: translate3d(0, -10px, 0);
                    (8: 16) transform: translate3d(0, 20px, 0);
                    (13: 16) transform: translate3d(0, -2000px, 0);
            amspApp/static/bower_components/animate.css/source/fading_entrances  (8 usages found)
                fadeInDown.css  (1 usage found)
                    (4: 16) transform: translate3d(0, -100%, 0);
                fadeInDownBig.css  (1 usage found)
                    (4: 16) transform: translate3d(0, -2000px, 0);
                fadeInLeft.css  (1 usage found)
                    (4: 16) transform: translate3d(-100%, 0, 0);
                fadeInLeftBig.css  (1 usage found)
                    (4: 16) transform: translate3d(-2000px, 0, 0);
                fadeInRight.css  (1 usage found)
                    (4: 16) transform: translate3d(100%, 0, 0);
                fadeInRightBig.css  (1 usage found)
                    (4: 16) transform: translate3d(2000px, 0, 0);
                fadeInUp.css  (1 usage found)
                    (4: 16) transform: translate3d(0, 100%, 0);
                fadeInUpBig.css  (1 usage found)
                    (4: 16) transform: translate3d(0, 2000px, 0);
            amspApp/static/bower_components/animate.css/source/fading_exits  (8 usages found)
                fadeOutDown.css  (1 usage found)
                    (8: 16) transform: translate3d(0, 100%, 0);
                fadeOutDownBig.css  (1 usage found)
                    (8: 16) transform: translate3d(0, 2000px, 0);
                fadeOutLeft.css  (1 usage found)
                    (8: 16) transform: translate3d(-100%, 0, 0);
                fadeOutLeftBig.css  (1 usage found)
                    (8: 16) transform: translate3d(-2000px, 0, 0);
                fadeOutRight.css  (1 usage found)
                    (8: 16) transform: translate3d(100%, 0, 0);
                fadeOutRightBig.css  (1 usage found)
                    (8: 16) transform: translate3d(2000px, 0, 0);
                fadeOutUp.css  (1 usage found)
                    (8: 16) transform: translate3d(0, -100%, 0);
                fadeOutUpBig.css  (1 usage found)
                    (8: 16) transform: translate3d(0, -2000px, 0);
            amspApp/static/bower_components/animate.css/source/flippers  (2 usages found)
                flip.css  (2 usages found)
                    (8: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -190deg);
                    (13: 35) transform: perspective(400px) translate3d(0, 0, 150px) rotate3d(0, 1, 0, -170deg);
            amspApp/static/bower_components/animate.css/source/lightspeed  (2 usages found)
                lightSpeedIn.css  (1 usage found)
                    (3: 16) transform: translate3d(100%, 0, 0) skewX(-30deg);
                lightSpeedOut.css  (1 usage found)
                    (7: 16) transform: translate3d(100%, 0, 0) skewX(30deg);
            amspApp/static/bower_components/animate.css/source/sliding_entrances  (8 usages found)
                slideInDown.css  (2 usages found)
                    (3: 16) transform: translate3d(0, -100%, 0);
                    (8: 16) transform: translate3d(0, 0, 0);
                slideInLeft.css  (2 usages found)
                    (3: 16) transform: translate3d(-100%, 0, 0);
                    (8: 16) transform: translate3d(0, 0, 0);
                slideInRight.css  (2 usages found)
                    (3: 16) transform: translate3d(100%, 0, 0);
                    (8: 16) transform: translate3d(0, 0, 0);
                slideInUp.css  (2 usages found)
                    (3: 16) transform: translate3d(0, 100%, 0);
                    (8: 16) transform: translate3d(0, 0, 0);
            amspApp/static/bower_components/animate.css/source/sliding_exits  (8 usages found)
                slideOutDown.css  (2 usages found)
                    (3: 16) transform: translate3d(0, 0, 0);
                    (8: 16) transform: translate3d(0, 100%, 0);
                slideOutLeft.css  (2 usages found)
                    (3: 16) transform: translate3d(0, 0, 0);
                    (8: 16) transform: translate3d(-100%, 0, 0);
                slideOutRight.css  (2 usages found)
                    (3: 16) transform: translate3d(0, 0, 0);
                    (8: 16) transform: translate3d(100%, 0, 0);
                slideOutUp.css  (2 usages found)
                    (3: 16) transform: translate3d(0, 0, 0);
                    (8: 16) transform: translate3d(0, -100%, 0);
            amspApp/static/bower_components/animate.css/source/specials  (3 usages found)
                hinge.css  (1 usage found)
                    (21: 16) transform: translate3d(0, 700px, 0);
                rollIn.css  (1 usage found)
                    (6: 16) transform: translate3d(-100%, 0, 0) rotate3d(0, 0, 1, -120deg);
                rollOut.css  (1 usage found)
                    (10: 16) transform: translate3d(100%, 0, 0) rotate3d(0, 0, 1, 120deg);
            amspApp/static/bower_components/animate.css/source/zooming_entrances  (8 usages found)
                zoomInDown.css  (2 usages found)
                    (4: 36) transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
                    (10: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                zoomInLeft.css  (2 usages found)
                    (4: 36) transform: scale3d(.1, .1, .1) translate3d(-1000px, 0, 0);
                    (10: 42) transform: scale3d(.475, .475, .475) translate3d(10px, 0, 0);
                zoomInRight.css  (2 usages found)
                    (4: 36) transform: scale3d(.1, .1, .1) translate3d(1000px, 0, 0);
                    (10: 42) transform: scale3d(.475, .475, .475) translate3d(-10px, 0, 0);
                zoomInUp.css  (2 usages found)
                    (4: 36) transform: scale3d(.1, .1, .1) translate3d(0, 1000px, 0);
                    (10: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
            amspApp/static/bower_components/animate.css/source/zooming_exits  (8 usages found)
                zoomOutDown.css  (2 usages found)
                    (4: 42) transform: scale3d(.475, .475, .475) translate3d(0, -60px, 0);
                    (10: 36) transform: scale3d(.1, .1, .1) translate3d(0, 2000px, 0);
                zoomOutLeft.css  (2 usages found)
                    (4: 42) transform: scale3d(.475, .475, .475) translate3d(42px, 0, 0);
                    (9: 26) transform: scale(.1) translate3d(-2000px, 0, 0);
                zoomOutRight.css  (2 usages found)
                    (4: 42) transform: scale3d(.475, .475, .475) translate3d(-42px, 0, 0);
                    (9: 26) transform: scale(.1) translate3d(2000px, 0, 0);
                zoomOutUp.css  (2 usages found)
                    (4: 42) transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
                    (10: 36) transform: scale3d(.1, .1, .1) translate3d(0, -2000px, 0);
            amspApp/static/bower_components/bootstrap-css-only/css  (28 usages found)
                bootstrap.css  (14 usages found)
                    (5738: 22) -webkit-transform: translate(0, -25%);
                    (5739: 22) -ms-transform: translate(0, -25%);
                    (5740: 22) -o-transform: translate(0, -25%);
                    (5741: 22) transform: translate(0, -25%);
                    (5744: 22) -webkit-transform: translate(0, 0);
                    (5745: 22) -ms-transform: translate(0, 0);
                    (5746: 22) -o-transform: translate(0, 0);
                    (5747: 22) transform: translate(0, 0);
                    (6101: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (6102: 24) transform: translate3d(100%, 0, 0);
                    (6107: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (6108: 24) transform: translate3d(-100%, 0, 0);
                    (6114: 24) -webkit-transform: translate3d(0, 0, 0);
                    (6115: 24) transform: translate3d(0, 0, 0);
                bootstrap.min.css  (14 usages found)
                    (5: 102923) translate
                    (5: 102955) translate
                    (5: 102986) translate
                    (5: 103014) translate
                    (5: 103074) translate
                    (5: 103103) translate
                    (5: 103131) translate
                    (5: 103156) translate
                    (5: 108778) translate
                    (5: 108810) translate
                    (5: 108918) translate
                    (5: 108951) translate
                    (5: 109093) translate
                    (5: 109122) translate
            amspApp/static/bower_components/bootstrap/dist/css  (28 usages found)
                bootstrap.css  (14 usages found)
                    (5931: 22) -webkit-transform: translate(0, -25%);
                    (5932: 22) -ms-transform: translate(0, -25%);
                    (5933: 22) -o-transform: translate(0, -25%);
                    (5934: 22) transform: translate(0, -25%);
                    (5937: 22) -webkit-transform: translate(0, 0);
                    (5938: 22) -ms-transform: translate(0, 0);
                    (5939: 22) -o-transform: translate(0, 0);
                    (5940: 22) transform: translate(0, 0);
                    (6317: 24) -webkit-transform: translate3d(100%, 0, 0);
                    (6318: 24) transform: translate3d(100%, 0, 0);
                    (6323: 24) -webkit-transform: translate3d(-100%, 0, 0);
                    (6324: 24) transform: translate3d(-100%, 0, 0);
                    (6330: 24) -webkit-transform: translate3d(0, 0, 0);
                    (6331: 24) transform: translate3d(0, 0, 0);
                bootstrap.min.css  (14 usages found)
                    (5: 107702) translate
                    (5: 107734) translate
                    (5: 107765) translate
                    (5: 107793) translate
                    (5: 107853) translate
                    (5: 107882) translate
                    (5: 107910) translate
                    (5: 107935) translate
                    (5: 113954) translate
                    (5: 113986) translate
                    (5: 114094) translate
                    (5: 114127) translate
                    (5: 114269) translate
                    (5: 114298) translate
            amspApp/static/bower_components/bootstrap/less  (5 usages found)
                carousel.less  (3 usages found)
                    (36: 10) .translate3d(100%, 0, 0);
                    (41: 10) .translate3d(-100%, 0, 0);
                    (47: 10) .translate3d(0, 0, 0);
                modals.less  (2 usages found)
                    (33: 6) .translate(0, -25%);
                    (36: 25) &.in .modal-dialog { .translate(0, 0) }
            amspApp/static/bower_components/bootstrap/less/mixins  (8 usages found)
                vendor-prefixes.less  (8 usages found)
                    (142: 2) .translate(@x; @y) {
                    (143: 22) -webkit-transform: translate(@x, @y);
                    (144: 22) -ms-transform: translate(@x, @y); // IE9 only
                    (145: 22) -o-transform: translate(@x, @y);
                    (146: 22) transform: translate(@x, @y);
                    (148: 2) .translate3d(@x; @y; @z) {
                    (149: 22) -webkit-transform: translate3d(@x, @y, @z);
                    (150: 22) transform: translate3d(@x, @y, @z);
            amspApp/static/bower_components/bpmn-modeler  (45 usages found)
                BpmnViewer.js  (12 usages found)
                    (11428: 45) matrix = new Snap.Matrix().scale(scale).translate(-box.x, -box.y);
                    (11454: 47) matrix = this._svg.node.createSVGMatrix().translate(delta.dx, delta.dy).multiply(matrix);
                    (11580: 22) .translate(originalPoint.x, originalPoint.y)
                    (11582: 22) .translate(-originalPoint.x, -originalPoint.y);
                    (12434: 9) gfx.translate(element.x, element.y);
                    (16445: 19) m.translate(t[1], 0);
                    (16452: 23) m.translate(x2 - x1, y2 - y1);
                    (16454: 23) m.translate(t[1], t[2]);
                    (17228: 54) m = m.add(el.transform().localMatrix.translate(el.attr("x") || 0, el.attr("y") || 0));
                    (18267: 21) matrixproto.translate = function (x, y) {
                    (21968: 21) Element.prototype.translate = function(x, y) {
                    (21970: 12) matrix.translate(x, y);
                BpmnViewerApp.js  (12 usages found)
                    (11425: 45) matrix = new Snap.Matrix().scale(scale).translate(-box.x, -box.y);
                    (11451: 47) matrix = this._svg.node.createSVGMatrix().translate(delta.dx, delta.dy).multiply(matrix);
                    (11577: 22) .translate(originalPoint.x, originalPoint.y)
                    (11579: 22) .translate(-originalPoint.x, -originalPoint.y);
                    (12431: 9) gfx.translate(element.x, element.y);
                    (16777: 19) m.translate(t[1], 0);
                    (16784: 23) m.translate(x2 - x1, y2 - y1);
                    (16786: 23) m.translate(t[1], t[2]);
                    (17560: 54) m = m.add(el.transform().localMatrix.translate(el.attr("x") || 0, el.attr("y") || 0));
                    (18599: 21) matrixproto.translate = function (x, y) {
                    (22300: 21) Element.prototype.translate = function(x, y) {
                    (22302: 12) matrix.translate(x, y);
                index.js  (21 usages found)
                    (16885: 57) matrix = new Snap.Matrix().scale(scale).translate(-box.x, -box.y);
                    (16911: 59) matrix = this._svg.node.createSVGMatrix().translate(delta.dx, delta.dy).multiply(matrix);
                    (17034: 22) .translate(originalPoint.x, originalPoint.y)
                    (17036: 22) .translate(-originalPoint.x, -originalPoint.y);
                    (17895: 21) gfx.translate(element.x, element.y);
                    (18289: 36) context.draggerGfx.translate(e.x, e.y);
                    (18502: 44) Util.addBendpoint(gfx).translate(p.x, p.y);
                    (18580: 34) floating.translate(intersection.point.x, intersection.point.y);
                    (19373: 25) preview.translate(shape.width / -2, shape.height / -2);
                    (19398: 24) visual.translate(event.x, event.y);
                    (22612: 27) dragGroup.translate(event.dx, event.dy);
                    (24079: 48) var matrix = new Snap.Matrix().translate(x, y).rotate(rotation, 0, 0);
                    (25406: 32) crosshairGroup.translate(event.x, event.y);
                    (25466: 35) context.dragGroup.translate(delta.x, delta.y);
                    (33375: 35) m.translate(t[1], 0);
                    (33382: 39) m.translate(x2 - x1, y2 - y1);
                    (33384: 39) m.translate(t[1], t[2]);
                    (34173: 66) m = m.add(el.transform().localMatrix.translate(el.attr("x") || 0, el.attr("y") || 0));
                    (35222: 33) matrixproto.translate = function (x, y) {
                    (38978: 31) Element.prototype.translate = function (x, y) {
                    (38980: 24) matrix.translate(x, y);
            amspApp/static/bower_components/bpmn-modeler/vendor  (12 usages found)
                disttt2.js  (12 usages found)
                    (11432: 45) matrix = new Snap.Matrix().scale(scale).translate(-box.x, -box.y);
                    (11458: 47) matrix = this._svg.node.createSVGMatrix().translate(delta.dx, delta.dy).multiply(matrix);
                    (11584: 22) .translate(originalPoint.x, originalPoint.y)
                    (11586: 22) .translate(-originalPoint.x, -originalPoint.y);
                    (12438: 9) gfx.translate(element.x, element.y);
                    (16784: 19) m.translate(t[1], 0);
                    (16791: 23) m.translate(x2 - x1, y2 - y1);
                    (16793: 23) m.translate(t[1], t[2]);
                    (17567: 54) m = m.add(el.transform().localMatrix.translate(el.attr("x") || 0, el.attr("y") || 0));
                    (18606: 21) matrixproto.translate = function (x, y) {
                    (22307: 21) Element.prototype.translate = function(x, y) {
                    (22309: 12) matrix.translate(x, y);
            amspApp/static/bower_components/c3  (45 usages found)
                c3.js  (28 usages found)
                    (261: 69) main = $$.main = $$.svg.append("g").attr("transform", $$.getTranslate('main'));
                    (758: 29) c3_chart_internal_fn.getTranslate = function (target) {
                    (843: 83) (withTransition ? $$.main.transition() : $$.main).attr("transform", $$.getTranslate('main'));
                    (844: 39) xAxis.attr("transform", $$.getTranslate('x'));
                    (845: 39) yAxis.attr("transform", $$.getTranslate('y'));
                    (846: 40) y2Axis.attr("transform", $$.getTranslate('y2'));
                    (847: 71) $$.main.select('.' + CLASS.chartArcs).attr("transform", $$.getTranslate('arc'));
                    (3829: 64) $$.legend = $$.svg.append("g").attr("transform", $$.getTranslate('legend'));
                    (3858: 87) (withTransition ? $$.legend.transition() : $$.legend).attr("transform", $$.getTranslate('legend'));
                    (4160: 38) .attr("transform", $$.getTranslate('x'))
                    (4169: 38) .attr("transform", $$.getTranslate('y'))
                    (4179: 38) .attr("transform", $$.getTranslate('y2'))
                    (4674: 61) updated = $$.updateAngle(d), c, x, y, h, ratio, translate = "";
                    (4682: 13) translate = "translate(" + (x * ratio) +  ',' + (y * ratio) +  ")";
                    (4684: 16) return translate;
                    (4826: 38) .attr("transform", $$.getTranslate('arc'));
                    (5239: 79) context = $$.context = $$.svg.append("g").attr("transform", $$.getTranslate('context'));
                    (5266: 38) .attr("transform", $$.getTranslate('subx'))
                    (5419: 44) $$.context.attr("transform", $$.getTranslate('context'));
                    (5420: 42) subXAxis.attr("transform", $$.getTranslate('subx'));
                    (6182: 17) var translateX, scaleX = 1, transform,
                    (6217: 21) translateX = $$.x(orgDomain[0]) - $$.x(domain[0]);
                    (6222: 25) translateX = $$.x(flowStart.x) - $$.x(flowEnd.x);
                    (6224: 25) translateX = diffDomain(domain) / 2;
                    (6228: 17) translateX = $$.x(orgDomain[0]) - $$.x(domain[0]);
                    (6231: 21) translateX = ($$.x(orgDomain[0]) - $$.x(domain[0]));
                    (6233: 21) translateX = ($$.x(flowStart.x) - $$.x(flowEnd.x));
                    (6237: 40) transform = 'translate(' + translateX + ',0) scale(' + scaleX + ',1)';
                c3.min.js  (17 usages found)
                    (1: 9579) getTranslate
                    (1: 17529) getTranslate
                    (1: 19070) getTranslate
                    (1: 19113) getTranslate
                    (1: 19153) getTranslate
                    (1: 19193) getTranslate
                    (1: 19263) getTranslate
                    (3: 13254) getTranslate
                    (3: 14156) getTranslate
                    (3: 20188) getTranslate
                    (3: 20552) getTranslate
                    (3: 20863) getTranslate
                    (4: 3690) getTranslate
                    (4: 13113) getTranslate
                    (4: 13538) getTranslate
                    (4: 16854) getTranslate
                    (4: 16900) getTranslate
            amspApp/static/bower_components/c3-angular/examples/assets/js  (34 usages found)
                c3.min.js  (17 usages found)
                    (1: 9579) getTranslate
                    (1: 17529) getTranslate
                    (1: 19070) getTranslate
                    (1: 19113) getTranslate
                    (1: 19153) getTranslate
                    (1: 19193) getTranslate
                    (1: 19263) getTranslate
                    (3: 13254) getTranslate
                    (3: 14156) getTranslate
                    (3: 20188) getTranslate
                    (3: 20552) getTranslate
                    (3: 20863) getTranslate
                    (4: 3690) getTranslate
                    (4: 13113) getTranslate
                    (4: 13538) getTranslate
                    (4: 16854) getTranslate
                    (4: 16900) getTranslate
                d3.min.js  (17 usages found)
                    (2: 1395) translate
                    (2: 4899) translate
                    (2: 5018) translate
                    (2: 13901) translate
                    (2: 14212) translate
                    (2: 14226) translate
                    (3: 16186) translate
                    (3: 18640) translate
                    (4: 1644) translate
                    (4: 2430) translate
                    (4: 2442) translate
                    (4: 2469) translate
                    (4: 2521) translate
                    (4: 2576) translate
                    (4: 2663) translate
                    (4: 2779) translate
                    (4: 15816) translate
            amspApp/static/bower_components/Chart.js  (2 usages found)
                Chart.js  (1 usage found)
                    (1711: 10) ctx.translate(xPos,(isRotated) ? this.endPoint + 12 : this.endPoint + 8);
                Chart.min.js  (1 usage found)
                    (10: 23453) translate
            amspApp/static/bower_components/Chart.js/samples  (12 usages found)
                line-customTooltips.html  (2 usages found)
                    (28: 28) -webkit-transform: translate(-50%, 0);
                    (29: 20) transform: translate(-50%, 0);
                pie-customTooltips.html  (10 usages found)
                    (25: 28) -webkit-transform: translate(-50%, 0);
                    (26: 20) transform: translate(-50%, 0);
                    (29: 28) -webkit-transform: translate(-50%, 0);
                    (30: 20) transform: translate(-50%, 0);
                    (43: 28) -webkit-transform: translate(-50%, -100%);
                    (44: 20) transform: translate(-50%, -100%);
                    (47: 28) -webkit-transform: translate(-50%, -100%);
                    (48: 20) transform: translate(-50%, -100%);
                    (62: 28) -webkit-transform: translate(-50%, 0);
                    (63: 20) transform: translate(-50%, 0);
            amspApp/static/bower_components/Chart.js/src  (1 usage found)
                Chart.Core.js  (1 usage found)
                    (1711: 10) ctx.translate(xPos,(isRotated) ? this.endPoint + 12 : this.endPoint + 8);
            amspApp/static/bower_components/ckeditor/full  (8 usages found)
                CHANGES.md  (4 usages found)
                    (334: 155) * [#11957](http://dev.ckeditor.com/ticket/11957): Fixed: Alignment labels in the [Enhanced Image](http://ckeditor.com/addon/image2) dialog window are not translated.
                    (403: 426) translate
                    (408: 34)   * Default image caption can be translated (customized) with the `editor.lang.image2.captionPlaceholder` string.
                    (521: 165) * [#11196](http://dev.ckeditor.com/ticket/11196): [Accessibility Instructions](http://ckeditor.com/addon/a11yhelp): Allowed additional keyboard button labels to be translated in the dialog window.
                LICENSE.md  (4 usages found)
                    (96: 20) These restrictions translate to certain responsibilities for you if you
                    (134: 46) either verbatim or with modifications and/or translated into another
                    (389: 29) rights.  These restrictions translate to certain responsibilities for
                    (484: 61) portion of it, either verbatim or with modifications and/or translated
            amspApp/static/bower_components/ckeditor/full/samples/css  (5 usages found)
                samples.css  (5 usages found)
                    (984: 22) -webkit-transform: translate(-50%, -50%) !important;
                    (985: 19) -moz-transform: translate(-50%, -50%) !important;
                    (986: 17) -o-transform: translate(-50%, -50%) !important;
                    (987: 18) -ms-transform: translate(-50%, -50%) !important;
                    (988: 14) transform: translate(-50%, -50%) !important;
            amspApp/static/bower_components/d3  (28 usages found)
                d3.js  (28 usages found)
                    (1307: 8) translate
                    (1355: 10) zoom.translate = function(_) {
                    (1426: 14) function translateTo(p, l) {
                    (1438: 7) translateTo(center0 = p, l);
                    (1461: 9) translate: [ view.x, view.y ]
                    (1476: 9) translateTo(d3.mouse(that), location0);
                    (1536: 9) translateTo(p0, l0);
                    (1557: 64) if (mousewheelTimer) clearTimeout(mousewheelTimer); else translate0 = location(center0 = center || d3.mouse(this)),
                    (1565: 7) translateTo(center0, translate0);
                    (1565: 28) translateTo(center0, translate0);
                    (3868: 44) var k = lower48.scale(), t = lower48.translate(), x = (coordinates[0] - t[0]) / k, y = (coordinates[1] - t[1]) / k;
                    (3918: 24) return albersUsa.translate(lower48.translate());
                    (3918: 42) return albersUsa.translate(lower48.translate());
                    (3920: 15) albersUsa.translate = function(_) {
                    (3921: 45) if (!arguments.length) return lower48.translate();
                    (3923: 30) lower48Point = lower48.translate(_).clipExtent([ [ x - .455 * k, y - .238 * k ], [ x + .455 * k, y + .238 * k ] ]).stream(pointStream).point;
                    (3924: 28) alaskaPoint = alaska.translate([ x - .307 * k, y + .201 * k ]).clipExtent([ [ x - .425 * k + ε, y + .12 * k + ε ], [ x - .214 * k - ε, y + .234 * k - ε ] ]).stream(pointStream).point;
                    (3925: 28) hawaiiPoint = hawaii.translate([ x - .205 * k, y + .212 * k ]).clipExtent([ [ x - .214 * k + ε, y + .166 * k + ε ], [ x - .115 * k - ε, y + .234 * k - ε ] ]).stream(pointStream).point;
                    (4342: 16) projection.translate = function(_) {
                    (4734: 58) var m = d3_geo_projection(project), scale = m.scale, translate = m.translate, clipExtent = m.clipExtent, clipAuto;
                    (4734: 72) var m = d3_geo_projection(project), scale = m.scale, translate = m.translate, clipExtent = m.clipExtent, clipAuto;
                    (4739: 7) m.translate = function() {
                    (4740: 15) var v = translate.apply(m, arguments);
                    (4747: 36) var k = π * scale(), t = translate();
                    (5958: 10) this.translate = [ m.e, m.f ];
                    (5963: 32) return "translate(" + this.translate + ")rotate(" + this.rotate + ")skewX(" + this.skew + ")scale(" + this.scale + ")";
                    (5991: 77) var s = [], q = [], n, A = d3.transform(a), B = d3.transform(b), ta = A.translate, tb = B.translate, ra = A.rotate, rb = B.rotate, wa = A.skew, wb = B.skew, ka = A.scale, kb = B.scale;
                    (5991: 95) var s = [], q = [], n, A = d3.transform(a), B = d3.transform(b), ta = A.translate, tb = B.translate, ra = A.rotate, rb = B.rotate, wa = A.skew, wb = B.skew, ka = A.scale, kb = B.scale;
            amspApp/static/bower_components/font-awesome/css  (2 usages found)
                font-awesome.css  (1 usage found)
                    (21: 14) transform: translate(0, 0);
                font-awesome.min.css  (1 usage found)
                    (4: 682) translate
            amspApp/static/bower_components/font-awesome/less  (2 usages found)
                core.less  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
                mixins.less  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
            amspApp/static/bower_components/font-awesome/scss  (2 usages found)
                _core.scss  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
                _mixins.scss  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
            amspApp/static/bower_components/fontawesome/css  (2 usages found)
                font-awesome.css  (1 usage found)
                    (21: 14) transform: translate(0, 0);
                font-awesome.min.css  (1 usage found)
                    (4: 682) translate
            amspApp/static/bower_components/fontawesome/less  (2 usages found)
                core.less  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
                mixins.less  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
            amspApp/static/bower_components/fontawesome/scss  (2 usages found)
                _core.scss  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
                _mixins.scss  (1 usage found)
                    (11: 14) transform: translate(0, 0); // ensures no half-pixel rendering in firefox
            amspApp/static/bower_components/hover  (2 usages found)
                README.md  (2 usages found)
                    (32: 20)         transform: translateZ(0);
                    (123: 16)     transform: translateZ(0);
            amspApp/static/bower_components/hover/css  (1,310 usages found)
                demo-page.css  (10 usages found)
                    (199: 24) -webkit-transform: translateY(-8px) translateZ(0);
                    (199: 41) -webkit-transform: translateY(-8px) translateZ(0);
                    (211: 16) transform: translateY(-8px) translateZ(0);
                    (211: 33) transform: translateY(-8px) translateZ(0);
                    (217: 24) -webkit-transform: translateZ(0);
                    (218: 16) transform: translateZ(0);
                    (222: 22) -webkit-transform: translate(-7px, -7px);
                    (223: 14) transform: translate(-7px, -7px);
                    (227: 22) -webkit-transform: translate(7px, 7px);
                    (228: 14) transform: translate(7px, 7px);
                hover-min.css  (650 usages found)
                    (12: 75) translateZ
                    (12: 99) translateZ
                    (12: 538) translateZ
                    (12: 562) translateZ
                    (12: 1274) translateZ
                    (12: 1298) translateZ
                    (12: 2000) translateZ
                    (12: 2024) translateZ
                    (12: 2827) translateZ
                    (12: 2851) translateZ
                    (12: 3744) translateZ
                    (12: 3768) translateZ
                    (12: 4434) translateZ
                    (12: 4458) translateZ
                    (12: 4969) translateZ
                    (12: 4993) translateZ
                    (12: 5511) translateZ
                    (12: 5535) translateZ
                    (12: 6052) translateZ
                    (12: 6076) translateZ
                    (12: 6530) translateZ
                    (12: 6554) translateZ
                    (12: 7039) translateZ
                    (12: 7063) translateZ
                    (12: 7480) translateY
                    (12: 7507) translateY
                    (12: 7595) translateZ
                    (12: 7619) translateZ
                    (12: 8033) translateY
                    (12: 8059) translateY
                    (12: 8123) translateY
                    (12: 8150) translateY
                    (12: 8189) translateY
                    (12: 8216) translateY
                    (12: 8256) translateY
                    (12: 8283) translateY
                    (12: 8341) translateY
                    (12: 8368) translateY
                    (12: 8407) translateY
                    (12: 8434) translateY
                    (12: 8474) translateY
                    (12: 8501) translateY
                    (12: 8575) translateY
                    (12: 8602) translateY
                    (12: 8668) translateY
                    (12: 8695) translateY
                    (12: 8783) translateZ
                    (12: 8807) translateZ
                    (12: 9577) translateY
                    (12: 9603) translateY
                    (12: 9641) translateY
                    (12: 9667) translateY
                    (12: 9706) translateY
                    (12: 9732) translateY
                    (12: 9790) translateY
                    (12: 9816) translateY
                    (12: 9854) translateY
                    (12: 9880) translateY
                    (12: 9919) translateY
                    (12: 9945) translateY
                    (12: 10018) translateY
                    (12: 10044) translateY
                    (12: 10109) translateY
                    (12: 10135) translateY
                    (12: 10223) translateZ
                    (12: 10247) translateZ
                    (12: 11044) translateZ
                    (12: 11068) translateZ
                    (12: 11517) translateZ
                    (12: 11541) translateZ
                    (12: 12071) translateZ
                    (12: 12095) translateZ
                    (12: 12610) translateY
                    (12: 12636) translateY
                    (12: 12676) translateY
                    (12: 12703) translateY
                    (12: 12745) translateY
                    (12: 12771) translateY
                    (12: 12811) translateY
                    (12: 12838) translateY
                    (12: 12880) translateY
                    (12: 12906) translateY
                    (12: 12945) translateY
                    (12: 12969) translateY
                    (12: 13040) translateY
                    (12: 13066) translateY
                    (12: 13106) translateY
                    (12: 13133) translateY
                    (12: 13175) translateY
                    (12: 13201) translateY
                    (12: 13241) translateY
                    (12: 13268) translateY
                    (12: 13310) translateY
                    (12: 13336) translateY
                    (12: 13375) translateY
                    (12: 13399) translateY
                    (12: 13496) translateZ
                    (12: 13520) translateZ
                    (12: 14089) translateX
                    (12: 14115) translateX
                    (12: 14155) translateX
                    (12: 14182) translateX
                    (12: 14224) translateX
                    (12: 14250) translateX
                    (12: 14290) translateX
                    (12: 14317) translateX
                    (12: 14359) translateX
                    (12: 14385) translateX
                    (12: 14424) translateX
                    (12: 14448) translateX
                    (12: 14521) translateX
                    (12: 14547) translateX
                    (12: 14587) translateX
                    (12: 14614) translateX
                    (12: 14656) translateX
                    (12: 14682) translateX
                    (12: 14722) translateX
                    (12: 14749) translateX
                    (12: 14791) translateX
                    (12: 14817) translateX
                    (12: 14856) translateX
                    (12: 14880) translateX
                    (12: 14979) translateZ
                    (12: 15003) translateZ
                    (12: 15587) translate
                    (12: 15616) translate
                    (12: 15659) translate
                    (12: 15690) translate
                    (12: 15736) translate
                    (12: 15765) translate
                    (12: 15808) translate
                    (12: 15839) translate
                    (12: 15885) translate
                    (12: 15914) translate
                    (12: 15956) translate
                    (12: 15981) translate
                    (12: 16060) translate
                    (12: 16089) translate
                    (12: 16132) translate
                    (12: 16163) translate
                    (12: 16209) translate
                    (12: 16238) translate
                    (12: 16281) translate
                    (12: 16312) translate
                    (12: 16358) translate
                    (12: 16387) translate
                    (12: 16429) translate
                    (12: 16454) translate
                    (12: 16559) translateZ
                    (12: 16583) translateZ
                    (12: 17189) translate
                    (12: 17219) translate
                    (12: 17263) translate
                    (12: 17293) translate
                    (12: 17338) translate
                    (12: 17368) translate
                    (12: 17412) translate
                    (12: 17442) translate
                    (12: 17487) translate
                    (12: 17517) translate
                    (12: 17560) translate
                    (12: 17585) translate
                    (12: 17661) translate
                    (12: 17691) translate
                    (12: 17735) translate
                    (12: 17765) translate
                    (12: 17810) translate
                    (12: 17840) translate
                    (12: 17884) translate
                    (12: 17914) translate
                    (12: 17959) translate
                    (12: 17989) translate
                    (12: 18032) translate
                    (12: 18057) translate
                    (12: 18159) translateZ
                    (12: 18183) translateZ
                    (12: 19529) translateZ
                    (12: 19553) translateZ
                    (12: 20919) translateZ
                    (12: 20943) translateZ
                    (12: 22318) translateZ
                    (12: 22342) translateZ
                    (12: 22875) translateX
                    (12: 22914) translateX
                    (12: 22966) translateX
                    (12: 23007) translateX
                    (12: 23081) translateX
                    (12: 23120) translateX
                    (12: 23172) translateX
                    (12: 23213) translateX
                    (12: 23316) translateZ
                    (12: 23340) translateZ
                    (12: 23850) translateX
                    (12: 23889) translateX
                    (12: 23940) translateX
                    (12: 23981) translateX
                    (12: 24034) translateX
                    (12: 24073) translateX
                    (12: 24124) translateX
                    (12: 24165) translateX
                    (12: 24218) translateX
                    (12: 24257) translateX
                    (12: 24308) translateX
                    (12: 24349) translateX
                    (12: 24402) translateX
                    (12: 24441) translateX
                    (12: 24492) translateX
                    (12: 24533) translateX
                    (12: 24586) translateX
                    (12: 24622) translateX
                    (12: 24671) translateX
                    (12: 24708) translateX
                    (12: 24782) translateX
                    (12: 24821) translateX
                    (12: 24872) translateX
                    (12: 24913) translateX
                    (12: 24966) translateX
                    (12: 25005) translateX
                    (12: 25056) translateX
                    (12: 25097) translateX
                    (12: 25150) translateX
                    (12: 25189) translateX
                    (12: 25240) translateX
                    (12: 25281) translateX
                    (12: 25334) translateX
                    (12: 25373) translateX
                    (12: 25424) translateX
                    (12: 25465) translateX
                    (12: 25518) translateX
                    (12: 25554) translateX
                    (12: 25603) translateX
                    (12: 25640) translateX
                    (12: 25743) translateZ
                    (12: 25767) translateZ
                    (12: 26300) translateZ
                    (12: 26324) translateZ
                    (12: 26941) translateZ
                    (12: 26965) translateZ
                    (12: 27803) translateZ
                    (12: 27827) translateZ
                    (12: 28844) translateZ
                    (12: 28868) translateZ
                    (12: 29886) translateZ
                    (12: 29910) translateZ
                    (12: 30933) translateZ
                    (12: 30957) translateZ
                    (12: 31968) translateZ
                    (12: 31992) translateZ
                    (12: 33143) translateZ
                    (12: 33167) translateZ
                    (12: 34319) translateZ
                    (12: 34343) translateZ
                    (12: 35500) translateZ
                    (12: 35524) translateZ
                    (12: 36663) translateZ
                    (12: 36687) translateZ
                    (12: 37668) translateZ
                    (12: 37692) translateZ
                    (12: 38669) translateZ
                    (12: 38693) translateZ
                    (12: 39657) translateZ
                    (12: 39681) translateZ
                    (12: 40660) translateZ
                    (12: 40684) translateZ
                    (12: 41774) translateZ
                    (12: 41798) translateZ
                    (12: 42892) translateZ
                    (12: 42916) translateZ
                    (12: 43990) translateZ
                    (12: 44014) translateZ
                    (12: 45086) translateZ
                    (12: 45110) translateZ
                    (12: 45603) translateZ
                    (12: 45627) translateZ
                    (12: 46061) translateZ
                    (12: 46085) translateZ
                    (12: 46823) translateZ
                    (12: 46847) translateZ
                    (12: 47549) translateZ
                    (12: 47573) translateZ
                    (12: 48147) translateZ
                    (12: 48171) translateZ
                    (12: 48798) translateZ
                    (12: 48822) translateZ
                    (12: 49504) translateZ
                    (12: 49528) translateZ
                    (12: 49983) translateZ
                    (12: 50007) translateZ
                    (12: 50720) translateZ
                    (12: 50744) translateZ
                    (12: 51482) translateZ
                    (12: 51506) translateZ
                    (12: 52217) translateZ
                    (12: 52241) translateZ
                    (12: 52946) translateZ
                    (12: 52970) translateZ
                    (12: 53700) translateZ
                    (12: 53724) translateZ
                    (12: 54416) translateZ
                    (12: 54440) translateZ
                    (12: 55065) translateY
                    (12: 55089) translateY
                    (12: 55203) translateZ
                    (12: 55227) translateZ
                    (12: 55545) translateY
                    (12: 55571) translateY
                    (12: 55915) translateY
                    (12: 55939) translateY
                    (12: 56035) translateZ
                    (12: 56059) translateZ
                    (12: 56373) translateY
                    (12: 56400) translateY
                    (12: 56742) translateY
                    (12: 56766) translateY
                    (12: 56851) translateZ
                    (12: 56875) translateZ
                    (12: 57300) translateZ
                    (12: 57324) translateZ
                    (12: 57770) translateZ
                    (12: 57794) translateZ
                    (12: 58331) translateZ
                    (12: 58355) translateZ
                    (12: 58833) translateZ
                    (12: 58857) translateZ
                    (12: 59383) translateZ
                    (12: 59407) translateZ
                    (12: 60226) translateY
                    (12: 60253) translateY
                    (12: 60392) translateY
                    (12: 60418) translateY
                    (12: 60514) translateZ
                    (12: 60538) translateZ
                    (12: 61672) translateZ
                    (12: 61696) translateZ
                    (12: 62287) translateY
                    (12: 62315) translateY
                    (12: 62412) translateZ
                    (12: 62436) translateZ
                    (12: 63053) translateX
                    (12: 63080) translateX
                    (12: 63177) translateZ
                    (12: 63201) translateZ
                    (12: 63807) translateY
                    (12: 63834) translateY
                    (12: 63929) translateZ
                    (12: 63953) translateZ
                    (12: 64565) translateX
                    (12: 64593) translateX
                    (12: 64694) translateZ
                    (12: 64718) translateZ
                    (12: 65416) translateY
                    (12: 65443) translateY
                    (12: 65584) translateY
                    (12: 65612) translateY
                    (12: 65715) translateZ
                    (12: 65739) translateZ
                    (12: 66463) translateX
                    (12: 66491) translateX
                    (12: 66639) translateX
                    (12: 66666) translateX
                    (12: 66769) translateZ
                    (12: 66793) translateZ
                    (12: 67506) translateY
                    (12: 67534) translateY
                    (12: 67685) translateY
                    (12: 67712) translateY
                    (12: 67813) translateZ
                    (12: 67837) translateZ
                    (12: 68556) translateX
                    (12: 68583) translateX
                    (12: 68727) translateX
                    (12: 68755) translateX
                    (12: 68849) translateZ
                    (12: 68873) translateZ
                    (12: 69230) translateZ
                    (12: 69254) translateZ
                    (12: 69575) translateX
                    (12: 69602) translateX
                    (12: 69698) translateZ
                    (12: 69722) translateZ
                    (12: 70084) translateZ
                    (12: 70108) translateZ
                    (12: 70438) translateX
                    (12: 70464) translateX
                    (12: 70543) translateY
                    (12: 70567) translateY
                    (12: 70607) translateY
                    (12: 70633) translateY
                    (12: 70705) translateY
                    (12: 70729) translateY
                    (12: 70769) translateY
                    (12: 70795) translateY
                    (12: 70888) translateZ
                    (12: 70912) translateZ
                    (12: 71215) translateZ
                    (12: 71239) translateZ
                    (12: 71599) translateY
                    (12: 71623) translateY
                    (12: 71663) translateY
                    (12: 71690) translateY
                    (12: 71761) translateY
                    (12: 71785) translateY
                    (12: 71825) translateY
                    (12: 71852) translateY
                    (12: 71944) translateZ
                    (12: 71968) translateZ
                    (12: 72269) translateZ
                    (12: 72293) translateZ
                    (12: 72658) translateZ
                    (12: 72682) translateZ
                    (12: 73396) translateY
                    (12: 73424) translateY
                    (12: 73532) translateY
                    (12: 73560) translateY
                    (12: 73674) translateZ
                    (12: 73698) translateZ
                    (12: 74011) translateZ
                    (12: 74035) translateZ
                    (12: 74634) translateZ
                    (12: 74658) translateZ
                    (12: 74961) translateZ
                    (12: 74985) translateZ
                    (12: 75299) translateY
                    (12: 75326) translateY
                    (12: 75421) translateY
                    (12: 75448) translateY
                    (12: 75548) translateZ
                    (12: 75572) translateZ
                    (12: 76387) translateY
                    (12: 76413) translateY
                    (12: 76506) translateY
                    (12: 76532) translateY
                    (12: 76630) translateZ
                    (12: 76654) translateZ
                    (12: 76988) translateZ
                    (12: 77012) translateZ
                    (12: 77509) translateZ
                    (12: 77533) translateZ
                    (12: 77892) translateZ
                    (12: 77916) translateZ
                    (12: 78248) translateZ
                    (12: 78283) translateZ
                    (12: 78375) translateZ
                    (12: 78399) translateZ
                    (12: 78760) translateZ
                    (12: 78784) translateZ
                    (12: 79498) translateZ
                    (12: 79522) translateZ
                    (12: 79826) translateZ
                    (12: 79850) translateZ
                    (12: 80564) translateZ
                    (12: 80588) translateZ
                    (12: 80897) translateZ
                    (12: 80921) translateZ
                    (12: 81736) translateZ
                    (12: 81760) translateZ
                    (12: 82071) translateZ
                    (12: 82095) translateZ
                    (12: 82898) translateZ
                    (12: 82922) translateZ
                    (12: 83281) translateZ
                    (12: 83305) translateZ
                    (12: 84107) translateZ
                    (12: 84131) translateZ
                    (12: 84489) translateZ
                    (12: 84513) translateZ
                    (12: 85147) translateZ
                    (12: 85171) translateZ
                    (12: 85532) translateZ
                    (12: 85556) translateZ
                    (12: 86121) translateZ
                    (12: 86145) translateZ
                    (12: 86506) translateZ
                    (12: 86530) translateZ
                    (12: 86978) translateZ
                    (12: 87002) translateZ
                    (12: 87368) translateZ
                    (12: 87392) translateZ
                    (12: 87871) translateZ
                    (12: 87895) translateZ
                    (12: 88255) translateZ
                    (12: 88279) translateZ
                    (12: 88603) translateY
                    (12: 88630) translateY
                    (12: 88723) translateZ
                    (12: 88747) translateZ
                    (12: 89106) translateZ
                    (12: 89130) translateZ
                    (12: 89451) translateY
                    (12: 89477) translateY
                    (12: 89546) translateY
                    (12: 89573) translateY
                    (12: 89612) translateY
                    (12: 89639) translateY
                    (12: 89679) translateY
                    (12: 89706) translateY
                    (12: 89769) translateY
                    (12: 89796) translateY
                    (12: 89835) translateY
                    (12: 89862) translateY
                    (12: 89902) translateY
                    (12: 89929) translateY
                    (12: 90008) translateY
                    (12: 90035) translateY
                    (12: 90106) translateY
                    (12: 90133) translateY
                    (12: 90226) translateZ
                    (12: 90250) translateZ
                    (12: 90608) translateZ
                    (12: 90632) translateZ
                    (12: 91334) translateY
                    (12: 91360) translateY
                    (12: 91398) translateY
                    (12: 91424) translateY
                    (12: 91463) translateY
                    (12: 91489) translateY
                    (12: 91552) translateY
                    (12: 91578) translateY
                    (12: 91616) translateY
                    (12: 91642) translateY
                    (12: 91681) translateY
                    (12: 91707) translateY
                    (12: 91785) translateY
                    (12: 91811) translateY
                    (12: 91881) translateY
                    (12: 91907) translateY
                    (12: 92000) translateZ
                    (12: 92024) translateZ
                    (12: 92383) translateZ
                    (12: 92407) translateZ
                    (12: 93131) translateX
                    (12: 93157) translateX
                    (12: 93197) translateX
                    (12: 93224) translateX
                    (12: 93266) translateX
                    (12: 93292) translateX
                    (12: 93332) translateX
                    (12: 93359) translateX
                    (12: 93401) translateX
                    (12: 93427) translateX
                    (12: 93466) translateX
                    (12: 93490) translateX
                    (12: 93568) translateX
                    (12: 93594) translateX
                    (12: 93634) translateX
                    (12: 93661) translateX
                    (12: 93703) translateX
                    (12: 93729) translateX
                    (12: 93769) translateX
                    (12: 93796) translateX
                    (12: 93838) translateX
                    (12: 93864) translateX
                    (12: 93903) translateX
                    (12: 93927) translateX
                    (12: 94031) translateZ
                    (12: 94055) translateZ
                    (12: 94427) translateZ
                    (12: 94451) translateZ
                    (12: 94950) translateY
                    (12: 94976) translateY
                    (12: 95016) translateY
                    (12: 95043) translateY
                    (12: 95085) translateY
                    (12: 95111) translateY
                    (12: 95151) translateY
                    (12: 95178) translateY
                    (12: 95220) translateY
                    (12: 95246) translateY
                    (12: 95285) translateY
                    (12: 95309) translateY
                    (12: 95385) translateY
                    (12: 95411) translateY
                    (12: 95451) translateY
                    (12: 95478) translateY
                    (12: 95520) translateY
                    (12: 95546) translateY
                    (12: 95586) translateY
                    (12: 95613) translateY
                    (12: 95655) translateY
                    (12: 95681) translateY
                    (12: 95720) translateY
                    (12: 95744) translateY
                    (12: 95846) translateZ
                    (12: 95870) translateZ
                    (12: 96240) translateZ
                    (12: 96264) translateZ
                    (12: 96739) translateX
                    (12: 96778) translateX
                    (12: 96830) translateX
                    (12: 96871) translateX
                    (12: 96950) translateX
                    (12: 96989) translateX
                    (12: 97041) translateX
                    (12: 97082) translateX
                    (12: 97190) translateZ
                    (12: 97214) translateZ
                    (12: 97573) translateZ
                    (12: 97597) translateZ
                    (12: 98029) translateX
                    (12: 98068) translateX
                    (12: 98119) translateX
                    (12: 98160) translateX
                    (12: 98213) translateX
                    (12: 98252) translateX
                    (12: 98303) translateX
                    (12: 98344) translateX
                    (12: 98397) translateX
                    (12: 98436) translateX
                    (12: 98487) translateX
                    (12: 98528) translateX
                    (12: 98581) translateX
                    (12: 98620) translateX
                    (12: 98671) translateX
                    (12: 98712) translateX
                    (12: 98765) translateX
                    (12: 98801) translateX
                    (12: 98850) translateX
                    (12: 98887) translateX
                    (12: 98966) translateX
                    (12: 99005) translateX
                    (12: 99056) translateX
                    (12: 99097) translateX
                    (12: 99150) translateX
                    (12: 99189) translateX
                    (12: 99240) translateX
                    (12: 99281) translateX
                    (12: 99334) translateX
                    (12: 99373) translateX
                    (12: 99424) translateX
                    (12: 99465) translateX
                    (12: 99518) translateX
                    (12: 99557) translateX
                    (12: 99608) translateX
                    (12: 99649) translateX
                    (12: 99702) translateX
                    (12: 99738) translateX
                    (12: 99787) translateX
                    (12: 99824) translateX
                    (12: 99932) translateZ
                    (12: 99956) translateZ
                    (12: 100319) translateZ
                    (12: 100343) translateZ
                    (12: 100802) translateZ
                    (12: 100826) translateZ
                    (12: 101675) translateZ
                    (12: 101699) translateZ
                    (12: 102430) translateZ
                    (12: 102454) translateZ
                    (12: 103200) translateZ
                    (12: 103224) translateZ
                hover.css  (650 usages found)
                    (18: 22) -webkit-transform: translateZ(0);
                    (19: 14) transform: translateZ(0);
                    (38: 22) -webkit-transform: translateZ(0);
                    (39: 14) transform: translateZ(0);
                    (82: 22) -webkit-transform: translateZ(0);
                    (83: 14) transform: translateZ(0);
                    (118: 22) -webkit-transform: translateZ(0);
                    (119: 14) transform: translateZ(0);
                    (156: 22) -webkit-transform: translateZ(0);
                    (157: 14) transform: translateZ(0);
                    (204: 22) -webkit-transform: translateZ(0);
                    (205: 14) transform: translateZ(0);
                    (240: 22) -webkit-transform: translateZ(0);
                    (241: 14) transform: translateZ(0);
                    (262: 22) -webkit-transform: translateZ(0);
                    (263: 14) transform: translateZ(0);
                    (282: 22) -webkit-transform: translateZ(0);
                    (283: 14) transform: translateZ(0);
                    (302: 22) -webkit-transform: translateZ(0);
                    (303: 14) transform: translateZ(0);
                    (322: 22) -webkit-transform: translateZ(0);
                    (323: 14) transform: translateZ(0);
                    (342: 22) -webkit-transform: translateZ(0);
                    (343: 14) transform: translateZ(0);
                    (356: 22) -webkit-transform: translateY(-8px);
                    (357: 14) transform: translateY(-8px);
                    (364: 22) -webkit-transform: translateZ(0);
                    (365: 14) transform: translateZ(0);
                    (378: 22) -webkit-transform: translateY(8px);
                    (379: 14) transform: translateY(8px);
                    (385: 24) -webkit-transform: translateY(-8px);
                    (386: 16) transform: translateY(-8px);
                    (390: 24) -webkit-transform: translateY(-4px);
                    (391: 16) transform: translateY(-4px);
                    (395: 24) -webkit-transform: translateY(-8px);
                    (396: 16) transform: translateY(-8px);
                    (402: 24) -webkit-transform: translateY(-8px);
                    (403: 16) transform: translateY(-8px);
                    (407: 24) -webkit-transform: translateY(-4px);
                    (408: 16) transform: translateY(-4px);
                    (412: 24) -webkit-transform: translateY(-8px);
                    (413: 16) transform: translateY(-8px);
                    (419: 24) -webkit-transform: translateY(-8px);
                    (420: 16) transform: translateY(-8px);
                    (426: 24) -webkit-transform: translateY(-8px);
                    (427: 16) transform: translateY(-8px);
                    (434: 22) -webkit-transform: translateZ(0);
                    (435: 14) transform: translateZ(0);
                    (461: 24) -webkit-transform: translateY(8px);
                    (462: 16) transform: translateY(8px);
                    (466: 24) -webkit-transform: translateY(4px);
                    (467: 16) transform: translateY(4px);
                    (471: 24) -webkit-transform: translateY(8px);
                    (472: 16) transform: translateY(8px);
                    (478: 24) -webkit-transform: translateY(8px);
                    (479: 16) transform: translateY(8px);
                    (483: 24) -webkit-transform: translateY(4px);
                    (484: 16) transform: translateY(4px);
                    (488: 24) -webkit-transform: translateY(8px);
                    (489: 16) transform: translateY(8px);
                    (495: 24) -webkit-transform: translateY(8px);
                    (496: 16) transform: translateY(8px);
                    (502: 24) -webkit-transform: translateY(8px);
                    (503: 16) transform: translateY(8px);
                    (510: 22) -webkit-transform: translateZ(0);
                    (511: 14) transform: translateZ(0);
                    (538: 22) -webkit-transform: translateZ(0);
                    (539: 14) transform: translateZ(0);
                    (558: 22) -webkit-transform: translateZ(0);
                    (559: 14) transform: translateZ(0);
                    (580: 22) -webkit-transform: translateZ(0);
                    (581: 14) transform: translateZ(0);
                    (601: 24) -webkit-transform: translateY(8px);
                    (602: 16) transform: translateY(8px);
                    (606: 24) -webkit-transform: translateY(-6px);
                    (607: 16) transform: translateY(-6px);
                    (611: 24) -webkit-transform: translateY(4px);
                    (612: 16) transform: translateY(4px);
                    (616: 24) -webkit-transform: translateY(-2px);
                    (617: 16) transform: translateY(-2px);
                    (621: 24) -webkit-transform: translateY(1px);
                    (622: 16) transform: translateY(1px);
                    (626: 24) -webkit-transform: translateY(0);
                    (627: 16) transform: translateY(0);
                    (633: 24) -webkit-transform: translateY(8px);
                    (634: 16) transform: translateY(8px);
                    (638: 24) -webkit-transform: translateY(-6px);
                    (639: 16) transform: translateY(-6px);
                    (643: 24) -webkit-transform: translateY(4px);
                    (644: 16) transform: translateY(4px);
                    (648: 24) -webkit-transform: translateY(-2px);
                    (649: 16) transform: translateY(-2px);
                    (653: 24) -webkit-transform: translateY(1px);
                    (654: 16) transform: translateY(1px);
                    (658: 24) -webkit-transform: translateY(0);
                    (659: 16) transform: translateY(0);
                    (666: 22) -webkit-transform: translateZ(0);
                    (667: 14) transform: translateZ(0);
                    (687: 24) -webkit-transform: translateX(8px);
                    (688: 16) transform: translateX(8px);
                    (692: 24) -webkit-transform: translateX(-6px);
                    (693: 16) transform: translateX(-6px);
                    (697: 24) -webkit-transform: translateX(4px);
                    (698: 16) transform: translateX(4px);
                    (702: 24) -webkit-transform: translateX(-2px);
                    (703: 16) transform: translateX(-2px);
                    (707: 24) -webkit-transform: translateX(1px);
                    (708: 16) transform: translateX(1px);
                    (712: 24) -webkit-transform: translateX(0);
                    (713: 16) transform: translateX(0);
                    (719: 24) -webkit-transform: translateX(8px);
                    (720: 16) transform: translateX(8px);
                    (724: 24) -webkit-transform: translateX(-6px);
                    (725: 16) transform: translateX(-6px);
                    (729: 24) -webkit-transform: translateX(4px);
                    (730: 16) transform: translateX(4px);
                    (734: 24) -webkit-transform: translateX(-2px);
                    (735: 16) transform: translateX(-2px);
                    (739: 24) -webkit-transform: translateX(1px);
                    (740: 16) transform: translateX(1px);
                    (744: 24) -webkit-transform: translateX(0);
                    (745: 16) transform: translateX(0);
                    (752: 22) -webkit-transform: translateZ(0);
                    (753: 14) transform: translateZ(0);
                    (773: 24) -webkit-transform: translate(8px, 8px);
                    (774: 16) transform: translate(8px, 8px);
                    (778: 24) -webkit-transform: translate(-6px, -6px);
                    (779: 16) transform: translate(-6px, -6px);
                    (783: 24) -webkit-transform: translate(4px, 4px);
                    (784: 16) transform: translate(4px, 4px);
                    (788: 24) -webkit-transform: translate(-2px, -2px);
                    (789: 16) transform: translate(-2px, -2px);
                    (793: 24) -webkit-transform: translate(1px, 1px);
                    (794: 16) transform: translate(1px, 1px);
                    (798: 24) -webkit-transform: translate(0, 0);
                    (799: 16) transform: translate(0, 0);
                    (805: 24) -webkit-transform: translate(8px, 8px);
                    (806: 16) transform: translate(8px, 8px);
                    (810: 24) -webkit-transform: translate(-6px, -6px);
                    (811: 16) transform: translate(-6px, -6px);
                    (815: 24) -webkit-transform: translate(4px, 4px);
                    (816: 16) transform: translate(4px, 4px);
                    (820: 24) -webkit-transform: translate(-2px, -2px);
                    (821: 16) transform: translate(-2px, -2px);
                    (825: 24) -webkit-transform: translate(1px, 1px);
                    (826: 16) transform: translate(1px, 1px);
                    (830: 24) -webkit-transform: translate(0, 0);
                    (831: 16) transform: translate(0, 0);
                    (838: 22) -webkit-transform: translateZ(0);
                    (839: 14) transform: translateZ(0);
                    (859: 24) -webkit-transform: translate(8px, -8px);
                    (860: 16) transform: translate(8px, -8px);
                    (864: 24) -webkit-transform: translate(-6px, 6px);
                    (865: 16) transform: translate(-6px, 6px);
                    (869: 24) -webkit-transform: translate(4px, -4px);
                    (870: 16) transform: translate(4px, -4px);
                    (874: 24) -webkit-transform: translate(-2px, 2px);
                    (875: 16) transform: translate(-2px, 2px);
                    (879: 24) -webkit-transform: translate(1px, -1px);
                    (880: 16) transform: translate(1px, -1px);
                    (884: 24) -webkit-transform: translate(0, 0);
                    (885: 16) transform: translate(0, 0);
                    (891: 24) -webkit-transform: translate(8px, -8px);
                    (892: 16) transform: translate(8px, -8px);
                    (896: 24) -webkit-transform: translate(-6px, 6px);
                    (897: 16) transform: translate(-6px, 6px);
                    (901: 24) -webkit-transform: translate(4px, -4px);
                    (902: 16) transform: translate(4px, -4px);
                    (906: 24) -webkit-transform: translate(-2px, 2px);
                    (907: 16) transform: translate(-2px, 2px);
                    (911: 24) -webkit-transform: translate(1px, -1px);
                    (912: 16) transform: translate(1px, -1px);
                    (916: 24) -webkit-transform: translate(0, 0);
                    (917: 16) transform: translate(0, 0);
                    (924: 22) -webkit-transform: translateZ(0);
                    (925: 14) transform: translateZ(0);
                    (1010: 22) -webkit-transform: translateZ(0);
                    (1011: 14) transform: translateZ(0);
                    (1098: 22) -webkit-transform: translateZ(0);
                    (1099: 14) transform: translateZ(0);
                    (1186: 22) -webkit-transform: translateZ(0);
                    (1187: 14) transform: translateZ(0);
                    (1207: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1208: 16) transform: translateX(3px) rotate(2deg);
                    (1212: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1213: 16) transform: translateX(-3px) rotate(-2deg);
                    (1219: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1220: 16) transform: translateX(3px) rotate(2deg);
                    (1224: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1225: 16) transform: translateX(-3px) rotate(-2deg);
                    (1232: 22) -webkit-transform: translateZ(0);
                    (1233: 14) transform: translateZ(0);
                    (1253: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1254: 16) transform: translateX(3px) rotate(2deg);
                    (1258: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1259: 16) transform: translateX(-3px) rotate(-2deg);
                    (1263: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1264: 16) transform: translateX(3px) rotate(2deg);
                    (1268: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1269: 16) transform: translateX(-3px) rotate(-2deg);
                    (1273: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (1274: 16) transform: translateX(2px) rotate(1deg);
                    (1278: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (1279: 16) transform: translateX(-2px) rotate(-1deg);
                    (1283: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (1284: 16) transform: translateX(2px) rotate(1deg);
                    (1288: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (1289: 16) transform: translateX(-2px) rotate(-1deg);
                    (1293: 24) -webkit-transform: translateX(1px) rotate(0);
                    (1294: 16) transform: translateX(1px) rotate(0);
                    (1298: 24) -webkit-transform: translateX(-1px) rotate(0);
                    (1299: 16) transform: translateX(-1px) rotate(0);
                    (1305: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1306: 16) transform: translateX(3px) rotate(2deg);
                    (1310: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1311: 16) transform: translateX(-3px) rotate(-2deg);
                    (1315: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (1316: 16) transform: translateX(3px) rotate(2deg);
                    (1320: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (1321: 16) transform: translateX(-3px) rotate(-2deg);
                    (1325: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (1326: 16) transform: translateX(2px) rotate(1deg);
                    (1330: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (1331: 16) transform: translateX(-2px) rotate(-1deg);
                    (1335: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (1336: 16) transform: translateX(2px) rotate(1deg);
                    (1340: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (1341: 16) transform: translateX(-2px) rotate(-1deg);
                    (1345: 24) -webkit-transform: translateX(1px) rotate(0);
                    (1346: 16) transform: translateX(1px) rotate(0);
                    (1350: 24) -webkit-transform: translateX(-1px) rotate(0);
                    (1351: 16) transform: translateX(-1px) rotate(0);
                    (1358: 22) -webkit-transform: translateZ(0);
                    (1359: 14) transform: translateZ(0);
                    (1381: 22) -webkit-transform: translateZ(0);
                    (1382: 14) transform: translateZ(0);
                    (1414: 22) -webkit-transform: translateZ(0);
                    (1415: 14) transform: translateZ(0);
                    (1446: 22) -webkit-transform: translateZ(0);
                    (1447: 14) transform: translateZ(0);
                    (1490: 22) -webkit-transform: translateZ(0);
                    (1491: 14) transform: translateZ(0);
                    (1534: 22) -webkit-transform: translateZ(0);
                    (1535: 14) transform: translateZ(0);
                    (1578: 22) -webkit-transform: translateZ(0);
                    (1579: 14) transform: translateZ(0);
                    (1622: 22) -webkit-transform: translateZ(0);
                    (1623: 14) transform: translateZ(0);
                    (1668: 22) -webkit-transform: translateZ(0);
                    (1669: 14) transform: translateZ(0);
                    (1714: 22) -webkit-transform: translateZ(0);
                    (1715: 14) transform: translateZ(0);
                    (1760: 22) -webkit-transform: translateZ(0);
                    (1761: 14) transform: translateZ(0);
                    (1806: 22) -webkit-transform: translateZ(0);
                    (1807: 14) transform: translateZ(0);
                    (1851: 22) -webkit-transform: translateZ(0);
                    (1852: 14) transform: translateZ(0);
                    (1896: 22) -webkit-transform: translateZ(0);
                    (1897: 14) transform: translateZ(0);
                    (1939: 22) -webkit-transform: translateZ(0);
                    (1940: 14) transform: translateZ(0);
                    (1982: 22) -webkit-transform: translateZ(0);
                    (1983: 14) transform: translateZ(0);
                    (2027: 22) -webkit-transform: translateZ(0);
                    (2028: 14) transform: translateZ(0);
                    (2072: 22) -webkit-transform: translateZ(0);
                    (2073: 14) transform: translateZ(0);
                    (2117: 22) -webkit-transform: translateZ(0);
                    (2118: 14) transform: translateZ(0);
                    (2163: 22) -webkit-transform: translateZ(0);
                    (2164: 14) transform: translateZ(0);
                    (2185: 22) -webkit-transform: translateZ(0);
                    (2186: 14) transform: translateZ(0);
                    (2206: 22) -webkit-transform: translateZ(0);
                    (2207: 14) transform: translateZ(0);
                    (2256: 22) -webkit-transform: translateZ(0);
                    (2257: 14) transform: translateZ(0);
                    (2304: 22) -webkit-transform: translateZ(0);
                    (2305: 14) transform: translateZ(0);
                    (2333: 22) -webkit-transform: translateZ(0);
                    (2334: 14) transform: translateZ(0);
                    (2365: 22) -webkit-transform: translateZ(0);
                    (2366: 14) transform: translateZ(0);
                    (2400: 22) -webkit-transform: translateZ(0);
                    (2401: 14) transform: translateZ(0);
                    (2419: 22) -webkit-transform: translateZ(0);
                    (2420: 14) transform: translateZ(0);
                    (2452: 22) -webkit-transform: translateZ(0);
                    (2453: 14) transform: translateZ(0);
                    (2486: 22) -webkit-transform: translateZ(0);
                    (2487: 14) transform: translateZ(0);
                    (2519: 22) -webkit-transform: translateZ(0);
                    (2520: 14) transform: translateZ(0);
                    (2552: 22) -webkit-transform: translateZ(0);
                    (2553: 14) transform: translateZ(0);
                    (2586: 22) -webkit-transform: translateZ(0);
                    (2587: 14) transform: translateZ(0);
                    (2619: 22) -webkit-transform: translateZ(0);
                    (2620: 14) transform: translateZ(0);
                    (2647: 22) -webkit-transform: translateY(0);
                    (2648: 14) transform: translateY(0);
                    (2656: 22) -webkit-transform: translateZ(0);
                    (2657: 14) transform: translateZ(0);
                    (2674: 22) -webkit-transform: translateY(4px);
                    (2675: 14) transform: translateY(4px);
                    (2684: 22) -webkit-transform: translateY(0);
                    (2685: 14) transform: translateY(0);
                    (2692: 22) -webkit-transform: translateZ(0);
                    (2693: 14) transform: translateZ(0);
                    (2710: 22) -webkit-transform: translateY(-4px);
                    (2711: 14) transform: translateY(-4px);
                    (2720: 22) -webkit-transform: translateY(0);
                    (2721: 14) transform: translateY(0);
                    (2729: 22) -webkit-transform: translateZ(0);
                    (2730: 14) transform: translateZ(0);
                    (2748: 22) -webkit-transform: translateZ(0);
                    (2749: 14) transform: translateZ(0);
                    (2767: 22) -webkit-transform: translateZ(0);
                    (2768: 14) transform: translateZ(0);
                    (2788: 22) -webkit-transform: translateZ(0);
                    (2789: 14) transform: translateZ(0);
                    (2807: 22) -webkit-transform: translateZ(0);
                    (2808: 14) transform: translateZ(0);
                    (2829: 22) -webkit-transform: translateZ(0);
                    (2830: 14) transform: translateZ(0);
                    (2860: 22) -webkit-transform: translateY(-5px);
                    (2861: 14) transform: translateY(-5px);
                    (2866: 22) -webkit-transform: translateY(5px);
                    (2867: 14) transform: translateY(5px);
                    (2875: 22) -webkit-transform: translateZ(0);
                    (2876: 14) transform: translateZ(0);
                    (2917: 22) -webkit-transform: translateZ(0);
                    (2918: 14) transform: translateZ(0);
                    (2941: 22) -webkit-transform: translateY(-10px);
                    (2942: 14) transform: translateY(-10px);
                    (2949: 22) -webkit-transform: translateZ(0);
                    (2950: 14) transform: translateZ(0);
                    (2973: 22) -webkit-transform: translateX(10px);
                    (2974: 14) transform: translateX(10px);
                    (2981: 22) -webkit-transform: translateZ(0);
                    (2982: 14) transform: translateZ(0);
                    (3005: 22) -webkit-transform: translateY(10px);
                    (3006: 14) transform: translateY(10px);
                    (3013: 22) -webkit-transform: translateZ(0);
                    (3014: 14) transform: translateZ(0);
                    (3037: 22) -webkit-transform: translateX(-10px);
                    (3038: 14) transform: translateX(-10px);
                    (3045: 22) -webkit-transform: translateZ(0);
                    (3046: 14) transform: translateZ(0);
                    (3072: 22) -webkit-transform: translateY(10px);
                    (3073: 14) transform: translateY(10px);
                    (3076: 22) -webkit-transform: translateY(-10px);
                    (3077: 14) transform: translateY(-10px);
                    (3084: 22) -webkit-transform: translateZ(0);
                    (3085: 14) transform: translateZ(0);
                    (3111: 22) -webkit-transform: translateX(-10px);
                    (3112: 14) transform: translateX(-10px);
                    (3115: 22) -webkit-transform: translateX(10px);
                    (3116: 14) transform: translateX(10px);
                    (3123: 22) -webkit-transform: translateZ(0);
                    (3124: 14) transform: translateZ(0);
                    (3150: 22) -webkit-transform: translateY(-10px);
                    (3151: 14) transform: translateY(-10px);
                    (3154: 22) -webkit-transform: translateY(10px);
                    (3155: 14) transform: translateY(10px);
                    (3162: 22) -webkit-transform: translateZ(0);
                    (3163: 14) transform: translateZ(0);
                    (3189: 22) -webkit-transform: translateX(10px);
                    (3190: 14) transform: translateX(10px);
                    (3193: 22) -webkit-transform: translateX(-10px);
                    (3194: 14) transform: translateX(-10px);
                    (3202: 22) -webkit-transform: translateZ(0);
                    (3203: 14) transform: translateZ(0);
                    (3219: 22) -webkit-transform: translateZ(0);
                    (3220: 14) transform: translateZ(0);
                    (3229: 22) -webkit-transform: translateX(-4px);
                    (3230: 14) transform: translateX(-4px);
                    (3237: 22) -webkit-transform: translateZ(0);
                    (3238: 14) transform: translateZ(0);
                    (3254: 22) -webkit-transform: translateZ(0);
                    (3255: 14) transform: translateZ(0);
                    (3264: 22) -webkit-transform: translateX(4px);
                    (3265: 14) transform: translateX(4px);
                    (3273: 24) -webkit-transform: translateY(0);
                    (3274: 16) transform: translateY(0);
                    (3279: 24) -webkit-transform: translateY(6px);
                    (3280: 16) transform: translateY(6px);
                    (3288: 24) -webkit-transform: translateY(0);
                    (3289: 16) transform: translateY(0);
                    (3294: 24) -webkit-transform: translateY(6px);
                    (3295: 16) transform: translateY(6px);
                    (3303: 22) -webkit-transform: translateZ(0);
                    (3304: 14) transform: translateZ(0);
                    (3318: 22) -webkit-transform: translateZ(0);
                    (3319: 14) transform: translateZ(0);
                    (3335: 24) -webkit-transform: translateY(0);
                    (3336: 16) transform: translateY(0);
                    (3341: 24) -webkit-transform: translateY(-6px);
                    (3342: 16) transform: translateY(-6px);
                    (3350: 24) -webkit-transform: translateY(0);
                    (3351: 16) transform: translateY(0);
                    (3356: 24) -webkit-transform: translateY(-6px);
                    (3357: 16) transform: translateY(-6px);
                    (3365: 22) -webkit-transform: translateZ(0);
                    (3366: 14) transform: translateZ(0);
                    (3380: 22) -webkit-transform: translateZ(0);
                    (3381: 14) transform: translateZ(0);
                    (3396: 22) -webkit-transform: translateZ(0);
                    (3397: 14) transform: translateZ(0);
                    (3431: 24) -webkit-transform: translateY(-100%);
                    (3432: 16) transform: translateY(-100%);
                    (3448: 24) -webkit-transform: translateY(-100%);
                    (3449: 16) transform: translateY(-100%);
                    (3462: 22) -webkit-transform: translateZ(0);
                    (3463: 14) transform: translateZ(0);
                    (3478: 22) -webkit-transform: translateZ(0);
                    (3479: 14) transform: translateZ(0);
                    (3503: 22) -webkit-transform: translateZ(0);
                    (3504: 14) transform: translateZ(0);
                    (3518: 22) -webkit-transform: translateZ(0);
                    (3519: 14) transform: translateZ(0);
                    (3537: 24) -webkit-transform: translateY(-1em);
                    (3538: 16) transform: translateY(-1em);
                    (3549: 24) -webkit-transform: translateY(-1em);
                    (3550: 16) transform: translateY(-1em);
                    (3558: 22) -webkit-transform: translateZ(0);
                    (3559: 14) transform: translateZ(0);
                    (3596: 24) -webkit-transform: translateY(1em);
                    (3597: 16) transform: translateY(1em);
                    (3608: 24) -webkit-transform: translateY(1em);
                    (3609: 16) transform: translateY(1em);
                    (3617: 22) -webkit-transform: translateZ(0);
                    (3618: 14) transform: translateZ(0);
                    (3632: 22) -webkit-transform: translateZ(0);
                    (3633: 14) transform: translateZ(0);
                    (3653: 22) -webkit-transform: translateZ(0);
                    (3654: 14) transform: translateZ(0);
                    (3670: 22) -webkit-transform: translateZ(0);
                    (3671: 14) transform: translateZ(0);
                    (3680: 33) -webkit-transform: scale(1.3) translateZ(0);
                    (3681: 25) transform: scale(1.3) translateZ(0);
                    (3688: 22) -webkit-transform: translateZ(0);
                    (3689: 14) transform: translateZ(0);
                    (3705: 22) -webkit-transform: translateZ(0);
                    (3706: 14) transform: translateZ(0);
                    (3747: 22) -webkit-transform: translateZ(0);
                    (3748: 14) transform: translateZ(0);
                    (3762: 22) -webkit-transform: translateZ(0);
                    (3763: 14) transform: translateZ(0);
                    (3796: 22) -webkit-transform: translateZ(0);
                    (3797: 14) transform: translateZ(0);
                    (3811: 22) -webkit-transform: translateZ(0);
                    (3812: 14) transform: translateZ(0);
                    (3847: 22) -webkit-transform: translateZ(0);
                    (3848: 14) transform: translateZ(0);
                    (3862: 22) -webkit-transform: translateZ(0);
                    (3863: 14) transform: translateZ(0);
                    (3898: 22) -webkit-transform: translateZ(0);
                    (3899: 14) transform: translateZ(0);
                    (3915: 22) -webkit-transform: translateZ(0);
                    (3916: 14) transform: translateZ(0);
                    (3953: 22) -webkit-transform: translateZ(0);
                    (3954: 14) transform: translateZ(0);
                    (3970: 22) -webkit-transform: translateZ(0);
                    (3971: 14) transform: translateZ(0);
                    (3994: 22) -webkit-transform: translateZ(0);
                    (3995: 14) transform: translateZ(0);
                    (4011: 22) -webkit-transform: translateZ(0);
                    (4012: 14) transform: translateZ(0);
                    (4031: 22) -webkit-transform: translateZ(0);
                    (4032: 14) transform: translateZ(0);
                    (4048: 22) -webkit-transform: translateZ(0);
                    (4049: 14) transform: translateZ(0);
                    (4066: 22) -webkit-transform: translateZ(0);
                    (4067: 14) transform: translateZ(0);
                    (4083: 22) -webkit-transform: translateZ(0);
                    (4084: 14) transform: translateZ(0);
                    (4101: 22) -webkit-transform: translateZ(0);
                    (4102: 14) transform: translateZ(0);
                    (4118: 22) -webkit-transform: translateZ(0);
                    (4119: 14) transform: translateZ(0);
                    (4128: 22) -webkit-transform: translateY(-4px);
                    (4129: 14) transform: translateY(-4px);
                    (4136: 22) -webkit-transform: translateZ(0);
                    (4137: 14) transform: translateZ(0);
                    (4153: 22) -webkit-transform: translateZ(0);
                    (4154: 14) transform: translateZ(0);
                    (4163: 22) -webkit-transform: translateY(4px);
                    (4164: 14) transform: translateY(4px);
                    (4170: 24) -webkit-transform: translateY(-6px);
                    (4171: 16) transform: translateY(-6px);
                    (4175: 24) -webkit-transform: translateY(-2px);
                    (4176: 16) transform: translateY(-2px);
                    (4180: 24) -webkit-transform: translateY(-6px);
                    (4181: 16) transform: translateY(-6px);
                    (4187: 24) -webkit-transform: translateY(-6px);
                    (4188: 16) transform: translateY(-6px);
                    (4192: 24) -webkit-transform: translateY(-2px);
                    (4193: 16) transform: translateY(-2px);
                    (4197: 24) -webkit-transform: translateY(-6px);
                    (4198: 16) transform: translateY(-6px);
                    (4204: 24) -webkit-transform: translateY(-6px);
                    (4205: 16) transform: translateY(-6px);
                    (4211: 24) -webkit-transform: translateY(-6px);
                    (4212: 16) transform: translateY(-6px);
                    (4219: 22) -webkit-transform: translateZ(0);
                    (4220: 14) transform: translateZ(0);
                    (4236: 22) -webkit-transform: translateZ(0);
                    (4237: 14) transform: translateZ(0);
                    (4259: 24) -webkit-transform: translateY(6px);
                    (4260: 16) transform: translateY(6px);
                    (4264: 24) -webkit-transform: translateY(2px);
                    (4265: 16) transform: translateY(2px);
                    (4269: 24) -webkit-transform: translateY(6px);
                    (4270: 16) transform: translateY(6px);
                    (4276: 24) -webkit-transform: translateY(6px);
                    (4277: 16) transform: translateY(6px);
                    (4281: 24) -webkit-transform: translateY(2px);
                    (4282: 16) transform: translateY(2px);
                    (4286: 24) -webkit-transform: translateY(6px);
                    (4287: 16) transform: translateY(6px);
                    (4293: 24) -webkit-transform: translateY(6px);
                    (4294: 16) transform: translateY(6px);
                    (4300: 24) -webkit-transform: translateY(6px);
                    (4301: 16) transform: translateY(6px);
                    (4308: 22) -webkit-transform: translateZ(0);
                    (4309: 14) transform: translateZ(0);
                    (4325: 22) -webkit-transform: translateZ(0);
                    (4326: 14) transform: translateZ(0);
                    (4348: 24) -webkit-transform: translateX(6px);
                    (4349: 16) transform: translateX(6px);
                    (4353: 24) -webkit-transform: translateX(-5px);
                    (4354: 16) transform: translateX(-5px);
                    (4358: 24) -webkit-transform: translateX(4px);
                    (4359: 16) transform: translateX(4px);
                    (4363: 24) -webkit-transform: translateX(-2px);
                    (4364: 16) transform: translateX(-2px);
                    (4368: 24) -webkit-transform: translateX(1px);
                    (4369: 16) transform: translateX(1px);
                    (4373: 24) -webkit-transform: translateX(0);
                    (4374: 16) transform: translateX(0);
                    (4380: 24) -webkit-transform: translateX(6px);
                    (4381: 16) transform: translateX(6px);
                    (4385: 24) -webkit-transform: translateX(-5px);
                    (4386: 16) transform: translateX(-5px);
                    (4390: 24) -webkit-transform: translateX(4px);
                    (4391: 16) transform: translateX(4px);
                    (4395: 24) -webkit-transform: translateX(-2px);
                    (4396: 16) transform: translateX(-2px);
                    (4400: 24) -webkit-transform: translateX(1px);
                    (4401: 16) transform: translateX(1px);
                    (4405: 24) -webkit-transform: translateX(0);
                    (4406: 16) transform: translateX(0);
                    (4413: 22) -webkit-transform: translateZ(0);
                    (4414: 14) transform: translateZ(0);
                    (4430: 22) -webkit-transform: translateZ(0);
                    (4431: 14) transform: translateZ(0);
                    (4447: 24) -webkit-transform: translateY(6px);
                    (4448: 16) transform: translateY(6px);
                    (4452: 24) -webkit-transform: translateY(-5px);
                    (4453: 16) transform: translateY(-5px);
                    (4457: 24) -webkit-transform: translateY(4px);
                    (4458: 16) transform: translateY(4px);
                    (4462: 24) -webkit-transform: translateY(-2px);
                    (4463: 16) transform: translateY(-2px);
                    (4467: 24) -webkit-transform: translateY(1px);
                    (4468: 16) transform: translateY(1px);
                    (4472: 24) -webkit-transform: translateY(0);
                    (4473: 16) transform: translateY(0);
                    (4479: 24) -webkit-transform: translateY(6px);
                    (4480: 16) transform: translateY(6px);
                    (4484: 24) -webkit-transform: translateY(-5px);
                    (4485: 16) transform: translateY(-5px);
                    (4489: 24) -webkit-transform: translateY(4px);
                    (4490: 16) transform: translateY(4px);
                    (4494: 24) -webkit-transform: translateY(-2px);
                    (4495: 16) transform: translateY(-2px);
                    (4499: 24) -webkit-transform: translateY(1px);
                    (4500: 16) transform: translateY(1px);
                    (4504: 24) -webkit-transform: translateY(0);
                    (4505: 16) transform: translateY(0);
                    (4512: 22) -webkit-transform: translateZ(0);
                    (4513: 14) transform: translateZ(0);
                    (4529: 22) -webkit-transform: translateZ(0);
                    (4530: 14) transform: translateZ(0);
                    (4546: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4547: 16) transform: translateX(3px) rotate(2deg);
                    (4551: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4552: 16) transform: translateX(-3px) rotate(-2deg);
                    (4558: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4559: 16) transform: translateX(3px) rotate(2deg);
                    (4563: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4564: 16) transform: translateX(-3px) rotate(-2deg);
                    (4571: 22) -webkit-transform: translateZ(0);
                    (4572: 14) transform: translateZ(0);
                    (4588: 22) -webkit-transform: translateZ(0);
                    (4589: 14) transform: translateZ(0);
                    (4605: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4606: 16) transform: translateX(3px) rotate(2deg);
                    (4610: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4611: 16) transform: translateX(-3px) rotate(-2deg);
                    (4615: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4616: 16) transform: translateX(3px) rotate(2deg);
                    (4620: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4621: 16) transform: translateX(-3px) rotate(-2deg);
                    (4625: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (4626: 16) transform: translateX(2px) rotate(1deg);
                    (4630: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (4631: 16) transform: translateX(-2px) rotate(-1deg);
                    (4635: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (4636: 16) transform: translateX(2px) rotate(1deg);
                    (4640: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (4641: 16) transform: translateX(-2px) rotate(-1deg);
                    (4645: 24) -webkit-transform: translateX(1px) rotate(0);
                    (4646: 16) transform: translateX(1px) rotate(0);
                    (4650: 24) -webkit-transform: translateX(-1px) rotate(0);
                    (4651: 16) transform: translateX(-1px) rotate(0);
                    (4657: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4658: 16) transform: translateX(3px) rotate(2deg);
                    (4662: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4663: 16) transform: translateX(-3px) rotate(-2deg);
                    (4667: 24) -webkit-transform: translateX(3px) rotate(2deg);
                    (4668: 16) transform: translateX(3px) rotate(2deg);
                    (4672: 24) -webkit-transform: translateX(-3px) rotate(-2deg);
                    (4673: 16) transform: translateX(-3px) rotate(-2deg);
                    (4677: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (4678: 16) transform: translateX(2px) rotate(1deg);
                    (4682: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (4683: 16) transform: translateX(-2px) rotate(-1deg);
                    (4687: 24) -webkit-transform: translateX(2px) rotate(1deg);
                    (4688: 16) transform: translateX(2px) rotate(1deg);
                    (4692: 24) -webkit-transform: translateX(-2px) rotate(-1deg);
                    (4693: 16) transform: translateX(-2px) rotate(-1deg);
                    (4697: 24) -webkit-transform: translateX(1px) rotate(0);
                    (4698: 16) transform: translateX(1px) rotate(0);
                    (4702: 24) -webkit-transform: translateX(-1px) rotate(0);
                    (4703: 16) transform: translateX(-1px) rotate(0);
                    (4710: 22) -webkit-transform: translateZ(0);
                    (4711: 14) transform: translateZ(0);
                    (4727: 22) -webkit-transform: translateZ(0);
                    (4728: 14) transform: translateZ(0);
                    (4746: 22) -webkit-transform: translateZ(0);
                    (4747: 14) transform: translateZ(0);
                    (4783: 22) -webkit-transform: translateZ(0);
                    (4784: 14) transform: translateZ(0);
                    (4817: 22) -webkit-transform: translateZ(0);
                    (4818: 14) transform: translateZ(0);
                    (4851: 22) -webkit-transform: translateZ(0);
                    (4852: 14) transform: translateZ(0);
            amspApp/static/bower_components/hover/less  (1 usage found)
                _hacks.less  (1 usage found)
                    (7: 23) .prefixed(transform, translateZ(0));
            amspApp/static/bower_components/hover/less/effects/2d-transitions  (46 usages found)
                _bob.less  (4 usages found)
                    (4: 24) .prefixed(transform, translateY(-8px));
                    (7: 24) .prefixed(transform, translateY(-4px));
                    (10: 24) .prefixed(transform, translateY(-8px));
                    (16: 24) .prefixed(transform, translateY(-8px));
                _buzz-out.less  (10 usages found)
                    (4: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                    (12: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (16: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                    (20: 24) .prefixed(transform, translateX(2px) rotate(1deg));
                    (24: 24) .prefixed(transform, translateX(-2px) rotate(-1deg));
                    (28: 24) .prefixed(transform, translateX(2px) rotate(1deg));
                    (32: 24) .prefixed(transform, translateX(-2px) rotate(-1deg));
                    (36: 24) .prefixed(transform, translateX(1px) rotate(0));
                    (40: 24) .prefixed(transform, translateX(-1px) rotate(0));
                _buzz.less  (2 usages found)
                    (4: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                _float.less  (1 usage found)
                    (11: 24) .prefixed(transform, translateY(-8px));
                _hang.less  (4 usages found)
                    (4: 24) .prefixed(transform, translateY(8px));
                    (7: 24) .prefixed(transform, translateY(4px));
                    (10: 24) .prefixed(transform, translateY(8px));
                    (16: 24) .prefixed(transform, translateY(8px));
                _sink.less  (1 usage found)
                    (11: 24) .prefixed(transform, translateY(8px));
                _wobble-horizontal.less  (6 usages found)
                    (4: 24) .prefixed(transform, translateX(8px));
                    (8: 24) .prefixed(transform, translateX(-6px));
                    (12: 24) .prefixed(transform, translateX(4px));
                    (16: 24) .prefixed(transform, translateX(-2px));
                    (20: 24) .prefixed(transform, translateX(1px));
                    (24: 24) .prefixed(transform, translateX(0));
                _wobble-to-bottom-right.less  (6 usages found)
                    (4: 24) .prefixed(transform, translate(8px, 8px));
                    (8: 24) .prefixed(transform, translate(-6px, -6px));
                    (12: 24) .prefixed(transform, translate(4px, 4px));
                    (16: 24) .prefixed(transform, translate(-2px, -2px));
                    (20: 24) .prefixed(transform, translate(1px, 1px));
                    (24: 24) .prefixed(transform, translate(0, 0));
                _wobble-to-top-right.less  (6 usages found)
                    (4: 26) .prefixed(transform, translate(8px, -8px));
                    (8: 26) .prefixed(transform, translate(-6px, 6px));
                    (12: 26) .prefixed(transform, translate(4px, -4px));
                    (16: 26) .prefixed(transform, translate(-2px, 2px));
                    (20: 26) .prefixed(transform, translate(1px, -1px));
                    (24: 26) .prefixed(transform, translate(0, 0));
                _wobble-vertical.less  (6 usages found)
                    (4: 24) .prefixed(transform, translateY(8px));
                    (8: 24) .prefixed(transform, translateY(-6px));
                    (12: 24) .prefixed(transform, translateY(4px));
                    (16: 24) .prefixed(transform, translateY(-2px));
                    (20: 24) .prefixed(transform, translateY(1px));
                    (24: 24) .prefixed(transform, translateY(0));
            amspApp/static/bower_components/hover/less/effects/border-transitions  (5 usages found)
                _overline-reveal.less  (2 usages found)
                    (18: 24) .prefixed(transform, translateY(-4px));
                    (29: 25) .prefixed(transform, translateY(0));
                _reveal.less  (1 usage found)
                    (30: 25) .prefixed(transform, translateY(0));
                _underline-reveal.less  (2 usages found)
                    (18: 24) .prefixed(transform, translateY(4px));
                    (29: 25) .prefixed(transform, translateY(0));
            amspApp/static/bower_components/hover/less/effects/icons  (70 usages found)
                _icon-back.less  (2 usages found)
                    (14: 24) .prefixed(transform, translateZ(0));
                    (25: 25) .prefixed(transform, translateX(-4px));
                _icon-bob.less  (5 usages found)
                    (4: 24) .prefixed(transform, translateY(-6px));
                    (7: 24) .prefixed(transform, translateY(-2px));
                    (10: 24) .prefixed(transform, translateY(-6px));
                    (16: 24) .prefixed(transform, translateY(-6px));
                    (32: 24) .prefixed(transform, translateZ(0));
                _icon-bounce-out.less  (1 usage found)
                    (20: 24) .prefixed(transform, translateZ(0));
                _icon-bounce.less  (1 usage found)
                    (15: 24) .prefixed(transform, translateZ(0));
                _icon-buzz-out.less  (11 usages found)
                    (4: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                    (12: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (16: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                    (20: 24) .prefixed(transform, translateX(2px) rotate(1deg));
                    (24: 24) .prefixed(transform, translateX(-2px) rotate(-1deg));
                    (28: 24) .prefixed(transform, translateX(2px) rotate(1deg));
                    (32: 24) .prefixed(transform, translateX(-2px) rotate(-1deg));
                    (36: 24) .prefixed(transform, translateX(1px) rotate(0));
                    (40: 24) .prefixed(transform, translateX(-1px) rotate(0));
                    (56: 24) .prefixed(transform, translateZ(0));
                _icon-buzz.less  (3 usages found)
                    (4: 24) .prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 24) .prefixed(transform, translateX(-3px) rotate(-2deg));
                    (24: 24) .prefixed(transform, translateZ(0));
                _icon-down.less  (3 usages found)
                    (6: 24) .prefixed(transform, translateY(0));
                    (10: 24) .prefixed(transform, translateY(6px));
                    (26: 24) .prefixed(transform, translateZ(0));
                _icon-drop.less  (2 usages found)
                    (10: 24) .prefixed(transform, translateY(-100%));
                    (32: 24) .prefixed(transform, translateZ(0));
                _icon-fade.less  (1 usage found)
                    (13: 24) .prefixed(transform, translateZ(0));
                _icon-float-away.less  (1 usage found)
                    (9: 24) .prefixed(transform, translateY(-1em));
                _icon-float.less  (2 usages found)
                    (14: 24) .prefixed(transform, translateZ(0));
                    (25: 25) .prefixed(transform, translateY(-4px));
                _icon-forward.less  (2 usages found)
                    (14: 24) .prefixed(transform, translateZ(0));
                    (25: 25) .prefixed(transform, translateX(4px));
                _icon-grow-rotate.less  (1 usage found)
                    (16: 24) .prefixed(transform, translateZ(0));
                _icon-grow.less  (2 usages found)
                    (14: 24) .prefixed(transform, translateZ(0));
                    (25: 36) .prefixed(transform, scale(1.3) translateZ(0));
                _icon-hang.less  (5 usages found)
                    (4: 24) .prefixed(transform, translateY(6px));
                    (7: 24) .prefixed(transform, translateY(2px));
                    (10: 24) .prefixed(transform, translateY(6px));
                    (16: 24) .prefixed(transform, translateY(6px));
                    (32: 24) .prefixed(transform, translateZ(0));
                _icon-pop.less  (1 usage found)
                    (20: 24) .prefixed(transform, translateZ(0));
                _icon-pulse-grow.less  (1 usage found)
                    (19: 24) .prefixed(transform, translateZ(0));
                _icon-pulse-shrink.less  (1 usage found)
                    (19: 24) .prefixed(transform, translateZ(0));
                _icon-pulse.less  (1 usage found)
                    (23: 24) .prefixed(transform, translateZ(0));
                _icon-push.less  (1 usage found)
                    (20: 24) .prefixed(transform, translateZ(0));
                _icon-rotate.less  (1 usage found)
                    (16: 24) .prefixed(transform, translateZ(0));
                _icon-shrink.less  (1 usage found)
                    (14: 24) .prefixed(transform, translateZ(0));
                _icon-sink-away.less  (2 usages found)
                    (9: 24) .prefixed(transform, translateY(1em));
                    (26: 24) .prefixed(transform, translateZ(0));
                _icon-sink.less  (2 usages found)
                    (14: 24) .prefixed(transform, translateZ(0));
                    (25: 25) .prefixed(transform, translateY(4px));
                _icon-up.less  (3 usages found)
                    (6: 24) .prefixed(transform, translateY(0));
                    (10: 24) .prefixed(transform, translateY(-6px));
                    (26: 24) .prefixed(transform, translateZ(0));
                _icon-wobble-horizontal.less  (7 usages found)
                    (4: 24) .prefixed(transform, translateX(6px));
                    (8: 24) .prefixed(transform, translateX(-5px));
                    (12: 24) .prefixed(transform, translateX(4px));
                    (16: 24) .prefixed(transform, translateX(-2px));
                    (20: 24) .prefixed(transform, translateX(1px));
                    (24: 24) .prefixed(transform, translateX(0));
                    (40: 24) .prefixed(transform, translateZ(0));
                _icon-wobble-vertical.less  (7 usages found)
                    (4: 24) .prefixed(transform, translateY(6px));
                    (8: 24) .prefixed(transform, translateY(-5px));
                    (12: 24) .prefixed(transform, translateY(4px));
                    (16: 24) .prefixed(transform, translateY(-2px));
                    (20: 24) .prefixed(transform, translateY(1px));
                    (24: 24) .prefixed(transform, translateY(0));
                    (40: 24) .prefixed(transform, translateZ(0));
            amspApp/static/bower_components/hover/less/effects/shadow-and-glow-transitions  (2 usages found)
                _float-shadow.less  (2 usages found)
                    (27: 24) .prefixed(transform, translateY(-5px)); /* move the element up by 5px */
                    (31: 25) .prefixed(transform, translateY(5px)); /* move the element down by 5px (it will stay in place because it's attached to the element that also moves up 5px) */
            amspApp/static/bower_components/hover/less/effects/speech-bubbles  (12 usages found)
                _bubble-bottom.less  (1 usage found)
                    (23: 24) .prefixed(transform, translateY(@tipHeight));
                _bubble-float-bottom.less  (2 usages found)
                    (24: 24) .prefixed(transform, translateY(-(@tipHeight)));
                    (27: 25) .prefixed(transform, translateY(@tipHeight));
                _bubble-float-left.less  (2 usages found)
                    (24: 24) .prefixed(transform, translateX(@tipWidth));
                    (27: 25) .prefixed(transform, translateX(-(@tipWidth)));
                _bubble-float-right.less  (2 usages found)
                    (24: 24) .prefixed(transform, translateX(-(@tipWidth)));
                    (27: 25) .prefixed(transform, translateX(@tipWidth));
                _bubble-float-top.less  (2 usages found)
                    (24: 24) .prefixed(transform, translateY(@tipHeight));
                    (27: 25) .prefixed(transform, translateY(-(@tipHeight)));
                _bubble-left.less  (1 usage found)
                    (23: 24) .prefixed(transform, translateX(-(@tipWidth)));
                _bubble-right.less  (1 usage found)
                    (23: 24) .prefixed(transform, translateX(@tipWidth));
                _bubble-top.less  (1 usage found)
                    (23: 24) .prefixed(transform, translateY(-(@tipHeight)));
            amspApp/static/bower_components/hover/scss  (1 usage found)
                _hacks.scss  (1 usage found)
                    (7: 31) @include prefixed(transform, translateZ(0));
            amspApp/static/bower_components/hover/scss/effects/2d-transitions  (46 usages found)
                _bob.scss  (4 usages found)
                    (4: 32) @include prefixed(transform, translateY(-8px));
                    (7: 32) @include prefixed(transform, translateY(-4px));
                    (10: 32) @include prefixed(transform, translateY(-8px));
                    (16: 32) @include prefixed(transform, translateY(-8px));
                _buzz-out.scss  (10 usages found)
                    (4: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                    (12: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (16: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                    (20: 32) @include prefixed(transform, translateX(2px) rotate(1deg));
                    (24: 32) @include prefixed(transform, translateX(-2px) rotate(-1deg));
                    (28: 32) @include prefixed(transform, translateX(2px) rotate(1deg));
                    (32: 32) @include prefixed(transform, translateX(-2px) rotate(-1deg));
                    (36: 32) @include prefixed(transform, translateX(1px) rotate(0));
                    (40: 32) @include prefixed(transform, translateX(-1px) rotate(0));
                _buzz.scss  (2 usages found)
                    (4: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                _float.scss  (1 usage found)
                    (11: 32) @include prefixed(transform, translateY(-8px));
                _hang.scss  (4 usages found)
                    (4: 32) @include prefixed(transform, translateY(8px));
                    (7: 32) @include prefixed(transform, translateY(4px));
                    (10: 32) @include prefixed(transform, translateY(8px));
                    (16: 32) @include prefixed(transform, translateY(8px));
                _sink.scss  (1 usage found)
                    (11: 32) @include prefixed(transform, translateY(8px));
                _wobble-horizontal.scss  (6 usages found)
                    (4: 32) @include prefixed(transform, translateX(8px));
                    (8: 32) @include prefixed(transform, translateX(-6px));
                    (12: 32) @include prefixed(transform, translateX(4px));
                    (16: 32) @include prefixed(transform, translateX(-2px));
                    (20: 32) @include prefixed(transform, translateX(1px));
                    (24: 32) @include prefixed(transform, translateX(0));
                _wobble-to-bottom-right.scss  (6 usages found)
                    (4: 32) @include prefixed(transform, translate(8px, 8px));
                    (8: 32) @include prefixed(transform, translate(-6px, -6px));
                    (12: 32) @include prefixed(transform, translate(4px, 4px));
                    (16: 32) @include prefixed(transform, translate(-2px, -2px));
                    (20: 32) @include prefixed(transform, translate(1px, 1px));
                    (24: 32) @include prefixed(transform, translate(0, 0));
                _wobble-to-top-right.scss  (6 usages found)
                    (4: 34) @include prefixed(transform, translate(8px, -8px));
                    (8: 34) @include prefixed(transform, translate(-6px, 6px));
                    (12: 34) @include prefixed(transform, translate(4px, -4px));
                    (16: 34) @include prefixed(transform, translate(-2px, 2px));
                    (20: 34) @include prefixed(transform, translate(1px, -1px));
                    (24: 34) @include prefixed(transform, translate(0, 0));
                _wobble-vertical.scss  (6 usages found)
                    (4: 32) @include prefixed(transform, translateY(8px));
                    (8: 32) @include prefixed(transform, translateY(-6px));
                    (12: 32) @include prefixed(transform, translateY(4px));
                    (16: 32) @include prefixed(transform, translateY(-2px));
                    (20: 32) @include prefixed(transform, translateY(1px));
                    (24: 32) @include prefixed(transform, translateY(0));
            amspApp/static/bower_components/hover/scss/effects/border-transitions  (5 usages found)
                _overline-reveal.scss  (2 usages found)
                    (18: 32) @include prefixed(transform, translateY(-4px));
                    (29: 33) @include prefixed(transform, translateY(0));
                _reveal.scss  (1 usage found)
                    (30: 33) @include prefixed(transform, translateY(0));
                _underline-reveal.scss  (2 usages found)
                    (18: 32) @include prefixed(transform, translateY(4px));
                    (29: 33) @include prefixed(transform, translateY(0));
            amspApp/static/bower_components/hover/scss/effects/icons  (70 usages found)
                _icon-back.scss  (2 usages found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                    (25: 33) @include prefixed(transform, translateX(-4px));
                _icon-bob.scss  (5 usages found)
                    (4: 32) @include prefixed(transform, translateY(-6px));
                    (7: 32) @include prefixed(transform, translateY(-2px));
                    (10: 32) @include prefixed(transform, translateY(-6px));
                    (16: 32) @include prefixed(transform, translateY(-6px));
                    (32: 32) @include prefixed(transform, translateZ(0));
                _icon-bounce-out.scss  (1 usage found)
                    (20: 32) @include prefixed(transform, translateZ(0));
                _icon-bounce.scss  (1 usage found)
                    (15: 32) @include prefixed(transform, translateZ(0));
                _icon-buzz-out.scss  (11 usages found)
                    (4: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                    (12: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (16: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                    (20: 32) @include prefixed(transform, translateX(2px) rotate(1deg));
                    (24: 32) @include prefixed(transform, translateX(-2px) rotate(-1deg));
                    (28: 32) @include prefixed(transform, translateX(2px) rotate(1deg));
                    (32: 32) @include prefixed(transform, translateX(-2px) rotate(-1deg));
                    (36: 32) @include prefixed(transform, translateX(1px) rotate(0));
                    (40: 32) @include prefixed(transform, translateX(-1px) rotate(0));
                    (56: 32) @include prefixed(transform, translateZ(0));
                _icon-buzz.scss  (3 usages found)
                    (4: 32) @include prefixed(transform, translateX(3px) rotate(2deg));
                    (8: 32) @include prefixed(transform, translateX(-3px) rotate(-2deg));
                    (24: 32) @include prefixed(transform, translateZ(0));
                _icon-down.scss  (3 usages found)
                    (6: 32) @include prefixed(transform, translateY(0));
                    (10: 32) @include prefixed(transform, translateY(6px));
                    (26: 32) @include prefixed(transform, translateZ(0));
                _icon-drop.scss  (2 usages found)
                    (10: 32) @include prefixed(transform, translateY(-100%));
                    (32: 32) @include prefixed(transform, translateZ(0));
                _icon-fade.scss  (1 usage found)
                    (13: 32) @include prefixed(transform, translateZ(0));
                _icon-float-away.scss  (1 usage found)
                    (9: 32) @include prefixed(transform, translateY(-1em));
                _icon-float.scss  (2 usages found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                    (25: 33) @include prefixed(transform, translateY(-4px));
                _icon-forward.scss  (2 usages found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                    (25: 33) @include prefixed(transform, translateX(4px));
                _icon-grow-rotate.scss  (1 usage found)
                    (16: 32) @include prefixed(transform, translateZ(0));
                _icon-grow.scss  (2 usages found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                    (25: 44) @include prefixed(transform, scale(1.3) translateZ(0));
                _icon-hang.scss  (5 usages found)
                    (4: 32) @include prefixed(transform, translateY(6px));
                    (7: 32) @include prefixed(transform, translateY(2px));
                    (10: 32) @include prefixed(transform, translateY(6px));
                    (16: 32) @include prefixed(transform, translateY(6px));
                    (32: 32) @include prefixed(transform, translateZ(0));
                _icon-pop.scss  (1 usage found)
                    (20: 32) @include prefixed(transform, translateZ(0));
                _icon-pulse-grow.scss  (1 usage found)
                    (19: 32) @include prefixed(transform, translateZ(0));
                _icon-pulse-shrink.scss  (1 usage found)
                    (19: 32) @include prefixed(transform, translateZ(0));
                _icon-pulse.scss  (1 usage found)
                    (23: 32) @include prefixed(transform, translateZ(0));
                _icon-push.scss  (1 usage found)
                    (20: 32) @include prefixed(transform, translateZ(0));
                _icon-rotate.scss  (1 usage found)
                    (16: 32) @include prefixed(transform, translateZ(0));
                _icon-shrink.scss  (1 usage found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                _icon-sink-away.scss  (2 usages found)
                    (9: 32) @include prefixed(transform, translateY(1em));
                    (26: 32) @include prefixed(transform, translateZ(0));
                _icon-sink.scss  (2 usages found)
                    (14: 32) @include prefixed(transform, translateZ(0));
                    (25: 33) @include prefixed(transform, translateY(4px));
                _icon-up.scss  (3 usages found)
                    (6: 32) @include prefixed(transform, translateY(0));
                    (10: 32) @include prefixed(transform, translateY(-6px));
                    (26: 32) @include prefixed(transform, translateZ(0));
                _icon-wobble-horizontal.scss  (7 usages found)
                    (4: 32) @include prefixed(transform, translateX(6px));
                    (8: 32) @include prefixed(transform, translateX(-5px));
                    (12: 32) @include prefixed(transform, translateX(4px));
                    (16: 32) @include prefixed(transform, translateX(-2px));
                    (20: 32) @include prefixed(transform, translateX(1px));
                    (24: 32) @include prefixed(transform, translateX(0));
                    (40: 32) @include prefixed(transform, translateZ(0));
                _icon-wobble-vertical.scss  (7 usages found)
                    (4: 32) @include prefixed(transform, translateY(6px));
                    (8: 32) @include prefixed(transform, translateY(-5px));
                    (12: 32) @include prefixed(transform, translateY(4px));
                    (16: 32) @include prefixed(transform, translateY(-2px));
                    (20: 32) @include prefixed(transform, translateY(1px));
                    (24: 32) @include prefixed(transform, translateY(0));
                    (40: 32) @include prefixed(transform, translateZ(0));
            amspApp/static/bower_components/hover/scss/effects/shadow-and-glow-transitions  (2 usages found)
                _float-shadow.scss  (2 usages found)
                    (27: 32) @include prefixed(transform, translateY(-5px)); /* move the element up by 5px */
                    (31: 33) @include prefixed(transform, translateY(5px)); /* move the element down by 5px (it will stay in place because it's attached to the element that also moves up 5px) */
            amspApp/static/bower_components/hover/scss/effects/speech-bubbles  (12 usages found)
                _bubble-bottom.scss  (1 usage found)
                    (23: 32) @include prefixed(transform, translateY($tipHeight));
                _bubble-float-bottom.scss  (2 usages found)
                    (24: 32) @include prefixed(transform, translateY(-($tipHeight)));
                    (27: 33) @include prefixed(transform, translateY($tipHeight));
                _bubble-float-left.scss  (2 usages found)
                    (24: 32) @include prefixed(transform, translateX($tipWidth));
                    (27: 33) @include prefixed(transform, translateX(-($tipWidth)));
                _bubble-float-right.scss  (2 usages found)
                    (24: 32) @include prefixed(transform, translateX(-($tipWidth)));
                    (27: 33) @include prefixed(transform, translateX($tipWidth));
                _bubble-float-top.scss  (2 usages found)
                    (24: 32) @include prefixed(transform, translateY($tipHeight));
                    (27: 33) @include prefixed(transform, translateY(-($tipHeight)));
                _bubble-left.scss  (1 usage found)
                    (23: 32) @include prefixed(transform, translateX(-($tipWidth)));
                _bubble-right.scss  (1 usage found)
                    (23: 32) @include prefixed(transform, translateX($tipWidth));
                _bubble-top.scss  (1 usage found)
                    (23: 32) @include prefixed(transform, translateY(-($tipHeight)));
            amspApp/static/bower_components/input-mask-js  (5 usages found)
                inputmask.js  (5 usages found)
                    (702: 22) function translatePosition(pos) {
                    (716: 24) begin: translatePosition(begin),
                    (717: 22) end: translatePosition(end)
                    (719: 25) if (begin = translatePosition(begin), end = translatePosition(end), end = "number" == typeof end ? end : begin,
                    (719: 57) if (begin = translatePosition(begin), end = translatePosition(end), end = "number" == typeof end ? end : begin,
            amspApp/static/bower_components/myapp  (27 usages found)
                appChart.js  (27 usages found)
                    (218: 13) translateCoords = d3.transform(svgGroup.attr("transform"));
                    (220: 17) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (220: 52) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (220: 68) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (220: 91) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (220: 107) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (221: 17) translateY = translateCoords.translate[1];
                    (221: 30) translateY = translateCoords.translate[1];
                    (221: 46) translateY = translateCoords.translate[1];
                    (223: 17) translateX = translateCoords.translate[0];
                    (223: 30) translateX = translateCoords.translate[0];
                    (223: 46) translateX = translateCoords.translate[0];
                    (224: 17) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (224: 50) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (224: 66) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (224: 89) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (224: 105) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (226: 22) scaleX = translateCoords.scale[0];
                    (227: 22) scaleY = translateCoords.scale[1];
                    (229: 68) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (229: 87) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (230: 82) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (230: 101) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (232: 26) zoomListener.translate([translateX, translateY]);
                    (232: 37) zoomListener.translate([translateX, translateY]);
                    (232: 49) zoomListener.translate([translateX, translateY]);
                    (242: 60) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
            amspApp/static/bower_components/ng-file-upload-master/demo/src/main/webapp/js  (28 usages found)
                ng-file-upload-all.js  (7 usages found)
                    (663: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (712: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (718: 8) this.translateScalars = function (str) {
                    (1426: 34) return file.size >= upload.translateScalars(val);
                    (1431: 34) return file.size <= upload.translateScalars(val);
                    (1527: 26) return d <= upload.translateScalars(val);
                    (1532: 26) return d >= upload.translateScalars(val);
                ng-file-upload-all.min.js  (7 usages found)
                    (2: 10537) translateScalars
                    (2: 11420) translateScalars
                    (2: 11532) translateScalars
                    (2: 22292) translateScalars
                    (2: 22396) translateScalars
                    (2: 23461) translateScalars
                    (2: 23605) translateScalars
                ng-file-upload.js  (7 usages found)
                    (241: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (290: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (296: 8) this.translateScalars = function (str) {
                    (1004: 34) return file.size >= upload.translateScalars(val);
                    (1009: 34) return file.size <= upload.translateScalars(val);
                    (1105: 26) return d <= upload.translateScalars(val);
                    (1110: 26) return d >= upload.translateScalars(val);
                ng-file-upload.min.js  (7 usages found)
                    (2: 3372) translateScalars
                    (2: 4255) translateScalars
                    (2: 4367) translateScalars
                    (2: 15127) translateScalars
                    (2: 15231) translateScalars
                    (2: 16296) translateScalars
                    (2: 16440) translateScalars
            amspApp/static/bower_components/ng-file-upload-master/dist  (28 usages found)
                ng-file-upload-all.js  (7 usages found)
                    (663: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (712: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (718: 8) this.translateScalars = function (str) {
                    (1426: 34) return file.size >= upload.translateScalars(val);
                    (1431: 34) return file.size <= upload.translateScalars(val);
                    (1527: 26) return d <= upload.translateScalars(val);
                    (1532: 26) return d >= upload.translateScalars(val);
                ng-file-upload-all.min.js  (7 usages found)
                    (2: 10537) translateScalars
                    (2: 11420) translateScalars
                    (2: 11532) translateScalars
                    (2: 22292) translateScalars
                    (2: 22396) translateScalars
                    (2: 23461) translateScalars
                    (2: 23605) translateScalars
                ng-file-upload.js  (7 usages found)
                    (241: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (290: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (296: 8) this.translateScalars = function (str) {
                    (1004: 34) return file.size >= upload.translateScalars(val);
                    (1009: 34) return file.size <= upload.translateScalars(val);
                    (1105: 26) return d <= upload.translateScalars(val);
                    (1110: 26) return d >= upload.translateScalars(val);
                ng-file-upload.min.js  (7 usages found)
                    (2: 3372) translateScalars
                    (2: 4255) translateScalars
                    (2: 4367) translateScalars
                    (2: 15127) translateScalars
                    (2: 15231) translateScalars
                    (2: 16296) translateScalars
                    (2: 16440) translateScalars
            amspApp/static/bower_components/ng-file-upload-master/src  (7 usages found)
                upload.js  (3 usages found)
                    (241: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (290: 32) config._chunkSize = upload.translateScalars(config.resumeChunkSize);
                    (296: 8) this.translateScalars = function (str) {
                validate.js  (4 usages found)
                    (125: 34) return file.size >= upload.translateScalars(val);
                    (130: 34) return file.size <= upload.translateScalars(val);
                    (226: 26) return d <= upload.translateScalars(val);
                    (231: 26) return d >= upload.translateScalars(val);
            amspApp/static/styles  (48 usages found)
                app-blue.css  (48 usages found)
                    (6875: 24) -webkit-transform: translate(0, -25%);
                    (6876: 16) transform: translate(0, -25%);
                    (6882: 24) -webkit-transform: translate(0, 0);
                    (6883: 16) transform: translate(0, 0);
                    (7286: 28) -webkit-transform: translate3d(100%, 0, 0);
                    (7287: 20) transform: translate3d(100%, 0, 0);
                    (7293: 28) -webkit-transform: translate3d(-100%, 0, 0);
                    (7294: 20) transform: translate3d(-100%, 0, 0);
                    (7301: 28) -webkit-transform: translate3d(0, 0, 0);
                    (7302: 20) transform: translate3d(0, 0, 0);
                    (9636: 24) -webkit-transform: translateZ(0);
                    (9637: 16) transform: translateZ(0);
                    (10609: 24) -webkit-transform: translateX(-50%);
                    (10610: 16) transform: translateX(-50%);
                    (10615: 24) -webkit-transform: translateY(-100%);
                    (10616: 16) transform: translateY(-100%);
                    (10637: 24) -webkit-transform: translateX(-50%);
                    (10638: 16) transform: translateX(-50%);
                    (10643: 24) -webkit-transform: translateY(-100%);
                    (10644: 16) transform: translateY(-100%);
                    (10667: 24) -webkit-transform: translateX(-50%);
                    (10668: 16) transform: translateX(-50%);
                    (10682: 24) -webkit-transform: translateY(-100%);
                    (10683: 16) transform: translateY(-100%);
                    (10699: 24) -webkit-transform: translateX(-50%);
                    (10700: 16) transform: translateX(-50%);
                    (10714: 24) -webkit-transform: translateY(-100%);
                    (10715: 16) transform: translateY(-100%);
                    (10819: 39) -webkit-transform: rotateX(90deg) translateZ(10px);
                    (10820: 31) transform: rotateX(90deg) translateZ(10px);
                    (10840: 40) -webkit-transform: rotateX(-90deg) translateZ(10px);
                    (10841: 32) transform: rotateX(-90deg) translateZ(10px);
                    (10864: 24) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (10864: 55) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (10865: 16) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (10865: 47) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (10888: 24) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (10888: 57) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (10889: 16) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (10889: 49) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (10971: 24) -webkit-transform: translateY(10px);
                    (10972: 16) transform: translateY(10px);
                    (11001: 24) -webkit-transform: translateY(-10px);
                    (11002: 16) transform: translateY(-10px);
                    (11271: 24) -webkit-transform: translate3d(0, 0, 0);
                    (11272: 16) transform: translate3d(0, 0, 0);
                    (11277: 24) -webkit-transform: translate3d(0, 0, 0);
                    (11278: 16) transform: translate3d(0, 0, 0);
            amspApp/static/styles/layout/topnav  (2 usages found)
                topnav.less  (2 usages found)
                    (241: 22) -webkit-transform: translateZ(0);
                    (242: 14) transform: translateZ(0);
            amspApp/static/styles/less  (5 usages found)
                carousel.less  (3 usages found)
                    (36: 10) .translate3d(100%, 0, 0);
                    (41: 10) .translate3d(-100%, 0, 0);
                    (47: 10) .translate3d(0, 0, 0);
                modals.less  (2 usages found)
                    (33: 6) .translate(0, -25%);
                    (36: 25) &.in .modal-dialog { .translate(0, 0) }
            amspApp/static/styles/less/mixins  (8 usages found)
                vendor-prefixes.less  (8 usages found)
                    (142: 2) .translate(@x; @y) {
                    (143: 22) -webkit-transform: translate(@x, @y);
                    (144: 22) -ms-transform: translate(@x, @y); // IE9 only
                    (145: 22) -o-transform: translate(@x, @y);
                    (146: 22) transform: translate(@x, @y);
                    (148: 2) .translate3d(@x; @y; @z) {
                    (149: 22) -webkit-transform: translate3d(@x, @y, @z);
                    (150: 22) transform: translate3d(@x, @y, @z);
            amspApp/static/styles/transitions  (6 usages found)
                pages.less  (6 usages found)
                    (47: 21) -webkit-transform:translate3d(0, 0, 0);
                    (48: 18) -moz-transform:translate3d(0, 0, 0);
                    (49: 13) transform:translate3d(0, 0, 0);
                    (54: 21) -webkit-transform:translate3d(0, 0, 0);
                    (55: 18) -moz-transform:translate3d(0, 0, 0);
                    (56: 13) transform:translate3d(0, 0, 0);
            amspApp/static/styles/widgets  (36 usages found)
                progressButton.less  (32 usages found)
                    (150: 21) -webkit-transform: translateX(-50%);
                    (151: 13) transform: translateX(-50%);
                    (156: 21) -webkit-transform: translateY(-100%);
                    (157: 13) transform: translateY(-100%);
                    (180: 21) -webkit-transform: translateX(-50%);
                    (181: 13) transform: translateX(-50%);
                    (186: 21) -webkit-transform: translateY(-100%);
                    (187: 13) transform: translateY(-100%);
                    (211: 21) -webkit-transform: translateX(-50%);
                    (212: 13) transform: translateX(-50%);
                    (226: 21) -webkit-transform: translateY(-100%);
                    (227: 13) transform: translateY(-100%);
                    (245: 21) -webkit-transform: translateX(-50%);
                    (246: 13) transform: translateX(-50%);
                    (260: 21) -webkit-transform: translateY(-100%);
                    (261: 13) transform: translateY(-100%);
                    (366: 36) -webkit-transform: rotateX(90deg) translateZ(10px);
                    (367: 28) transform: rotateX(90deg) translateZ(10px);
                    (388: 37) -webkit-transform: rotateX(-90deg) translateZ(10px);
                    (389: 29) transform: rotateX(-90deg) translateZ(10px);
                    (413: 21) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (413: 52) -webkit-transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (414: 13) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (414: 44) transform: translateX(50%) rotateY(90deg) translateZ(10px);
                    (438: 21) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (438: 54) -webkit-transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (439: 13) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (439: 46) transform: translateX(-50%) rotateY(-90deg) translateZ(10px);
                    (525: 21) -webkit-transform: translateY(10px);
                    (526: 13) transform: translateY(10px);
                    (556: 21) -webkit-transform: translateY(-10px);
                    (557: 13) transform: translateY(-10px);
                smart-button.less  (4 usages found)
                    (28: 20) transform: translateY(100%);
                    (37: 20) transform: translateY(-100%);
                    (69: 28) transform: translateY(-100%);
                    (75: 28) transform: translateY(100%);
            templates/authentication  (10 usages found)
                forget.html  (2 usages found)
                    (23: 23) | translate //
                    (28: 25) translate //
                login.html  (4 usages found)
                    (32: 44) 'rememberme' | translate //</label>
                    (43: 39) >// 'login' | translate //
                    (48: 25) translate //
                    (54: 48) //'iforgetmypassword'| translate //
                resetpass.html  (2 usages found)
                    (29: 23) | translate //
                    (34: 25) translate //
                signup.html  (2 usages found)
                    (99: 23) | translate //
                    (104: 25) translate //
            templates/companyManagement  (99 usages found)
                __CompanyMembers.html  (1 usage found)
                    (10: 33) //'users' | translate//
                ChartEdit.html  (29 usages found)
                    (20: 34) // 'chartedit' | translate //
                    (53: 35) // 'ChartZones' | translate //
                    (394: 33) translateCoords = d3.transform(svgGroup.attr("transform"));
                    (396: 37) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (396: 72) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (396: 88) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (396: 111) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (396: 127) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (397: 37) translateY = translateCoords.translate[1];
                    (397: 50) translateY = translateCoords.translate[1];
                    (397: 66) translateY = translateCoords.translate[1];
                    (399: 37) translateX = translateCoords.translate[0];
                    (399: 50) translateX = translateCoords.translate[0];
                    (399: 66) translateX = translateCoords.translate[0];
                    (400: 37) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (400: 70) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (400: 86) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (400: 109) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (400: 125) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (402: 42) scaleX = translateCoords.scale[0];
                    (403: 42) scaleY = translateCoords.scale[1];
                    (405: 88) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (405: 107) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (406: 102) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (406: 121) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (408: 46) zoomListener.translate([translateX, translateY]);
                    (408: 57) zoomListener.translate([translateX, translateY]);
                    (408: 69) zoomListener.translate([translateX, translateY]);
                    (418: 80) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                CompaniesManagment.html  (2 usages found)
                    (329: 42) // 'total' | translate //://Companies.count//
                    (350: 42) // 'total' | translate //://Companies.count//
                CompanyChart.html  (37 usages found)
                    (10: 31) //'chart'|translate//
                    (29: 38) // 'chartedit' | translate //
                    (63: 51) // 'Secratrait Permissions' | translate //
                    (77: 46) <th>//'Name'|translate//</th>
                    (78: 49) <th>//'Default'|translate//</th>
                    (79: 48) <th>//'Access'|translate//</th>
                    (80: 48) <th>//'Export'|translate//</th>
                    (81: 48) <th>//'Import'|translate//</th>
                    (107: 88) <td colspan="5">//"Please select a chart item to edit"|translate//</td>
                    (122: 39) // 'ChartZones' | translate //
                    (484: 33) translateCoords = d3.transform(svgGroup.attr("transform"));
                    (486: 37) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (486: 72) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (486: 88) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (486: 111) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (486: 127) translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                    (487: 37) translateY = translateCoords.translate[1];
                    (487: 50) translateY = translateCoords.translate[1];
                    (487: 66) translateY = translateCoords.translate[1];
                    (489: 37) translateX = translateCoords.translate[0];
                    (489: 50) translateX = translateCoords.translate[0];
                    (489: 66) translateX = translateCoords.translate[0];
                    (490: 37) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (490: 70) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (490: 86) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (490: 109) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (490: 125) translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
                    (492: 42) scaleX = translateCoords.scale[0];
                    (493: 42) scaleY = translateCoords.scale[1];
                    (495: 88) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (495: 107) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (496: 102) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (496: 121) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (498: 46) zoomListener.translate([translateX, translateY]);
                    (498: 57) zoomListener.translate([translateX, translateY]);
                    (498: 69) zoomListener.translate([translateX, translateY]);
                    (508: 80) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                CompanyManagement.html  (1 usage found)
                    (4: 39) //'Companies Managment' | translate//
                CompanyProducts.html  (7 usages found)
                    (8: 39) //'productionslist' | translate //
                    (25: 40) // 'registeredcount' | translate //://Productions.count//
                    (26: 87) // 'inthefollowinglistonly15itemsarevisibleyoucanseeothersbypaging' | translate //
                    (101: 52) // 'add_edit_company_production' | translate //
                    (112: 76) <label for="titleOfProduction">//'titleofproduction' | translate //</label>
                    (126: 61) <label>//'productionLogo' | translate //</label>
                    (137: 64) <label>//'productiondetails' | translate //</label>
                CompanyProfile.html  (2 usages found)
                    (45: 76) <h3 class="panel-title">//'briefcompanyintroduction' | translate//
                    (62: 72) <h3 class="panel-title"> //'companyintroduction' | translate//
                CopySecretarait.html  (9 usages found)
                    (15: 52) <td rowspan="2">//'Name' | translate//</td>
                    (16: 64) <td colspan="3">//'Numbering Format' | translate//</td>
                    (17: 62) <td colspan="3">//'Latest Numbers' | translate//</td>
                    (21: 42) <td>//'Inside' | translate//</td>
                    (22: 43) <td>//'Exports' | translate//</td>
                    (23: 43) <td>//'Imports' | translate//</td>
                    (24: 42) <td>//'Inside' | translate//</td>
                    (25: 43) <td>//'Exports' | translate//</td>
                    (26: 43) <td>//'Imports' | translate//</td>
                Members.html  (1 usage found)
                    (24: 47) //'has no person'|translate //
                Secretarait.html  (10 usages found)
                    (7: 51) <th rowspan="2">//'Secratrait Name' | translate//</th>
                    (8: 43) <th colspan="3">//'Formats' | translate//</th>
                    (9: 50) <th colspan="3">//'Latest Numbers' | translate//</th>
                    (13: 32) <th>//'Internal' | translate//</th>
                    (14: 30) <th>//'Export' | translate//</th>
                    (15: 30) <th>//'Import' | translate//</th>
                    (16: 32) <th>//'Internae' | translate//</th>
                    (17: 30) <th>//'Export' | translate//</th>
                    (18: 30) <th>//'Import' | translate//</th>
                    (46: 101) <button class="btn btn-primary" ng-click="addDabir(DabirkhanehList)"> //'Add New' | translate//
            templates/friends  (8 usages found)
                friends.html  (8 usages found)
                    (7: 51) //'Find Friends or Members' | translate//
                    (77: 71) <small><a ng-click="CloseInvModal()">(//'Close' | translate//)</a>
                    (92: 60) <h3><strong>//'All Charts'|translate//</strong></h3>
                    (93: 61) <small>//'Select to invite'|translate//</small>
                    (111: 84) <h3 ng-if="chart.isEmpty">//'Empty Position' | translate//</h3>
                    (118: 48) <h3>//'Invitation'|translate//</h3>
                    (119: 70) <small>//'See selected user invitations'|translate//</small>
                    (126: 127) //inv.chartName// <span ng-if="inv.isEmpty" style="font-weight: bold">(//'Empty Position'|translate//)</span>
            templates/generic-templates  (11 usages found)
                CompanyCharts.html  (1 usage found)
                    (5: 20) <strong>//'Charts'|translate//</strong>
                selectPositions.html  (1 usage found)
                    (10: 41) //'persons'|translate//
                Table.html  (9 usages found)
                    (10: 76) <h3 class="panel-title inline">// '{{ gt_table_title }}' | translate //
                    (32: 64) // 'all{{ gt_object_name }}' | translate // : // totalItemsCount // &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
                    (34: 55) // 'resaultfounded' | translate // : // foundedItemsCount //
                    (40: 70) <small style="color: #000000">//'from' | translate // // itemsFrom // // 'to' | translate //
                    (40: 109) <small style="color: #000000">//'from' | translate // // itemsFrom // // 'to' | translate //
                    (53: 57) <th>// '{{ data_title }}' | translate //</th>
                    (55: 49) <th>// 'itemsperpage' | translate //&nbsp;&nbsp;
                    (97: 17) translate // // itemsFrom // // 'to' | translate // //itemsTo//
                    (97: 56) translate // // itemsFrom // // 'to' | translate // //itemsTo//
            templates/letter  (12 usages found)
                InboxCompose.html  (5 usages found)
                    (5: 60) <div class="mail-header"><h4>//'newLetter'|translate//</h4></div>
                    (6: 67) <div class="receipient"><strong class="to">//'to'|translate// </strong>
                    (7: 131) &nbsp;&nbsp;&nbsp;<span class="btn btn-default btn-sm" ng-if="!(selectedPositions)" ng-click="selectPositions()">//'selectPerson'|translate//</span>
                    (11: 80) <div class="subject"><strong class="strong-header">//'subject'|translate//</strong> <strong
                    (18: 50) //'DropImageorPDFsfileshere'|translate//</p>
                InboxSidebar.html  (7 usages found)
                    (7: 56) <h3 class="modal-title">//'labelModal'|translate//</h3>
                    (11: 44) <label>//'backgroundColor'|translate//
                    (13: 38) <label>//'textColor'|translate//
                    (28: 56) <h3 class="modal-title">//'GroupModal'|translate//</h3>
                    (33: 34) <div>//'members'|translate//
                    (39: 39) //'justjoint'|translate//</label>
                    (86: 30) <h6>//'labels' | translate//</h6>
            templates/myProfile  (34 usages found)
                PersonProfile.html  (33 usages found)
                    (51: 68) <h3 class="panel-title">//'About me' | translate//
                    (78: 81) <div class="col-md-6 profile-detail"><p>//'gender:'|translate//</p></div>
                    (79: 79) <div class="col-md-6 profile-detail"><p>//'home:'|translate//</p></div>
                    (80: 80) <div class="col-md-6 profile-detail"><p>//'birth:'|translate//</p></div>
                    (81: 83) <div class="col-md-6 profile-detail"><p>//'religion:'|translate//</p></div>
                    (82: 83) <div class="col-md-6 profile-detail"><p>//'interests'|translate//</p></div>
                    (83: 81) <div class="col-md-6 profile-detail"><p>//'career:'|translate//</p></div>
                    (84: 83) <div class="col-md-6 profile-detail"><p>//'hometown:'|translate//</p></div>
                    (85: 87) <div class="col-md-6 profile-detail"><p>//'relationship:'|translate//</p></div>
                    (86: 80) <div class="col-md-6 profile-detail"><p>//'sport:'|translate//</p></div>
                    (87: 84) <div class="col-md-6 profile-detail"><p>//'something:'|translate//</p></div>
                    (105: 85) <div class="col-md-6 profile-detail"><p>//'postalcode:'|translate //</p></div>
                    (106: 87) <div class="col-md-6 profile-detail"><p>//'personalSite:'|translate //</p></div>
                    (107: 83) <div class="col-md-6 profile-detail"><p>//'homeAdrr:'|translate //</p></div>
                    (108: 85) <div class="col-md-6 profile-detail"><p>//'officeAddr:'|translate //</p></div>
                    (164: 51) <th>//'level'|translate//</th>
                    (165: 51) <th>//'major'|translate//</th>
                    (166: 50) <th>//'year'|translate//</th>
                    (167: 53) <th>//'average'|translate//</th>
                    (214: 57) <th>//'courseTitle'|translate//</th>
                    (215: 55) <th>//'institute'|translate//</th>
                    (216: 62) <th>//'certificateTitle'|translate//</th>
                    (217: 50) <th>//'year'|translate//</th>
                    (267: 51) <th>//'Title'|translate//</th>
                    (268: 51) <th>//'level'|translate//</th>
                    (269: 55) <th>//'exprience'|translate//</th>
                    (315: 50) <th>//'Lang'|translate//</th>
                    (316: 51) <th>//'level'|translate//</th>
                    (317: 56) <th>//'experience'|translate//</th>
                    (366: 55) <th>//'workTitle'|translate//</th>
                    (367: 53) <th>//'company'|translate//</th>
                    (368: 50) <th>//'time'|translate//</th>
                    (369: 52) <th>//'salary'|translate//</th>
                Posts.html  (1 usage found)
                    (10: 46) //"jointosystemat" | translate //
            templates/others  (1 usage found)
                newbpmn.html  (1 usage found)
                    (10: 31) //'New Process' | translate//
            templates/others/sidebar  (23 usages found)
                sidebar.html  (23 usages found)
                    (12: 33) translate //</a></li>
                    (20: 68) <li class="sidemenu-header">// 'ams' | translate //</li>
                    (22: 49) 'inboxLetter' | translate //</a></li>
                    (24: 49) 'secretariat' | translate //</a></li>
                    (32: 69) <li class="sidemenu-header">// 'bpms' | translate //</li>
                    (34: 48) 'inboxTasks' | translate //</a></li>
                    (36: 33) translate //</a></li>
                    (38: 50) 'tasksArchive' | translate //</a></li>
                    (40: 35) | translate //</a></li>
                    (76: 70) <li class="sidemenu-header">// 'tools' | translate //</li>
                    (79: 51) 'smartCalendar' | translate //</a></li>
                    (81: 33) translate //</a></li>
                    (83: 33) translate //</a></li>
                    (85: 48) 'myContacts' | translate //</a></li>
                    (93: 73) <li class="sidemenu-header">// 'settings' | translate //</li>
                    (96: 33) translate //</a></li>
                    (98: 51) 'importMailBox' | translate //</a></li>
                    (100: 48) 'changePass' | translate //</a></li>
                    (108: 111) <li><a ng-class="{active: $state.includes('users')}" ui-sref="users">// 'users' | translate
                    (111: 33) translate //</a></li>
                    (149: 58) <div class="feed-header">// 'tips' | translate //</div>
                    (153: 55) <a href="">// 'li1' | translate //</a> <span class="feed-date">25/4/2015</span>
                    (157: 55) <a href="">// 'li4' | translate //</a> <span class="feed-date">25/4/2015</span>
            templates/others/top-nav  (4 usages found)
                topnav.html  (4 usages found)
                    (10: 64) <a class="navbar-brand" ui-sref="home"> // 'AmsPlus' | translate //</a>
                    (145: 44) <span>// 'languages' | translate//</span>
                    (191: 62) <li><a ui-sref="profile"> // 'profile' | translate //</a></li>
                    (193: 92) <a href="javascript:void(0)" ng-click="vm.logout()"> // 'logout' | translate //</a></li>
    Usage in comments  (509 usages found)
        amsPlus  (509 usages found)
            amspApp/static/angularThings/others/fitlers  (1 usage found)
                moment.js  (1 usage found)
                    (399: 29) // It is impossible translate months into days without knowing
            amspApp/static/bower_components/angular  (3 usages found)
                angular.js  (3 usages found)
                    (6805: 12) // translate normalized key to actual key
                    (8341: 21)  *          reverse-translated using the {@link ng.$compile.directive.Attributes#$attr $attr}
                    (18698: 59)  * roundtrip apps, it is desirable for the browser not to translate the form submission into a full
            amspApp/static/bower_components/angular-translate  (392 usages found)
                angular-translate.js  (389 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
                    (24: 23)  * @name pascalprecht.translate
                    (43: 11) // $translate.use() will also remember the language.
                    (68: 23)  * @name pascalprecht.translate.$translateSanitizationProvider
                    (68: 34)  * @name pascalprecht.translate.$translateSanitizationProvider
                    (72: 24)  * Configurations for $translateSanitization
                    (97: 31)    * @propertyOf pascalprecht.translate.$translateSanitizationProvider
                    (97: 42)    * @propertyOf pascalprecht.translate.$translateSanitizationProvider
                    (148: 25)    * @name pascalprecht.translate.$translateSanitizationProvider#addStrategy
                    (148: 36)    * @name pascalprecht.translate.$translateSanitizationProvider#addStrategy
                    (149: 29)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (149: 40)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (165: 25)    * @name pascalprecht.translate.$translateSanitizationProvider#removeStrategy
                    (165: 36)    * @name pascalprecht.translate.$translateSanitizationProvider#removeStrategy
                    (166: 29)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (166: 40)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (181: 25)    * @name pascalprecht.translate.$translateSanitizationProvider#useStrategy
                    (181: 36)    * @name pascalprecht.translate.$translateSanitizationProvider#useStrategy
                    (182: 29)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (182: 40)    * @methodOf pascalprecht.translate.$translateSanitizationProvider
                    (198: 25)    * @name pascalprecht.translate.$translateSanitization
                    (198: 36)    * @name pascalprecht.translate.$translateSanitization
                    (203: 45)    * Sanitizes interpolation parameters and translated texts.
                    (236: 29)        * @name pascalprecht.translate.$translateSanitization#useStrategy
                    (236: 40)        * @name pascalprecht.translate.$translateSanitization#useStrategy
                    (237: 33)        * @methodOf pascalprecht.translate.$translateSanitization
                    (237: 44)        * @methodOf pascalprecht.translate.$translateSanitization
                    (252: 29)        * @name pascalprecht.translate.$translateSanitization#sanitize
                    (252: 40)        * @name pascalprecht.translate.$translateSanitization#sanitize
                    (253: 33)        * @methodOf pascalprecht.translate.$translateSanitization
                    (253: 44)        * @methodOf pascalprecht.translate.$translateSanitization
                    (314: 23)  * @name pascalprecht.translate.$translateProvider
                    (314: 34)  * @name pascalprecht.translate.$translateProvider
                    (317: 5)  * $translateProvider allows developers to register translation-tables, asynchronous loaders
                    (500: 25)    * @name pascalprecht.translate.$translateProvider#translations
                    (500: 36)    * @name pascalprecht.translate.$translateProvider#translations
                    (501: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (501: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (511: 8)    *  $translateProvider.translations('de_DE', {
                    (516: 8)    *  $translateProvider.translations('en_US', {
                    (557: 25)    * @name pascalprecht.translate.$translateProvider#cloakClassName
                    (557: 36)    * @name pascalprecht.translate.$translateProvider#cloakClassName
                    (558: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (558: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (562: 43)    * Let's you change the class name for `translate-cloak` directive.
                    (563: 29)    * Default class name is `translate-cloak`.
                    (565: 27)    * @param {string} name translate-cloak class name
                    (616: 25)    * @name pascalprecht.translate.$translateProvider#addInterpolation
                    (616: 36)    * @name pascalprecht.translate.$translateProvider#addInterpolation
                    (617: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (617: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (620: 45)    * Adds interpolation services to angular-translate, so it can manage them.
                    (631: 25)    * @name pascalprecht.translate.$translateProvider#useMessageFormatInterpolation
                    (631: 36)    * @name pascalprecht.translate.$translateProvider#useMessageFormatInterpolation
                    (632: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (632: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (635: 20)    * Tells angular-translate to use interpolation functionality of messageformat.js.
                    (644: 25)    * @name pascalprecht.translate.$translateProvider#useInterpolation
                    (644: 36)    * @name pascalprecht.translate.$translateProvider#useInterpolation
                    (645: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (645: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (648: 20)    * Tells angular-translate which interpolation style to use as default, application-wide.
                    (661: 25)    * @name pascalprecht.translate.$translateProvider#useSanitizeStrategy
                    (661: 36)    * @name pascalprecht.translate.$translateProvider#useSanitizeStrategy
                    (662: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (662: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (676: 25)    * @name pascalprecht.translate.$translateProvider#preferredLanguage
                    (676: 36)    * @name pascalprecht.translate.$translateProvider#preferredLanguage
                    (677: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (677: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (681: 65)    * at initial startup by passing a language key. Similar to `$translateProvider#use`
                    (700: 25)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicator
                    (700: 36)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicator
                    (701: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (701: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (705: 52)    * setting the indicator as 'X' and one tries to translate a translation id
                    (709: 8)    * `$translateProvider.translationNotFoundIndicatorLeft()` and
                    (710: 8)    * `$translateProvider.translationNotFoundIndicatorRight()`.
                    (725: 25)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicatorLeft
                    (725: 36)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicatorLeft
                    (726: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (726: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (744: 25)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicatorLeft
                    (744: 36)    * @name pascalprecht.translate.$translateProvider#translationNotFoundIndicatorLeft
                    (745: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (745: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (763: 25)    * @name pascalprecht.translate.$translateProvider#fallbackLanguage
                    (763: 36)    * @name pascalprecht.translate.$translateProvider#fallbackLanguage
                    (764: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (764: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (768: 65)    * at initial startup by passing a language key. Similar to `$translateProvider#use`
                    (804: 25)    * @name pascalprecht.translate.$translateProvider#use
                    (804: 36)    * @name pascalprecht.translate.$translateProvider#use
                    (805: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (805: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (811: 57)    * You actually don't have to use this method since `$translateProvider#preferredLanguage`
                    (830: 25)    * @name pascalprecht.translate.$translateProvider#storageKey
                    (830: 36)    * @name pascalprecht.translate.$translateProvider#storageKey
                    (831: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (831: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (853: 25)    * @name pascalprecht.translate.$translateProvider#useUrlLoader
                    (853: 36)    * @name pascalprecht.translate.$translateProvider#useUrlLoader
                    (854: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (854: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (857: 20)    * Tells angular-translate to use `$translateUrlLoader` extension service as loader.
                    (857: 39)    * Tells angular-translate to use `$translateUrlLoader` extension service as loader.
                    (868: 25)    * @name pascalprecht.translate.$translateProvider#useStaticFilesLoader
                    (868: 36)    * @name pascalprecht.translate.$translateProvider#useStaticFilesLoader
                    (869: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (869: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (872: 20)    * Tells angular-translate to use `$translateStaticFilesLoader` extension service as loader.
                    (872: 39)    * Tells angular-translate to use `$translateStaticFilesLoader` extension service as loader.
                    (882: 25)    * @name pascalprecht.translate.$translateProvider#useLoader
                    (882: 36)    * @name pascalprecht.translate.$translateProvider#useLoader
                    (883: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (883: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (886: 20)    * Tells angular-translate to use any other service as loader.
                    (899: 25)    * @name pascalprecht.translate.$translateProvider#useLocalStorage
                    (899: 36)    * @name pascalprecht.translate.$translateProvider#useLocalStorage
                    (900: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (900: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (903: 20)    * Tells angular-translate to use `$translateLocalStorage` service as storage layer.
                    (903: 39)    * Tells angular-translate to use `$translateLocalStorage` service as storage layer.
                    (912: 25)    * @name pascalprecht.translate.$translateProvider#useCookieStorage
                    (912: 36)    * @name pascalprecht.translate.$translateProvider#useCookieStorage
                    (913: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (913: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (916: 20)    * Tells angular-translate to use `$translateCookieStorage` service as storage layer.
                    (916: 39)    * Tells angular-translate to use `$translateCookieStorage` service as storage layer.
                    (924: 25)    * @name pascalprecht.translate.$translateProvider#useStorage
                    (924: 36)    * @name pascalprecht.translate.$translateProvider#useStorage
                    (925: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (925: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (928: 20)    * Tells angular-translate to use custom service as storage layer.
                    (937: 25)    * @name pascalprecht.translate.$translateProvider#storagePrefix
                    (937: 36)    * @name pascalprecht.translate.$translateProvider#storagePrefix
                    (938: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (938: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (955: 25)    * @name pascalprecht.translate.$translateProvider#useMissingTranslationHandlerLog
                    (955: 36)    * @name pascalprecht.translate.$translateProvider#useMissingTranslationHandlerLog
                    (956: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (956: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (959: 20)    * Tells angular-translate to use built-in log handler when trying to translate
                    (959: 73)    * Tells angular-translate to use built-in log handler when trying to translate
                    (971: 25)    * @name pascalprecht.translate.$translateProvider#useMissingTranslationHandler
                    (971: 36)    * @name pascalprecht.translate.$translateProvider#useMissingTranslationHandler
                    (972: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (972: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (976: 46)    * This method can be used to tell angular-translate to use a custom
                    (982: 29)    *  app.config(function ($translateProvider) {
                    (983: 10)    *    $translateProvider.useMissingTranslationHandler('customHandler');
                    (1002: 25)    * @name pascalprecht.translate.$translateProvider#usePostCompiling
                    (1002: 36)    * @name pascalprecht.translate.$translateProvider#usePostCompiling
                    (1003: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1003: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1006: 40)    * If post compiling is enabled, all translated values will be processed
                    (1011: 29)    *  app.config(function ($translateProvider) {
                    (1012: 10)    *    $translateProvider.usePostCompiling(true);
                    (1025: 25)    * @name pascalprecht.translate.$translateProvider#forceAsyncReload
                    (1025: 36)    * @name pascalprecht.translate.$translateProvider#forceAsyncReload
                    (1026: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1026: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1035: 29)    *  app.config(function ($translateProvider) {
                    (1036: 10)    *    $translateProvider.forceAsyncReload(true);
                    (1049: 25)    * @name pascalprecht.translate.$translateProvider#uniformLanguageTag
                    (1049: 36)    * @name pascalprecht.translate.$translateProvider#uniformLanguageTag
                    (1050: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1050: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1053: 20)    * Tells angular-translate which language tag should be used as a result when determining
                    (1056: 67)    * This setting must be set before invoking {@link pascalprecht.translate.$translateProvider#methods_determinePreferredLanguage determinePreferredLanguage()}.
                    (1056: 78)    * This setting must be set before invoking {@link pascalprecht.translate.$translateProvider#methods_determinePreferredLanguage determinePreferredLanguage()}.
                    (1059: 7)    * $translateProvider
                    (1105: 25)    * @name pascalprecht.translate.$translateProvider#determinePreferredLanguage
                    (1105: 36)    * @name pascalprecht.translate.$translateProvider#determinePreferredLanguage
                    (1106: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1106: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1109: 20)    * Tells angular-translate to try to determine on its own which language key
                    (1110: 64)    * to set as preferred language. When `fn` is given, angular-translate uses it
                    (1118: 38)    * locale (see {@link pascalprecht.translate.$translateProvider#methods_uniformLanguageTag uniformLanguageTag()}).
                    (1118: 49)    * locale (see {@link pascalprecht.translate.$translateProvider#methods_uniformLanguageTag uniformLanguageTag()}).
                    (1137: 25)    * @name pascalprecht.translate.$translateProvider#registerAvailableLanguageKeys
                    (1137: 36)    * @name pascalprecht.translate.$translateProvider#registerAvailableLanguageKeys
                    (1138: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1138: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1143: 26)    * {@link pascalprecht.translate.$translateProvider#determinePreferredLanguage determinePreferredLanguage}.
                    (1143: 37)    * {@link pascalprecht.translate.$translateProvider#determinePreferredLanguage determinePreferredLanguage}.
                    (1144: 60)    * When available languages keys are registered, angular-translate
                    (1164: 25)    * @name pascalprecht.translate.$translateProvider#useLoaderCache
                    (1164: 36)    * @name pascalprecht.translate.$translateProvider#useLoaderCache
                    (1165: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1165: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1169: 26)    * {@link pascalprecht.translate.$translateProvider#determinePreferredLanguage determinePreferredLanguage}.
                    (1169: 37)    * {@link pascalprecht.translate.$translateProvider#determinePreferredLanguage determinePreferredLanguage}.
                    (1195: 25)    * @name pascalprecht.translate.$translateProvider#directivePriority
                    (1195: 36)    * @name pascalprecht.translate.$translateProvider#directivePriority
                    (1196: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1196: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1199: 39)    * Sets the default priority of the translate directive. The standard value is `0`.
                    (1202: 39)    * @param {number} priority for the translate-directive
                    (1217: 25)    * @name pascalprecht.translate.$translateProvider#statefulFilter
                    (1217: 36)    * @name pascalprecht.translate.$translateProvider#statefulFilter
                    (1218: 29)    * @methodOf pascalprecht.translate.$translateProvider
                    (1218: 40)    * @methodOf pascalprecht.translate.$translateProvider
                    (1223: 23)    * Sets whether the translate filter should be stateful or stateless. The standard value is `true`
                    (1242: 25)    * @name pascalprecht.translate.$translate
                    (1242: 36)    * @name pascalprecht.translate.$translate
                    (1249: 12)    * The `$translate` service is the actual core of angular-translate. It expects a translation id
                    (1249: 61)    * The `$translate` service is the actual core of angular-translate. It expects a translation id
                    (1250: 45)    * and optional interpolate parameters to translate contents.
                    (1253: 8)    *  $translate('HEADLINE_TEXT').then(function (translation) {
                    (1254: 16)    *    $scope.translatedText = translation;
                    (1356: 26) // We can just translate.
                    (1501: 11) // $translateProvider.addInterpolation(), we have to map'em
                    (1552: 41)        * @param langKey The language to translate to.
                    (1591: 41)        * @param langKey The language to translate to.
                    (1614: 16)        * @name translateByHandler
                    (1617: 10)        * Translate by missing translation handler.
                    (1705: 10)        * Translates with the usage of the fallback languages.
                    (1718: 10)        * Translates with the usage of the fallback languages.
                    (1741: 36) // If using link, rerun $translate with linked translationId and return it
                    (1751: 48) // for logging purposes only (as in $translateMissingTranslationHandlerLog), value is not returned to promise
                    (1756: 32) // since we couldn't translate the inital requested translation id,
                    (1800: 36) // If using link, rerun $translate with linked translationId and return it
                    (1808: 48) // for logging purposes only (as in $translateMissingTranslationHandlerLog), value is not returned to promise
                    (1813: 32) // since we couldn't translate the inital requested translation id,
                    (1841: 29)        * @name pascalprecht.translate.$translate#preferredLanguage
                    (1841: 40)        * @name pascalprecht.translate.$translate#preferredLanguage
                    (1842: 33)        * @methodOf pascalprecht.translate.$translate
                    (1842: 44)        * @methodOf pascalprecht.translate.$translate
                    (1860: 29)        * @name pascalprecht.translate.$translate#cloakClassName
                    (1860: 40)        * @name pascalprecht.translate.$translate#cloakClassName
                    (1861: 33)        * @methodOf pascalprecht.translate.$translate
                    (1861: 44)        * @methodOf pascalprecht.translate.$translate
                    (1864: 49)        * Returns the configured class name for `translate-cloak` directive.
                    (1874: 29)        * @name pascalprecht.translate.$translate#fallbackLanguage
                    (1874: 40)        * @name pascalprecht.translate.$translate#fallbackLanguage
                    (1875: 33)        * @methodOf pascalprecht.translate.$translate
                    (1875: 44)        * @methodOf pascalprecht.translate.$translate
                    (1911: 29)        * @name pascalprecht.translate.$translate#useFallbackLanguage
                    (1911: 40)        * @name pascalprecht.translate.$translate#useFallbackLanguage
                    (1912: 33)        * @methodOf pascalprecht.translate.$translate
                    (1912: 44)        * @methodOf pascalprecht.translate.$translate
                    (1938: 29)        * @name pascalprecht.translate.$translate#proposedLanguage
                    (1938: 40)        * @name pascalprecht.translate.$translate#proposedLanguage
                    (1939: 33)        * @methodOf pascalprecht.translate.$translate
                    (1939: 44)        * @methodOf pascalprecht.translate.$translate
                    (1952: 29)        * @name pascalprecht.translate.$translate#storage
                    (1952: 40)        * @name pascalprecht.translate.$translate#storage
                    (1953: 33)        * @methodOf pascalprecht.translate.$translate
                    (1953: 44)        * @methodOf pascalprecht.translate.$translate
                    (1966: 29)        * @name pascalprecht.translate.$translate#use
                    (1966: 40)        * @name pascalprecht.translate.$translate#use
                    (1967: 33)        * @methodOf pascalprecht.translate.$translate
                    (1967: 44)        * @methodOf pascalprecht.translate.$translate
                    (1970: 24)        * Tells angular-translate which language to use by given language key. This method is
                    (1979: 11)        * $translate.use("en_US").then(function(data){
                    (1980: 27)        *   $scope.text = $translate("HELLO");
                    (2039: 29)        * @name pascalprecht.translate.$translate#storageKey
                    (2039: 40)        * @name pascalprecht.translate.$translate#storageKey
                    (2040: 33)        * @methodOf pascalprecht.translate.$translate
                    (2040: 44)        * @methodOf pascalprecht.translate.$translate
                    (2053: 29)        * @name pascalprecht.translate.$translate#isPostCompilingEnabled
                    (2053: 40)        * @name pascalprecht.translate.$translate#isPostCompilingEnabled
                    (2054: 33)        * @methodOf pascalprecht.translate.$translate
                    (2054: 44)        * @methodOf pascalprecht.translate.$translate
                    (2067: 29)        * @name pascalprecht.translate.$translate#isForceAsyncReloadEnabled
                    (2067: 40)        * @name pascalprecht.translate.$translate#isForceAsyncReloadEnabled
                    (2068: 33)        * @methodOf pascalprecht.translate.$translate
                    (2068: 44)        * @methodOf pascalprecht.translate.$translate
                    (2081: 29)        * @name pascalprecht.translate.$translate#refresh
                    (2081: 40)        * @name pascalprecht.translate.$translate#refresh
                    (2082: 33)        * @methodOf pascalprecht.translate.$translate
                    (2082: 44)        * @methodOf pascalprecht.translate.$translate
                    (2094: 11)        * $translateRefreshStart and $translateRefreshEnd events.
                    (2094: 38)        * $translateRefreshStart and $translateRefreshEnd events.
                    (2099: 11)        * $translate.refresh();
                    (2101: 11)        * $translate.refresh('en_US');
                    (2179: 29)        * @name pascalprecht.translate.$translate#instant
                    (2179: 40)        * @name pascalprecht.translate.$translate#instant
                    (2180: 33)        * @methodOf pascalprecht.translate.$translate
                    (2180: 44)        * @methodOf pascalprecht.translate.$translate
                    (2261: 29)        * @name pascalprecht.translate.$translate#versionInfo
                    (2261: 40)        * @name pascalprecht.translate.$translate#versionInfo
                    (2262: 33)        * @methodOf pascalprecht.translate.$translate
                    (2262: 44)        * @methodOf pascalprecht.translate.$translate
                    (2265: 66)        * Returns the current version information for the angular-translate library
                    (2267: 35)        * @return {string} angular-translate version
                    (2275: 29)        * @name pascalprecht.translate.$translate#loaderCache
                    (2275: 40)        * @name pascalprecht.translate.$translate#loaderCache
                    (2276: 33)        * @methodOf pascalprecht.translate.$translate
                    (2276: 44)        * @methodOf pascalprecht.translate.$translate
                    (2332: 23)  * @name pascalprecht.translate.$translateDefaultInterpolation
                    (2332: 34)  * @name pascalprecht.translate.$translateDefaultInterpolation
                    (2341: 26)  * * {@link pascalprecht.translate.$translateSanitization}
                    (2341: 37)  * * {@link pascalprecht.translate.$translateSanitization}
                    (2343: 22)  * @return {object} $translateDefaultInterpolation Interpolator service
                    (2357: 25)    * @name pascalprecht.translate.$translateDefaultInterpolation#setLocale
                    (2357: 36)    * @name pascalprecht.translate.$translateDefaultInterpolation#setLocale
                    (2358: 29)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2358: 40)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2371: 25)    * @name pascalprecht.translate.$translateDefaultInterpolation#getInterpolationIdentifier
                    (2371: 36)    * @name pascalprecht.translate.$translateDefaultInterpolation#getInterpolationIdentifier
                    (2372: 29)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2372: 40)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2385: 31)    * @see {@link pascalprecht.translate.$translateSanitization}
                    (2385: 42)    * @see {@link pascalprecht.translate.$translateSanitization}
                    (2394: 25)    * @name pascalprecht.translate.$translateDefaultInterpolation#interpolate
                    (2394: 36)    * @name pascalprecht.translate.$translateDefaultInterpolation#interpolate
                    (2395: 29)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2395: 40)    * @methodOf pascalprecht.translate.$translateDefaultInterpolation
                    (2424: 23)  * @name pascalprecht.translate.directive:translate
                    (2424: 43)  * @name pascalprecht.translate.directive:translate
                    (2431: 4)  * Translates given translation id either through attribute or DOM content.
                    (2432: 24)  * Internally it uses `translate` filter to translate translation id. It possible to
                    (2432: 45)  * Internally it uses `translate` filter to translate translation id. It possible to
                    (2433: 22)  * pass an optional `translate-values` object literal as string into translation id.
                    (2435: 21)  * @param {string=} translate Translation id which could be either string or interpolated string.
                    (2436: 21)  * @param {string=} translate-values Values to pass into translation id. Can be passed as object literal string or interpolated object.
                    (2437: 21)  * @param {string=} translate-attr-ATTR translate Translation id and put it into ATTR attribute.
                    (2437: 41)  * @param {string=} translate-attr-ATTR translate Translation id and put it into ATTR attribute.
                    (2438: 21)  * @param {string=} translate-default will be used unless translation was successful
                    (2439: 22)  * @param {boolean=} translate-compile (default true if present) defines locally activation of {@link pascalprecht.translate.$translateProvider#methods_usePostCompiling}
                    (2439: 116)  * @param {boolean=} translate-compile (default true if present) defines locally activation of {@link pascalprecht.translate.$translateProvider#methods_usePostCompiling}
                    (2439: 127)  * @param {boolean=} translate-compile (default true if present) defines locally activation of {@link pascalprecht.translate.$translateProvider#methods_usePostCompiling}
                    (2444: 27)       <div ng-controller="TranslateCtrl">
                    (2446: 14)         <pre translate="TRANSLATION_ID"></pre>
                    (2447: 14)         <pre translate>TRANSLATION_ID</pre>
                    (2448: 14)         <pre translate translate-attr-title="TRANSLATION_ID"></pre>
                    (2448: 24)         <pre translate translate-attr-title="TRANSLATION_ID"></pre>
                    (2449: 14)         <pre translate="{{translationId}}"></pre>
                    (2450: 14)         <pre translate>{{translationId}}</pre>
                    (2451: 14)         <pre translate="WITH_VALUES" translate-values="{value: 5}"></pre>
                    (2451: 38)         <pre translate="WITH_VALUES" translate-values="{value: 5}"></pre>
                    (2452: 14)         <pre translate translate-values="{value: 5}">WITH_VALUES</pre>
                    (2452: 24)         <pre translate translate-values="{value: 5}">WITH_VALUES</pre>
                    (2453: 14)         <pre translate="WITH_VALUES" translate-values="{{values}}"></pre>
                    (2453: 38)         <pre translate="WITH_VALUES" translate-values="{{values}}"></pre>
                    (2454: 14)         <pre translate translate-values="{{values}}">WITH_VALUES</pre>
                    (2454: 24)         <pre translate translate-values="{{values}}">WITH_VALUES</pre>
                    (2455: 14)         <pre translate translate-attr-title="WITH_VALUES" translate-values="{{values}}"></pre>
                    (2455: 24)         <pre translate translate-attr-title="WITH_VALUES" translate-values="{{values}}"></pre>
                    (2455: 59)         <pre translate translate-attr-title="WITH_VALUES" translate-values="{{values}}"></pre>
                    (2460: 47)       angular.module('ngView', ['pascalprecht.translate'])
                    (2462: 26)       .config(function ($translateProvider) {
                    (2464: 10)         $translateProvider.translations('en',{
                    (2471: 44)       angular.module('ngView').controller('TranslateCtrl', function ($scope) {
                    (2480: 18)       it('should translate', function () {
                    (2484: 34)           element = $compile('<p translate="TRANSLATION_ID"></p>')($rootScope);
                    (2488: 34)           element = $compile('<p translate="{{translationId}}"></p>')($rootScope);
                    (2492: 34)           element = $compile('<p translate>TRANSLATION_ID</p>')($rootScope);
                    (2496: 34)           element = $compile('<p translate>{{translationId}}</p>')($rootScope);
                    (2500: 34)           element = $compile('<p translate translate-attr-title="TRANSLATION_ID"></p>')($rootScope);
                    (2500: 44)           element = $compile('<p translate translate-attr-title="TRANSLATION_ID"></p>')($rootScope);
                    (2566: 49) // Ensures any change of the attribute "translate" containing the id will
                    (2614: 34) // case of element "<translate>xyz</translate>"
                    (2614: 49) // case of element "<translate>xyz</translate>"
                    (2680: 45) // as an empty string cannot be translated, we can solve this using successful=false
                    (2687: 24) // default translate into innerHTML
                    (2699: 16) // translate attribute
                    (2718: 16) // w/ $translate.use(...)
                    (2745: 23)  * @name pascalprecht.translate.directive:translateCloak
                    (2745: 43)  * @name pascalprecht.translate.directive:translateCloak
                    (2747: 15)  * @requires $translate
                    (2751: 12)  * Adds a `translate-cloak` class name to the given element where this directive
                    (2758: 24)  * {@link pascalprecht.translate.$translateProvider#cloakClassName $translate.cloakClassName()}.
                    (2758: 35)  * {@link pascalprecht.translate.$translateProvider#cloakClassName $translate.cloakClassName()}.
                    (2758: 69)  * {@link pascalprecht.translate.$translateProvider#cloakClassName $translate.cloakClassName()}.
                    (2760: 21)  * @param {string=} translate-cloak If a translationId is provided, it will be used for showing
                    (2803: 23)  * @name pascalprecht.translate.filter:translate
                    (2803: 40)  * @name pascalprecht.translate.filter:translate
                    (2805: 27)  * @requires pascalprecht.translate.$translate
                    (2805: 38)  * @requires pascalprecht.translate.$translate
                    (2809: 11)  * Uses `$translate` service to translate contents. Accepts interpolate parameters
                    (2809: 33)  * Uses `$translate` service to translate contents. Accepts interpolate parameters
                    (2812: 57)  * @param {string} translationId A translation id to be translated.
                    (2815: 22)  * @returns {string} Translated text.
                    (2820: 27)       <div ng-controller="TranslateCtrl">
                    (2822: 36)         <pre>{{ 'TRANSLATION_ID' | translate }}</pre>
                    (2823: 33)         <pre>{{ translationId | translate }}</pre>
                    (2824: 33)         <pre>{{ 'WITH_VALUES' | translate:'{value: 5}' }}</pre>
                    (2825: 33)         <pre>{{ 'WITH_VALUES' | translate:values }}</pre>
                    (2830: 47)       angular.module('ngView', ['pascalprecht.translate'])
                    (2832: 26)       .config(function ($translateProvider) {
                    (2834: 10)         $translateProvider.translations('en', {
                    (2838: 10)         $translateProvider.preferredLanguage('en');
                    (2842: 44)       angular.module('ngView').controller('TranslateCtrl', function ($scope) {
                    (2881: 23)  * @name pascalprecht.translate.$translationCache
                angular-translate.min.js  (3 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
            amspApp/static/bower_components/angular-translate-loader-static-files  (8 usages found)
                angular-translate-loader-static-files.js  (5 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
                    (25: 23)  * @name pascalprecht.translate.$translateStaticFilesLoader
                    (25: 34)  * @name pascalprecht.translate.$translateStaticFilesLoader
                angular-translate-loader-static-files.min.js  (3 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
            amspApp/static/bower_components/angular-translate-loader-url  (8 usages found)
                angular-translate-loader-url.js  (5 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
                    (25: 23)  * @name pascalprecht.translate.$translateUrlLoader
                    (25: 34)  * @name pascalprecht.translate.$translateUrlLoader
                angular-translate-loader-url.min.js  (3 usages found)
                    (2: 12)  * angular-translate - v2.7.2 - 2015-06-01
                    (3: 30)  * http://github.com/angular-translate/angular-translate
                    (3: 48)  * http://github.com/angular-translate/angular-translate
            amspApp/static/bower_components/bpmn-modeler  (21 usages found)
                BpmnViewer.js  (7 usages found)
                    (18260: 19)          * Matrix.translate
                    (18263: 12)          * Translate the matrix
                    (21948: 11)  * @class TranslatePlugin
                    (21950: 36)  * Extends snapsvg with methods to translate elements
                    (21955: 30)    * @method snapsvg.Element#translate
                    (21959: 8)    * e.translate(10, 20);
                    (21961: 34)    * // sets transform matrix to translate(10, 20)
                BpmnViewerApp.js  (7 usages found)
                    (18592: 19)          * Matrix.translate
                    (18595: 12)          * Translate the matrix
                    (22280: 11)  * @class TranslatePlugin
                    (22282: 36)  * Extends snapsvg with methods to translate elements
                    (22287: 30)    * @method snapsvg.Element#translate
                    (22291: 8)    * e.translate(10, 20);
                    (22293: 34)    * // sets transform matrix to translate(10, 20)
                index.js  (7 usages found)
                    (35215: 31)                      * Matrix.translate
                    (35218: 24)                      * Translate the matrix
                    (38958: 19)          * @class TranslatePlugin
                    (38960: 44)          * Extends snapsvg with methods to translate elements
                    (38965: 40)              * @method snapsvg.Element#translate
                    (38969: 18)              * e.translate(10, 20);
                    (38971: 44)              * // sets transform matrix to translate(10, 20)
            amspApp/static/bower_components/bpmn-modeler/vendor  (7 usages found)
                disttt2.js  (7 usages found)
                    (18599: 19)          * Matrix.translate
                    (18602: 12)          * Translate the matrix
                    (22287: 11)  * @class TranslatePlugin
                    (22289: 36)  * Extends snapsvg with methods to translate elements
                    (22294: 30)    * @method snapsvg.Element#translate
                    (22298: 8)    * e.translate(10, 20);
                    (22300: 34)    * // sets transform matrix to translate(10, 20)
            amspApp/static/bower_components/c3  (2 usages found)
                c3.js  (2 usages found)
                    (3836: 18) // MEMO: translate will be upated by this, so transform not needed in updateLegend()
                    (6677: 26) // 2. ceil values of translate/x/y to int for half pixel antialiasing
            amspApp/static/bower_components/ckeditor/full/plugins/notificationaggregator  (1 usage found)
                plugin.js  (1 usage found)
                    (122: 63) 		 * "Translating widgets (2 of 3)" if more widgets are being translated at the same
            amspApp/static/bower_components/ckeditor/full/plugins/widget/dev/assets/simplebox  (1 usage found)
                plugin.js  (1 usage found)
                    (58: 36) // Note: In order to be able to translate your widget you should use the
            amspApp/static/bower_components/fullcalendar  (3 usages found)
                fullcalendar.js  (3 usages found)
                    (4822: 40) // For determining how a given "cell" translates into a "date":
                    (5049: 8) // translate to cells
                    (5058: 12) // can translate to multiple days, and an edge case reveals itself when we the
            amspApp/static/bower_components/jalalijscalendar/lang  (36 usages found)
                calendar-bg.js  (1 usage found)
                    (83: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-big5-utf8.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-big5.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-br.js  (1 usage found)
                    (62: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ca.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-cs-utf8.js  (1 usage found)
                    (32: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-cs-win.js  (1 usage found)
                    (32: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-da.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-de.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this ;-)
                calendar-el.js  (1 usage found)
                    (56: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-en.js  (1 usage found)
                    (118: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-es.js  (1 usage found)
                    (88: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-fa.js  (2 usages found)
                    (117: 68) "Copyright (c) 2008 Ali Farhadi (http://farhadi.ir/)\n" + // don't translate this this ;-)
                    (121: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-fi.js  (1 usage found)
                    (66: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-fr.js  (1 usage found)
                    (84: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-he-utf8.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-hu.js  (1 usage found)
                    (83: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-it.js  (1 usage found)
                    (83: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ko-utf8.js  (1 usage found)
                    (85: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ko.js  (1 usage found)
                    (85: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-lt-utf8.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-lt.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-lv.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-no.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-pl-utf8.js  (1 usage found)
                    (60: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-pl.js  (1 usage found)
                    (24: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-pt.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ro.js  (1 usage found)
                    (33: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ru.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-ru_win_.js  (1 usage found)
                    (82: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-si.js  (1 usage found)
                    (62: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-sp.js  (1 usage found)
                    (69: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-sv.js  (1 usage found)
                    (61: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                calendar-zh.js  (1 usage found)
                    (78: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
                cn_utf8.js  (1 usage found)
                    (83: 64) "(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" + // don't translate this this ;-)
            amspApp/static/bower_components/jquery-ui/ui  (3 usages found)
                jquery-ui.custom.js  (1 usage found)
                    (13675: 5) // Translates a [top,left] array into a baseline value
                jquery-ui.js  (1 usage found)
                    (8068: 5) // Translates a [top,left] array into a baseline value
                jquery.ui.effect.js  (1 usage found)
                    (933: 5) // Translates a [top,left] array into a baseline value
            amspApp/static/bower_components/jquery-ui/ui/i18n  (4 usages found)
                jquery-ui-i18n.js  (2 usages found)
                    (573: 4) /* Translated by Jorge Barreiro <yortx.barry@gmail.com>. */
                    (1449: 4) /* Translated by Le Thanh Huy (lthanhhuy@cit.ctu.edu.vn). */
                jquery.ui.datepicker-gl.js  (1 usage found)
                    (2: 4) /* Translated by Jorge Barreiro <yortx.barry@gmail.com>. */
                jquery.ui.datepicker-vi.js  (1 usage found)
                    (2: 4) /* Translated by Le Thanh Huy (lthanhhuy@cit.ctu.edu.vn). */
            amspApp/static/bower_components/Scroll  (3 usages found)
                jquery.mCustomScrollbar.js  (3 usages found)
                    (181: 64) 				the reported mouse-wheel delta value. The number of lines (translated to pixels) one wheel notch scrolls.
                    (627: 10) /* translate yx values to actual scroll-to positions */
                    (1801: 6) /* translates values (e.g. "top", 100, "100px", "#id") to actual scroll-to positions */
            amspApp/static/bower_components/Scroll/js/uncompressed  (3 usages found)
                jquery.mCustomScrollbar.js  (3 usages found)
                    (181: 64) 				the reported mouse-wheel delta value. The number of lines (translated to pixels) one wheel notch scrolls.
                    (627: 10) /* translate yx values to actual scroll-to positions */
                    (1801: 6) /* translates values (e.g. "top", 100, "100px", "#id") to actual scroll-to positions */
            amspApp/static/bower_components/ui-router/release  (2 usages found)
                angular-ui-router.js  (2 usages found)
                    (4338: 4)  * Translates to {@link ui.router.state.$state#methods_is $state.is("stateName")}.
                    (4356: 4)  * Translates to {@link ui.router.state.$state#methods_includes $state.includes('fullOrPartialStateName')}.
            amspApp/static/bower_components/ui-router/src  (2 usages found)
                stateFilters.js  (2 usages found)
                    (8: 4)  * Translates to {@link ui.router.state.$state#methods_is $state.is("stateName")}.
                    (26: 4)  * Translates to {@link ui.router.state.$state#methods_includes $state.includes('fullOrPartialStateName')}.
            templates/others/sidebar  (9 usages found)
                sidebar.html  (9 usages found)
                    (50: 62) {#                                // 'Companies Managment' | translate //#}
                    (52: 95) {#                                   ui-sref="profileCompanyManagement">// 'profileCompany' | translate //</a><#}
                    (56: 123) {#                                   ui-sref="profileCompanyManagement">// 'profileCompany' | translate //</a></li>#}
                    (58: 73) {#                                'chart' | translate //</a></li>#}
                    (60: 109) {#                                   ui-sref="membersManagement">// 'members' | translate //</a></li>#}
                    (62: 85) {#                                'businessProcesses' | translate //</a></li>#}
                    (64: 119) {#                                   ui-sref="secretariatsManagement">// 'secretariats' | translate //</a></li>#}
                    (66: 113) {#                                   ui-sref="documentsManagement">// 'documents' | translate //</a></li>#}
                    (68: 74) {#                                'hiring' | translate //</a></li>#}
    Usage in string constants  (379 usages found)
        amsPlus  (379 usages found)
            amspApp/static/angularThings  (1 usage found)
                app.js  (1 usage found)
                    (29: 23) 'pascalprecht.translate',
            amspApp/static/angularThings/others/extras  (1 usage found)
                map.min.js  (1 usage found)
                    (733: 69) this.rootElement.node.setAttribute('transform', 'scale('+scale+') translate('+transX+', '+transY+')');
            amspApp/static/bower_components  (2 usages found)
                masonry.js  (2 usages found)
                    (9: 14418) translate
                    (9: 14453) translate
            amspApp/static/bower_components/angular-growl/build  (2 usages found)
                angular-growl.js  (1 usage found)
                    (115: 30) translate = $filter('translate');
                angular-growl.min.js  (1 usage found)
                    (6: 2417) translate
            amspApp/static/bower_components/angular-translate  (157 usages found)
                .bower.json  (5 usages found)
                    (2: 20) "name": "angular-translate",
                    (5: 22) "main": "./angular-translate.js",
                    (17: 62) "homepage": "https://github.com/PascalPrecht/bower-angular-translate",
                    (24: 59) "_source": "git://github.com/PascalPrecht/bower-angular-translate.git",
                    (26: 31) "_originalSource": "angular-translate"
                angular-translate.js  (75 usages found)
                    (29: 30) angular.module('pascalprecht.translate', ['ng'])
                    (62: 27) runTranslate.$inject = ['$translate'];
                    (64: 32) runTranslate.displayName = 'runTranslate';
                    (74: 30) angular.module('pascalprecht.translate').provider('$translateSanitization', $translateSanitizationProvider);
                    (74: 53) angular.module('pascalprecht.translate').provider('$translateSanitization', $translateSanitizationProvider);
                    (215: 41) throw new Error('pascalprecht.translate.$translateSanitization: Unknown sanitization strategy: \'' + selectedStrategy + '\'');
                    (215: 52) throw new Error('pascalprecht.translate.$translateSanitization: Unknown sanitization strategy: \'' + selectedStrategy + '\'');
                    (224: 33) translate
                    (224: 44) $translateSanitization
                    (224: 177) translate
                    (290: 37) translate
                    (290: 48) $translateSanitization
                    (321: 30) angular.module('pascalprecht.translate')
                    (322: 24) .constant('pascalprechtTranslateOverrider', {})
                    (323: 13) .provider('$translate', $translate);
                    (344: 26) $cloakClassName = 'translate-cloak',
                    (406: 50) getFirstBrowserLanguage.displayName = 'angular-translate/service: getFirstBrowserLanguage';
                    (416: 36) getLocale.displayName = 'angular-translate/service: getLocale';
                    (639: 36) return this.useInterpolation('$translateMessageFormatInterpolation');
                    (820: 27) throw new Error('$translateProvider couldn\'t find translationTable for langKey: \'' + langKey + '\'');
                    (863: 29) return this.useLoader('$translateUrlLoader', angular.extend({ url: url }, options));
                    (877: 29) return this.useLoader('$translateStaticFilesLoader', options);
                    (907: 30) return this.useStorage('$translateLocalStorage');
                    (919: 30) return this.useStorage('$translateCookieStorage');
                    (966: 48) return this.useMissingTranslationHandler('$translateMissingTranslationHandlerLog');
                    (1274: 74) defaultInterpolator = $injector.get($interpolationFactory || '$translateDefaultInterpolation'),
                    (1406: 28) $rootScope.$emit('$translateChangeSuccess', {language: key});
                    (1421: 28) $rootScope.$emit('$translateChangeEnd', {language: key});
                    (1443: 28) $rootScope.$emit('$translateLoadingStart', {language: key});
                    (1461: 30) $rootScope.$emit('$translateLoadingSuccess', {language: key});
                    (1475: 30) $rootScope.$emit('$translateLoadingEnd', {language: key});
                    (1480: 30) $rootScope.$emit('$translateLoadingError', {language: key});
                    (1482: 30) $rootScope.$emit('$translateLoadingEnd', {language: key});
                    (1993: 28) $rootScope.$emit('$translateChangeStart', {language: key});
                    (2011: 32) $rootScope.$emit('$translateChangeError', {language: key});
                    (2013: 32) $rootScope.$emit('$translateChangeEnd', {language: key});
                    (2117: 30) $rootScope.$emit('$translateRefreshEnd', {language: langKey});
                    (2122: 30) $rootScope.$emit('$translateRefreshEnd', {language: langKey});
                    (2125: 28) $rootScope.$emit('$translateRefreshStart', {language: langKey});
                    (2310: 32) $rootScope.$emit('$translateChangeEnd', { language: translation.key });
                    (2326: 60) $translate.$inject = ['$STORAGE_KEY', '$windowProvider', '$translateSanitizationProvider', 'pascalprechtTranslateOverrider'];
                    (2326: 105) $translate.$inject = ['$STORAGE_KEY', '$windowProvider', '$translateSanitizationProvider', 'pascalprechtTranslateOverrider'];
                    (2345: 30) angular.module('pascalprecht.translate').factory('$translateDefaultInterpolation', $translateDefaultInterpolation);
                    (2345: 52) angular.module('pascalprecht.translate').factory('$translateDefaultInterpolation', $translateDefaultInterpolation);
                    (2415: 61) $translateDefaultInterpolation.$inject = ['$interpolate', '$translateSanitization'];
                    (2417: 48) $translateDefaultInterpolation.displayName = '$translateDefaultInterpolation';
                    (2419: 30) angular.module('pascalprecht.translate').constant('$STORAGE_KEY', 'NG_TRANSLATE_LANG_KEY');
                    (2419: 71) angular.module('pascalprecht.translate').constant('$STORAGE_KEY', 'NG_TRANSLATE_LANG_KEY');
                    (2421: 30) angular.module('pascalprecht.translate')
                    (2508: 13) .directive('translate', translateDirective);
                    (2538: 62) var translateValueExist = tElement[0].outerHTML.match(/translate-value-+/i);
                    (2558: 96) if (Object.prototype.hasOwnProperty.call(iAttr, attr) && attr.substr(0, 14) === 'translateValue' && attr !== 'translateValues') {
                    (2558: 125) if (Object.prototype.hasOwnProperty.call(iAttr, attr) && attr.substr(0, 14) === 'translateValue' && attr !== 'translateValues') {
                    (2612: 25) iAttr.$observe('translate', function (translationId) {
                    (2627: 87) if (iAttr.hasOwnProperty(translateAttr) && translateAttr.substr(0, 13) === 'translateAttr') {
                    (2632: 25) iAttr.$observe('translateDefault', function (value) {
                    (2637: 27) iAttr.$observe('translateValues', function (interpolateParams) {
                    (2654: 94) if (Object.prototype.hasOwnProperty.call(iAttr, attr) && attr.substr(0, 14) === 'translateValue' && attr !== 'translateValues') {
                    (2654: 123) if (Object.prototype.hasOwnProperty.call(iAttr, attr) && attr.substr(0, 14) === 'translateValue' && attr !== 'translateValues') {
                    (2686: 34) if (translateAttr === 'translate') {
                    (2719: 39) var unbind = $rootScope.$on('$translateChangeSuccess', updateTranslations);
                    (2738: 33) translateDirective.$inject = ['$translate', '$q', '$interpolate', '$compile', '$parse', '$rootScope'];
                    (2740: 35) translateDirective.displayName = 'translateDirective';
                    (2742: 30) angular.module('pascalprecht.translate')
                    (2764: 13) .directive('translateCloak', translateCloakDirective);
                    (2778: 41) removeListener = $rootScope.$on('$translateChangeEnd', function () {
                    (2788: 27) iAttr.$observe('translateCloak', function (translationId) {
                    (2796: 52) translateCloakDirective.$inject = ['$rootScope', '$translate'];
                    (2798: 40) translateCloakDirective.displayName = 'translateCloakDirective';
                    (2800: 30) angular.module('pascalprecht.translate')
                    (2852: 10) .filter('translate', translateFilterFactory);
                    (2873: 47) translateFilterFactory.$inject = ['$parse', '$translate'];
                    (2875: 39) translateFilterFactory.displayName = 'translateFilterFactory';
                    (2877: 30) angular.module('pascalprecht.translate')
                    (2902: 22) return 'pascalprecht.translate';
                angular-translate.min.js  (75 usages found)
                    (6: 1146) translate
                    (6: 1157) $translateSanitization
                    (6: 1280) translate
                    (6: 1291) $translateSanitization
                    (6: 1424) translate
                    (6: 1866) translate
                    (6: 1877) $translateSanitization
                    (6: 2368) translate
                    (6: 3117) translate
                    (6: 3243) translate
                    (6: 4533) $translateMessageFormatInterpolation
                    (6: 5333) $translateProvider
                    (6: 5552) $translateUrlLoader
                    (6: 5662) $translateStaticFilesLoader
                    (6: 5805) $translateLocalStorage
                    (6: 5888) $translateCookieStorage
                    (6: 6104) $translateMissingTranslationHandlerLog
                    (6: 6962) $translateDefaultInterpolation
                    (6: 7746) $translateChangeSuccess
                    (6: 7941) $translateChangeEnd
                    (6: 8068) $translateLoadingStart
                    (6: 8262) $translateLoadingSuccess
                    (6: 8440) $translateLoadingEnd
                    (6: 8536) $translateLoadingError
                    (6: 8595) $translateLoadingEnd
                    (6: 11462) $translateChangeStart
                    (6: 11784) $translateChangeError
                    (6: 11842) $translateChangeEnd
                    (6: 12125) $translateRefreshEnd
                    (6: 12194) $translateRefreshEnd
                    (6: 12341) $translateRefreshStart
                    (6: 13532) $translateChangeEnd
                    (6: 14295) translate
                    (6: 14660) translateValue
                    (6: 14695) translateValues
                    (6: 15337) translate
                    (6: 15463) translateAttr
                    (6: 15516) translateDefault
                    (6: 15579) translateValues
                    (6: 15881) translateValue
                    (6: 15916) translateValues
                    (6: 16186) translate
                    (6: 16653) $translateChangeSuccess
                    (6: 16944) $translateChangeEnd
                    (6: 17074) translateCloak
                    (6: 17368) translate
                    (6: 17407) $translate
                    (6: 17437) runTranslate
                    (6: 17477) translate
                    (6: 17500) $translateSanitization
                    (6: 17555) translate
                    (6: 17589) pascalprechtTranslateOverrider
                    (6: 17624) $translate
                    (6: 17684) $translateSanitizationProvider
                    (6: 17728) pascalprechtTranslateOverrider
                    (6: 17806) translate
                    (6: 17828) $translateDefaultInterpolation
                    (6: 17890) $translateSanitization
                    (6: 17930) $translateDefaultInterpolation
                    (6: 17990) translate
                    (6: 18030) NG_TRANSLATE_LANG_KEY
                    (6: 18080) translate
                    (6: 18103) translate
                    (6: 18130) $translate
                    (6: 18210) translateDirective
                    (6: 18259) translate
                    (6: 18282) translateCloak
                    (6: 18327) $translate
                    (6: 18354) translateCloakDirective
                    (6: 18408) translate
                    (6: 18428) translate
                    (6: 18464) $translate
                    (6: 18491) translateFilterFactory
                    (6: 18544) translate
                    (6: 18663) translate
                bower.json  (2 usages found)
                    (2: 20) "name": "angular-translate",
                    (5: 22) "main": "./angular-translate.js",
            amspApp/static/bower_components/angular-translate-loader-static-files  (19 usages found)
                .bower.json  (7 usages found)
                    (2: 20) "name": "angular-translate-loader-static-files",
                    (3: 40) "description": "A plugin for Angular Translate",
                    (5: 22) "main": "./angular-translate-loader-static-files.js",
                    (7: 14) "angular-translate": "~2.7.2"
                    (17: 62) "homepage": "https://github.com/PascalPrecht/bower-angular-translate-loader-static-files",
                    (24: 59) "_source": "git://github.com/PascalPrecht/bower-angular-translate-loader-static-files.git",
                    (26: 31) "_originalSource": "angular-translate-loader-static-files"
                angular-translate-loader-static-files.js  (4 usages found)
                    (22: 30) angular.module('pascalprecht.translate')
                    (36: 12) .factory('$translateStaticFilesLoader', $translateStaticFilesLoader);
                    (111: 45) $translateStaticFilesLoader.displayName = '$translateStaticFilesLoader';
                    (112: 22) return 'pascalprecht.translate';
                angular-translate-loader-static-files.min.js  (4 usages found)
                    (6: 1100) translate
                    (6: 1122) $translateStaticFilesLoader
                    (6: 1194) $translateStaticFilesLoader
                    (6: 1236) translate
                bower.json  (4 usages found)
                    (2: 20) "name": "angular-translate-loader-static-files",
                    (3: 40) "description": "A plugin for Angular Translate",
                    (5: 22) "main": "./angular-translate-loader-static-files.js",
                    (7: 14) "angular-translate": "~2.7.2"
            amspApp/static/bower_components/angular-translate-loader-url  (19 usages found)
                .bower.json  (7 usages found)
                    (2: 20) "name": "angular-translate-loader-url",
                    (3: 40) "description": "A plugin for Angular Translate",
                    (5: 22) "main": "./angular-translate-loader-url.js",
                    (7: 14) "angular-translate": "~2.7.2"
                    (17: 62) "homepage": "https://github.com/PascalPrecht/bower-angular-translate-loader-url",
                    (24: 59) "_source": "git://github.com/PascalPrecht/bower-angular-translate-loader-url.git",
                    (26: 31) "_originalSource": "angular-translate-loader-url"
                angular-translate-loader-url.js  (4 usages found)
                    (22: 30) angular.module('pascalprecht.translate')
                    (40: 12) .factory('$translateUrlLoader', $translateUrlLoader);
                    (72: 37) $translateUrlLoader.displayName = '$translateUrlLoader';
                    (73: 22) return 'pascalprecht.translate';
                angular-translate-loader-url.min.js  (4 usages found)
                    (6: 520) translate
                    (6: 542) $translateUrlLoader
                    (6: 606) $translateUrlLoader
                    (6: 640) translate
                bower.json  (4 usages found)
                    (2: 20) "name": "angular-translate-loader-url",
                    (3: 40) "description": "A plugin for Angular Translate",
                    (5: 22) "main": "./angular-translate-loader-url.js",
                    (7: 14) "angular-translate": "~2.7.2"
            amspApp/static/bower_components/bootstrap-css-only/css  (35 usages found)
                bootstrap-theme.css.map  (8 usages found)
                    (1: 16479) translate
                    (1: 16521) translate
                    (1: 16562) translate
                    (1: 16615) translate
                    (1: 16656) translate
                    (1: 16680) translate
                    (1: 16728) translate
                    (1: 16775) translate
                bootstrap.css.map  (27 usages found)
                    (1: 183746) translate
                    (1: 183784) translate
                    (1: 183821) translate
                    (1: 183855) translate
                    (1: 184119) translate
                    (1: 184154) translate
                    (1: 184188) translate
                    (1: 184219) translate
                    (1: 191639) translate
                    (1: 191680) translate
                    (1: 191822) translate
                    (1: 191864) translate
                    (1: 192046) translate
                    (1: 192084) translate
                    (1: 240842) translate
                    (1: 240884) translate
                    (1: 240925) translate
                    (1: 240978) translate
                    (1: 241019) translate
                    (1: 241043) translate
                    (1: 241091) translate
                    (1: 241138) translate
                    (1: 359543) translate
                    (1: 359641) translate
                    (1: 369886) translate
                    (1: 369986) translate
                    (1: 370108) translate
            amspApp/static/bower_components/bootstrap/dist/css  (35 usages found)
                bootstrap-theme.css.map  (8 usages found)
                    (1: 40311) translate
                    (1: 40353) translate
                    (1: 40394) translate
                    (1: 40447) translate
                    (1: 40488) translate
                    (1: 40512) translate
                    (1: 40560) translate
                    (1: 40607) translate
                bootstrap.css.map  (27 usages found)
                    (1: 190499) translate
                    (1: 190537) translate
                    (1: 190574) translate
                    (1: 190608) translate
                    (1: 190872) translate
                    (1: 190907) translate
                    (1: 190941) translate
                    (1: 190972) translate
                    (1: 198896) translate
                    (1: 198937) translate
                    (1: 199079) translate
                    (1: 199121) translate
                    (1: 199303) translate
                    (1: 199341) translate
                    (1: 247726) translate
                    (1: 247768) translate
                    (1: 247809) translate
                    (1: 247862) translate
                    (1: 247903) translate
                    (1: 247927) translate
                    (1: 247975) translate
                    (1: 248022) translate
                    (1: 368554) translate
                    (1: 368652) translate
                    (1: 379412) translate
                    (1: 379512) translate
                    (1: 379634) translate
            amspApp/static/bower_components/bpmn-modeler  (6 usages found)
                BpmnViewer.js  (2 usages found)
                    (703: 8) 'translate(' + top + ',' + 0 + ')'
                    (1677: 29) markerRect.transform('translate(' + (element.width / 2 - 7.5) + ',' + (element.height - 20) + ')');
                BpmnViewerApp.js  (2 usages found)
                    (700: 8) 'translate(' + top + ',' + 0 + ')'
                    (1674: 29) markerRect.transform('translate(' + (element.width / 2 - 7.5) + ',' + (element.height - 20) + ')');
                index.js  (2 usages found)
                    (1067: 22) 'translate(' + top + ',' + 0 + ')'
                    (2060: 43) markerRect.transform('translate(' + (element.width / 2 - 7.5) + ',' + (element.height - 20) + ')');
            amspApp/static/bower_components/bpmn-modeler/draw  (2 usages found)
                BpmnRenderer.js  (2 usages found)
                    (313: 8) 'translate(' + top + ',' + 0 + ')'
                    (1287: 29) markerRect.transform('translate(' + (element.width / 2 - 7.5) + ',' + (element.height - 20) + ')');
            amspApp/static/bower_components/bpmn-modeler/vendor  (2 usages found)
                disttt2.js  (2 usages found)
                    (707: 8) 'translate(' + top + ',' + 0 + ')'
                    (1681: 29) markerRect.transform('translate(' + (element.width / 2 - 7.5) + ',' + (element.height - 20) + ')');
            amspApp/static/bower_components/c3  (10 usages found)
                c3.js  (5 usages found)
                    (785: 17) return "translate(" + x + "," + y + ")";
                    (4682: 26) translate = "translate(" + (x * ratio) +  ',' + (y * ratio) +  ")";
                    (6237: 26) transform = 'translate(' + translateX + ',0) scale(' + scaleX + ',1)';
                    (6690: 25) return "translate(" + Math.ceil(x(d) + tickOffset) + ", 0)";
                    (6695: 25) return "translate(0," + Math.ceil(y(d)) + ")";
                c3.min.js  (5 usages found)
                    (1: 685) translate
                    (1: 778) translate
                    (1: 17970) translate
                    (4: 1105) translate
                    (4: 32331) translate
            amspApp/static/bower_components/c3-angular/examples/assets/js  (11 usages found)
                c3.min.js  (5 usages found)
                    (1: 685) translate
                    (1: 778) translate
                    (1: 17970) translate
                    (4: 1105) translate
                    (4: 32331) translate
                d3.min.js  (6 usages found)
                    (2: 14335) translate
                    (2: 14438) translate
                    (3: 460) translate
                    (3: 569) translate
                    (4: 15799) translate
                    (5: 11688) translate
            amspApp/static/bower_components/ckeditor/full/samples/js  (5 usages found)
                sf.js  (5 usages found)
                    (12: 322) translateX
                    (12: 358) translateX
                    (12: 397) translateX
                    (12: 431) translateX
                    (12: 460) translateX
            amspApp/static/bower_components/d3  (6 usages found)
                d3.js  (6 usages found)
                    (5963: 13) return "translate(" + this.translate + ")rotate(" + this.rotate + ")skewX(" + this.skew + ")scale(" + this.scale + ")";
                    (5993: 15) s.push("translate(", null, ",", null, ")");
                    (6002: 15) s.push("translate(" + tb + ")");
                    (9030: 15) return "translate(" + (isFinite(v0) ? v0 : x1(d)) + ",0)";
                    (9036: 15) return "translate(0," + (isFinite(v0) ? v0 : y1(d)) + ")";
                    (9129: 17) return "translate(" + xExtent[+/e$/.test(d)] + "," + yExtent[+/^s/.test(d)] + ")";
            amspApp/static/bower_components/jalalijscalendar  (1 usage found)
                calendar.js  (1 usage found)
                    (666: 44) text = "Help and about box text is not translated into this language.\n" +
            amspApp/static/bower_components/jalalijscalendar/lang  (1 usage found)
                calendar-br.js  (1 usage found)
                    (66: 2) "Translate to portuguese Brazil (pt-BR) by Fernando Dourado (fernando.dourado@ig.com.br)\n" +
            amspApp/static/bower_components/myapp  (7 usages found)
                appChart.js  (7 usages found)
                    (229: 54) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (230: 68) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (242: 37) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                    (345: 37) node.attr("transform", "translate(" + d.y0 + "," + d.x0 + ")");
                    (566: 25) return "translate(" + source.y0 + "," + source.x0 + ")";
                    (628: 25) return "translate(" + d.y + "," + d.x + ")";
                    (639: 25) return "translate(" + source.y + "," + source.x + ")";
            amspApp/static/languages  (2 usages found)
                en.json  (2 usages found)
                    (95: 47) "<h3 class="modal-title">//'labelModal'|translate//</h3>": "",
                    (96: 35) "<label>//'backgroundColor'|translate//": "",
            templates/authentication  (8 usages found)
                forget.html  (1 usage found)
                    (18: 100) ng-model="vm.ForgetEmail" placeholder=" // 'pleaseenteryouremail' | translate //">
                resetpass.html  (2 usages found)
                    (18: 87) ng-model="vm.NewPass" placeholder=" // 'newpassword' | translate //">
                    (22: 98) ng-model="vm.ConfirmNewPass" placeholder=" // 'confirmpassword' | translate //">
                signup.html  (5 usages found)
                    (18: 85) ng-model="vm.username" placeholder=" // 'fullname' | translate //">
                    (32: 78) ng-model="vm.email" placeholder="// 'email' | translate //">
                    (46: 84) ng-model="vm.password" placeholder="// 'password' | translate //">
                    (59: 87) ng-model="vm.password2" placeholder="// 'repeatpass' | translate //">
                    (79: 85) ng-model="vm.Captcha" placeholder="// 'repeatpass' | translate //">
            templates/companyManagement  (27 usages found)
                ChartEdit.html  (7 usages found)
                    (405: 74) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (406: 88) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (418: 57) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                    (521: 61) node.attr("transform", "translate(" + d.y0 + "," + d.x0 + ")");
                    (747: 49) return "translate(" + source.y0 + "," + source.x0 + ")";
                    (809: 49) return "translate(" + d.y + "," + d.x + ")";
                    (820: 49) return "translate(" + source.y + "," + source.x + ")";
                CompanyChart.html  (7 usages found)
                    (495: 74) svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
                    (496: 88) d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
                    (508: 57) svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                    (611: 61) node.attr("transform", "translate(" + d.y0 + "," + d.x0 + ")");
                    (837: 49) return "translate(" + source.y0 + "," + source.x0 + ")";
                    (899: 49) return "translate(" + d.y + "," + d.x + ")";
                    (910: 49) return "translate(" + source.y + "," + source.x + ")";
                CompanyProducts.html  (7 usages found)
                    (48: 75) <button type="button" tooltip="//'like' | translate//"
                    (50: 77) <button type="button" tooltip="//'follow' | translate//"
                    (52: 77) <button type="button" tooltip="//'needit' | translate//" class="btn btn-default btn-xs">
                    (55: 75) <button type="button" tooltip="//'edit' | translate//"
                    (59: 63) tooltip="//'delete' | translate//"
                    (88: 104) data-target="#addUpdateCompanyProductionModal" tooltip="//'Addnewproduction' | translate//">
                    (117: 75) placeholder="//'enteryourproductionnamehere' | translate //">
                CompanyProfile.html  (1 usage found)
                    (34: 152) <input type="text" class="form-control underline" ng-model="Profile.extra.name" id="nameOfCompany" placeholder="//'Enter Company Name'|translate//">
                Members.html  (5 usages found)
                    (27: 162) <button class="btn btn-danger btn-xs fa fa-bomb" ng-click="RemoveInbox(item)" tooltip="//'Completely remove position with inbox archive'|translate //"></button>
                    (44: 135) <button type="button" class="btn btn-default disabled fa fa-search" tooltip="//'View Profile'|translate//">
                    (46: 149) <button type="button" class="btn btn-default disabled fa fa-fighter-jet" tooltip="//'Send out confirmation'|translate//">
                    (48: 164) <button type="button" class="btn btn-default fa fa-bitbucket" ng-click="ForceOut(item)" tooltip="//'Force out this person'|translate//">
                    (51: 130) <button type="button" class="btn btn-default fa fa-sitemap" tooltip="//'Change Position'|translate//" ng-click="LoadChart(item)">
            templates/forms/base-templates  (1 usage found)
                select_multiple.html  (1 usage found)
                    (6: 66) placeholder="// 'Searchhere...' | translate //" ng-model="{{ style.searchInput }}"
            templates/friends  (7 usages found)
                friends.html  (7 usages found)
                    (50: 63) tooltip="//'View profile'|translate//"></button>
                    (52: 77) tooltip="//'Send membership invitation'|translate//"></button>
                    (54: 77) tooltip="//'Send friendship invitation'|translate//"></button>
                    (56: 63) tooltip="//'Send message'|translate//"></button>
                    (103: 94) tooltip="//'Click here to send/remove invitation'|translate//">
                    (134: 80) tooltip="//'Click here to approve'|translate//"
                    (141: 90) tooltip="//'Click here to remove invitation'|translate//"
            templates/generic-templates  (4 usages found)
                selectPositions.html  (3 usages found)
                    (5: 50) <tab heading="//'persons'|translate//">
                    (42: 37) <tab heading="//'chart'|translate//"></tab>
                    (43: 38) <tab heading="//'groups'|translate//" ui-sref="company.chart({ 'companyid': companyId })"></tab>
                Table.html  (1 usage found)
                    (16: 87) placeholder="// 'Searchhere...' | translate //"
            templates/myProfile  (2 usages found)
                PersonProfile.html  (2 usages found)
                    (34: 63) placeholder="//'enteryourname'|translate//"
                    (39: 60) placeholder="//'occupation'|translate//"
            templates/others  (6 usages found)
                index.html  (6 usages found)
                    (103: 49) <script src={% static "bower_components/angular-translate/angular-translate.js" %}></script>
                    (103: 67) <script src={% static "bower_components/angular-translate/angular-translate.js" %}></script>
                    (104: 49) <script src={% static "bower_components/angular-translate-loader-url/angular-translate-loader-url.js" %}></script>
                    (104: 78) <script src={% static "bower_components/angular-translate-loader-url/angular-translate-loader-url.js" %}></script>
                    (105: 49) <script src={% static "bower_components/angular-translate-loader-static-files/angular-translate-loader-static-files.js" %}></script>
                    (105: 87) <script src={% static "bower_components/angular-translate-loader-static-files/angular-translate-loader-static-files.js" %}></script>


"""

aa = aa.split('//"')
bb = []
for a in aa:
    bb.append(a.split())
aa = aa