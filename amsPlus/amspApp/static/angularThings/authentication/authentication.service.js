/**
 * Created by amirmansouri on 6/22/15.
 */
/**
 * Authentication
 */
(function () {
    'use strict';

    angular
        .module('AniTheme')
        .factory('Authentication', Authentication);

    Authentication.$inject = [ '$cookies', '$http','$location'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function Authentication($cookies, $http,$location) {

        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Authentication = {
            getAuthenticatedUser: getAuthenticatedUser,
            isAuthenticated: isAuthenticated,
            login: login,
            logout: logout,
            register: register,
            setAuthenticatedUser: setAuthenticatedUser,
            unauthenticate: unauthenticate
        };

        return Authentication;

        ////////////////////

        /**
         * @name register
         * @desc Try to register a new user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} password2 The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         * @memberOf thinkster.authentication.services.Authentication
         */

        function logout() {
            return $http.post('/api/v1/auth/logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            /**
             * .
             * @name logoutSuccessFn
             * @desc Unauthenticate and redirect to index with page reload
             */
            function logoutSuccessFn(data, status, headers, config) {
                Authentication.unauthenticate();
                $location.url('/login');
            }

            /**
             * @name logoutErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function logoutErrorFn(data, status, headers, config) {
                console.error('Epic failure!');

            }
        }

        function register(email, password, password2, username) {
             return $http.post('/api/v1/users/', {
                username: username,
                password: password,
                confirm_password: password2,
                email: email
            });
        }

        function login(username, password,remember) {
            return $http.post('/api/v1/auth/login/', {
                username: username, password: password,remember:remember
            });



        }

        function getAuthenticatedUser() {
            if (!($.cookie("authenticatedUser"))) {
                return;
            }

            return JSON.parse($cookies.authenticatedUser);
        }

        function isAuthenticated() {
            return $.cookie("authenticatedUser");
        }

        function setAuthenticatedUser(user,remember) {
            if  (remember==true){
                $.cookie("authenticatedUser", JSON.stringify(user), { expires: 7 });
            }else{

                $.cookie("authenticatedUser", JSON.stringify(user));
            }
        }

        function unauthenticate() {
            delete $cookies.authenticatedUser;
        }
    }


})();