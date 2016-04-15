(function(){
    angular.module('App', ['textAngular']).config(
        function($interpolateProvider) {
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
        });
}());