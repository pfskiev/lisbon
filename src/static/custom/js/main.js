$('document').ready(function() {
    var _id = '';
    $(".datepicker").datepicker();
    //$('.phone').mask('+(000)-00-000-00-00');
    $('.btn.btn-warning').each(function(){
        $(this).addClass('shadow')
    })
    $('.carousel').carousel({
        interval: 5000
    })
    _.map(['textarea', 'input', 'label', 'select'], function(el){
                el === 'label' && $(el).attr('type') !== 'submit' ? $(el).addClass('my-label') : $(el).addClass('form-control');
            });
        $('select').css('height', '40px')

    $('.js-accordion-trigger').bind('click', function(e){
        var $parent = $(this).parent();
        $parent.find('.submenu').slideToggle('fast');
        if($parent.find('.fa-chevron-down').attr('style') == "transform: rotate(-180deg);") {
            $parent.find('.fa-chevron-down').css('transform', 'rotate(-0deg)')
        }
        else {
            $parent.find('.fa-chevron-down').css('transform', 'rotate(-180deg)');
        }
        e.preventDefault();
    });

    if ($("#js-parallax-window").length) {
        parallax();
    }

});

$(window).scroll(function(e) {
  if ($("#js-parallax-window").length) {
    parallax();
  }
});

function parallax(){
  if( $("#js-parallax-window").length > 0 ) {
    var plxBackground = $("#js-parallax-background");
    var plxWindow = $("#js-parallax-window");

    var plxWindowTopToPageTop = $(plxWindow).offset().top;
    var windowTopToPageTop = $(window).scrollTop();
    var plxWindowTopToWindowTop = plxWindowTopToPageTop - windowTopToPageTop;

    var plxBackgroundTopToPageTop = $(plxBackground).offset().top;
    var windowInnerHeight = window.innerHeight;
    var plxBackgroundTopToWindowTop = plxBackgroundTopToPageTop - windowTopToPageTop;
    var plxBackgroundTopToWindowBottom = windowInnerHeight - plxBackgroundTopToWindowTop;
    var plxSpeed = 0.35;

    plxBackground.css('top', - (plxWindowTopToWindowTop * plxSpeed) + 'px');
  }
}

function delete_contact(id) {
    _id = id
}
function confirm_delete() {
    window.location.pathname = '/tours/' + _id + '/delete/'
}

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(() => console.log('SERVICE WORKER DOWNLOADED'));
    });
}
