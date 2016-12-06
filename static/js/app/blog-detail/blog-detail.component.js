'use strict';

angular.module('blogDetail').
    component('blogDetail', {
         templateUrl: '/templatess/productdetail.html',

        controller: function( Post, $cookies, $http, $location, $routeParams, $scope){
            $scope.loading = true;
            $scope.post = null;
            $scope.pageError = false;
            $scope.notFound = false;

            function postDataSuccess(data){

                $scope.loading = false;
                $scope.post = data

            }

            var id = $routeParams.id
            Post.get({"id": id}, postDataSuccess)

             $scope.updateProduct = function(post) {
                post.$update({"id": post.id,content: $scope.post.content}, function(data){
                    $location.path("/blog/")
                }, function(e_data){
                    console.log(e_data)
                })
            }


    }
});