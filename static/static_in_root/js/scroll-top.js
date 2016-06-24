$(document).ready(function () {
    $(".btn-top").on("click", function (event) {
        event.preventDefault();
        var id = $(this).attr('href'),
            top = $(id).offset().top;
        console.log("asd");
        $('body,html').animate({scrollTop: top}, 1000);
    });

});


