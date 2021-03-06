(function () {

    function contactUs () {
        function link (scope) {
            _.map(['textarea', 'input', 'label', 'select'], function(el){
                el === 'label' && $(el).attr('type') !== 'submit' ? $(el).addClass('my-label') : $(el).addClass('form-control');
            });
            $('select').css('height', '40px')

        }
        return {
            scope: {},
            templateUrl: '/contact-us',
            link: link

        }
    }

    angular.module('App')
        .directive('contactUs', contactUs)
}());

(function () {

    function bookNow () {
        function link (scope, element) {

            _.map(['textarea', 'input', 'label', 'select'], function(el){
                el === 'label' && $(el).attr('type') !== 'submit' ? $(el).addClass('my-label') : $(el).addClass('form-control');
            });
            $('select').css('height', '40px')

        }
        return {

            scope: {

            },
            templateUrl: '/book-form',
            link: link

        }
    }

    angular.module('App')
        .directive('bookNow', bookNow)
}());