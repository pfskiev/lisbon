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
});

function delete_contact(id) {
    _id = id
}
function confirm_delete() {
    window.location.pathname = '/tours/' + _id + '/delete/'
}

