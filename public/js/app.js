(function() {
  var app = angular.module('trawel', []);

  app.controller('CityController', function($scope, $http){
	$scope.city = function(param) {
	$http.get('data.json', param).success(
    function(data){
		
	//What should I do here?
    console.log(data);
    }
  ).error();
 } 
});

  app.controller('TabController', function(){
    this.tab = 1;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    };
  });

});