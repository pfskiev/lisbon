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
    $('footer .text-justify').empty().text('We are portuguese family company providing best quality of service in tourism in LISBON city and PORTUGAL. Our staff is qualified guides, including myself, who speak several languages and ready to show you the best what Lisbon has to offer. What is important to us is that you get satisfied of our services and if you are happy then we are double happy! Come and enjoy Golden Lisbon! Your sincerely, Mark Danici - CEO')
});

function delete_contact(id) {
    _id = id
}
function confirm_delete() {
    window.location.pathname = '/tours/' + _id + '/delete/'
}

