$('#id_login').addClass('login-input');
$('#id_password').addClass('login-input');
$('#id_email').addClass('login-input');

$(function () {
    var login = $("#id_login_pat");
    var password = $("#id_password_pat");
    var login_change = $("#pass-login-change");
    login.change(function () {
        login_change.val(1);
    });
    password.change(function () {
        login_change.val(1);
    });
    $("input").prop('required', true);
    var photo = $("#id_photo_pat").prop('required', false);
    $("#photo_pat-clear_id").prop('required', false);
    var s = $(".update-info-form ul li a").text();
    if (s) {
        $("#current-image").attr({"src": "/media/" + s});
    } else {
        photo.css("margin-left", "150px");
    }
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#current-image').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    photo.change(function () {
        readURL(this);
    });
});
function clicked() {
    $(document).ready(function () {
        var login = $('#id_login_pat');
        var password = $('#id_password_pat');
        login.val(login.val().toLowerCase());
        password.val(password.val().toLowerCase());
    });
    return confirm('Вы уверены что хотите обновить свой профиль?');
}

