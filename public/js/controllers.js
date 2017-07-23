var placeController = angular.module('placeController', []);

placeController.controller('ListController', ['$scope', '$http', function($scope, $http) {
  $http.get('js/data.json').success(function(data) {
    $scope.places = data;
  });
}]);

placeController.controller('DetailsController', ['$scope', '$http','$routeParams', function($scope, $http, $routeParams) {
  $http.get('js/data.json').success(function(data) {
    $scope.places = data;
    $scope.whichItem = $routeParams.itemId;
  });
}]);
