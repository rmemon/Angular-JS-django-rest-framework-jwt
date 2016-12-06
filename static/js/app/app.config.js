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
                template: "<blog-list></blog-list>",
              }).
              when("/about", {
                templateUrl: "/templatess/about.html"
              }).
              when("/blog", {
                  template: "<blog-list></blog-list>",
//                  redirectTo: '/'
              }).

              when("/blog/:id", {
                  template: "<blog-detail></blog-detail>"
              }).

              when("/login", {
                  template: "<login-detail></login-detail>",
                  // redirectTo: '/'
              }).
              when("/logout", {
                  // template: "<login-detail></login-detail>",
                  redirectTo: '/login'
              }).
               when("/register", {
                  template: "<register-detail></register-detail>",
                  // redirectTo: '/'
              }).

              when("/add", {
                  template: "<product-add></product-add>",

              }).
              otherwise({
                  template: "Not Found"
              })
    });