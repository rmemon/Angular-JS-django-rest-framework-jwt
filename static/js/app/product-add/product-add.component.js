'use strict';
angular.module('productAdd').
    component('productAdd', {
        templateUrl: '/templatess/productadd.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $routeParams,
                $rootScope,
                $scope
            ){

            var productUrl = 'api/product/add/';
            $scope.productError = {}
            var token = $cookies.get("token");

            $scope.product = {

            };
            $scope.doProductadd = function(product){

                if (!product.title) {
                    $scope.productError.title = ["This field may not be blank."]
                }
                if (!product.charge_perhour) {
                    $scope.productError.charge_perhour = ["This field may not be blank."]
                }
                if (!product.charge_perday) {
                    $scope.productError.charge_perday = ["This field may not be blank."]
                }
                if (!product.charge_perweek) {
                    $scope.productError.charge_perweek = ["This field may not be blank."]
                }

                if (product.title && product.charge_perhour && product.charge_perday && product.charge_perweek) {
                    var reqConfig = {
                        method: "POST",
                        url: productUrl,
                        data: {
                            title: product.title,
                            charge_perhour: product.charge_perhour,
                            charge_perday: product.charge_perday,
                            charge_perweek: product.charge_perweek,
                        },
                            headers:{"Authorization": "JWT " + token},
                    }
                    var requestAction = $http(reqConfig)

                    requestAction.success(function(r_data, r_status, r_headers, r_config){
                            $location.path("/")
                    })
                    requestAction.error(function(e_data, e_status, e_headers, e_config){
                            $scope.loginError = e_data

                    })
                }

}
        }
})
