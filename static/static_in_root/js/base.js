/**
 * Created by kinglight on 02.05.16.
 */
$(document).ready(function () {
    var asd =1;
    $("#news").click(function () {
        $(".sidebar-menu-wrap").addClass("active");
        $("#popnews").addClass("active");
    });
    $(".sidebar-menu-wrap").click(function(){
        //alert("sd");
        var container = $(".sidebar-menu-wrap");
        if ($(event.target).closest('.sidebar-menu').length === 0) {
            container.removeClass("active");
            $(".sidebar-menu").removeClass("active");

       }
    });
    //$(document).on('click', function (event) {
    //
    //    // if ($("#popnews").hasClass("active")) {
    //    //alert("Sdf");
    //    var container = $(".sidebar-menu");
    //    if ($(event.target).closest('.sidebar-menu').length === 0) {
    //        container.removeClass("active");
    //
    //    }
    //});


});