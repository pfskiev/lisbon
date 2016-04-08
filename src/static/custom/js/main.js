$('document').ready(function() {
    var _id = '';
    $(".datepicker").datepicker();
    $('.phone').mask('+(000)-00-000-00-00');
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
});

function delete_contact(id) {
    _id = id
}
function confirm_delete() {
    window.location.pathname = '/tours/' + _id + '/delete/'
}

