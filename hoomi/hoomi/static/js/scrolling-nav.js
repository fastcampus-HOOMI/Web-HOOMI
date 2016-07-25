//jQuery to collapse the navbar on scroll
$(document).ready(function(){
    $(window).scroll(function() {
        if ($('.navbar').offset().top > 50) {
            $('.navbar').addClass('.navbar-fixed-top');
        } else {
            $('.navbar').removeClass('.navbar-fixed-top');
        }
    });

    //jQuery for page scrolling feature - requires jQuery Easing plugin
    $(function() {
        $('.page-scroll a').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
    });
});