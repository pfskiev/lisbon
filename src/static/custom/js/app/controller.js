(function(){

    function textEditorCtrl ($scope){

        console.log('Hello')

    }

    textEditorCtrl.$inject = ['$scope'];

    angular.module('App')
        .controller('textEditorCtrl', textEditorCtrl)
}());