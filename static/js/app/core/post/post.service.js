'use strict';

//angular.
//    module('core.post').
//        factory('Post', function(LoginRequiredInterceptor, $cookies, $httpParamSerializer, $location,$resource){
//            var url = '/api/posts/:id/'
//            return $resource(url, {}, {
//                query: {
//                    method: "GET",
//                    params: {},
//                    isArray: true,
//                    cache: false,
//                    transformResponse: function(data, headersGetter, status){
//                         console.log(data);
//
//
//                        var finalData = angular.fromJson(data);
//                        console.log(finalData);
//                        return finalData
//                    }
//                },
//                get: {
//                    method: "GET",
//                    params: {"id": "@id"},
//                    isArray: false,
//                    cache: false,
//                }
//            })
//
//
//
//        });


        angular.
    module('core.post').
        factory('Post', function(LoginRequiredInterceptor, $cookies, $httpParamSerializer, $location,$resource){
            var url = '/api/posts/:id/'

            var token = $cookies.get("token");
            return $resource(url, {}, {
                query: {
                    method: "GET",
                    headers:{"Authorization": "JWT " + token},
                    params: {},
                    isArray: true,
                    cache: false,
                    interceptor: {responseError: LoginRequiredInterceptor},
                    transformResponse: function(data, headersGetter, status){
                         console.log(data);

                        var finalData = angular.fromJson(data);
                        console.log(finalData);
                        return finalData
                    }
                },
                get: {
                    method: "GET",
                    params: {"id": "@id"},
                    headers:{"Authorization": "JWT " + token},
                    interceptor: {responseError: LoginRequiredInterceptor},
                    isArray: false,
                    cache: false,


                },
                delete: {
                    url: '/api/posts/:id/delete/',
                    method: "DELETE",
                    headers:{"Authorization": "JWT " + token},
                    interceptor: {responseError: LoginRequiredInterceptor},

                },
                update:{
                    url: '/api/post/:id/edit/',
                    method: "PUT",
                    headers:{"Authorization": "JWT " + token},
                    interceptor: {responseError: LoginRequiredInterceptor},
                },
                productdelete:{
                    url: '/api/posts/:id/delete/',
                    method: "DELETE",
                    headers:{"Authorization": "JWT " + token},
                    interceptor: {responseError: LoginRequiredInterceptor},
                },

            })


        });