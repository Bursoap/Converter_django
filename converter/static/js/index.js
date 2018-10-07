$(document).ready(function(){
    $('#btn1').click(function() {
        var number = {"input_number": $('#number').val()};
        var csrftoken = getCookie('csrftoken');
        send_ajax(number, csrftoken);
        return false;
    });
});

function send_ajax(number, csrftoken) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
        url:    '/',
        type:   'POST',
        data: JSON.stringify(number),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response){
            $('.invalid-feedback').hide();
            $('.is-invalid').removeClass('is-invalid');
            $('#result').val(response['result']);
         },
        error: function(response) {
            var error = response["responseJSON"]["__all__"][0];
            $(".number").html(error).show();
            $("#number").addClass('is-invalid')
        }
    });
    return false;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
