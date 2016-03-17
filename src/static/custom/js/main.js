$('document').ready(function() {
    var _id = '';
    $(".datepicker").datepicker();
    $('.phone').mask('0(000)-000-00-00');
    $('.btn.btn-warning').each(function(){
        $(this).addClass('shadow')
    })
});

function delete_contact(id) {
    _id = id
}
function confirm_delete() {
    window.location.pathname = '/tours/' + _id + '/delete/'
}


