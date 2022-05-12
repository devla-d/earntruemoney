'use strict';

(function($) {

    // $(window).on('load', function() {
    //     console.log('Hello')
    //     $('.wrapper').addClass('show')
    //         .delay(3000)
    //         .queue(function(next) {
    //             $(this).addClass('show');
    //             next();
    //         })
    // })

    $(document).ready(function() {

        $('.set-bg').each(function() {
            var bg = $(this).data('bg');
            $(this).css('background-image', `url(${bg})`)
        })


        /**
         * Animation on scroll
         */
        AOS.init({
            offset: 0,
            duration: 1200,
            easing: 'ease-in-out',
        });



        new WOW().init();




        var side_bar_is_open = false
        $(".hamburger").on("click", function() {
            if (side_bar_is_open === false) {
                side_bar_is_open = true
                $(".sidebar, .page-overlay").addClass('active')
            } else {

            }
        })

        $(".dismiss").on("click", function() {
            if (side_bar_is_open === true) {
                side_bar_is_open = false
                $(".sidebar, .page-overlay").removeClass('active')
            }
        })








    })


    $('.accordion >.accordion-item:eq(0) .accordion-title').addClass('active').next().slideDown().parent().addClass('active');
    $('.accordion .accordion-title').click(function(j) {
        var dropDown = $(this).closest('.accordion-item').find('.question-block');
        console.log(dropDown)
        $(this).closest('.accordion').find('.question-block').not(dropDown).slideUp();
        if ($(this).hasClass('active')) {
            $(this).removeClass('active').parent().removeClass('active');
        } else {
            $(this).closest('.accordion').find('.accordion-title.active').removeClass('active').parent().removeClass('active');
            $(this).addClass('active').parent().addClass('active');
        }
        dropDown.stop(false, true).slideToggle();
        j.preventDefault();
    });




    $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
        $("body").toggleClass("sidebar-toggled");
        $(".left-panel").toggleClass("toggled");

    });
    $('.open-notification').on("click", function(e) {
        e.preventDefault()
        $(".notification-dialog").addClass("active");
    })

    $(".close-notification").on("click", function() {
        $(".notification-dialog").removeClass("active");
    })
    $('.close-ref-dialog  ').on('click', function() {
        $('.referral-dialog').toggleClass('active')
    })
    $('.close-msg-dialog  ').on('click', function() {
        $('.msg-dialog').toggleClass('active')
    })
    $('#open-ref').on('click', function(e) {
        e.preventDefault()
        $('.referral-dialog').toggleClass('active')
    })
})(jQuery);