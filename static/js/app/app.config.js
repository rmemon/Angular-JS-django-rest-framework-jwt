'use strict';

angular.module('try').
    config(
        function(
          $locationProvider,
          $resourceProvider,
          $routeProvider
          ){


          $locationProvider.html5Mode({
              enabled:true
            })

          $resourceProvider.defaults.stripTrailingSlashes = false;
          $routeProvider.
              when("/", {
                template: "<product-list></product-list>",
              }).
              when("/about", {
                templateUrl: "/templatess/about.html"
              }).
              when("/product", {
                  template: "<product-list></product-list>",
//                  redirectTo: '/'
              }).

              when("/product/:id", {
                  template: "<product-detail></product-detail>"
              }).

              when("/login", {
                  template: "<login-detail></login-detail>",
                  // redirectTo: '/'
              }).
              when("/logout", {
                   template: "<login-detail></login-detail>",
//                  redirectTo: '/login'
              }).
               when("/register", {
                  template: "<register-detail></register-detail>",
              }).

              when("/add", {
                  template: "<product-add></product-add>",

              }).
              otherwise({
                  template: "Not Found"
              })
    });