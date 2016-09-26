$(document).ready(function(){
    $('.menu-btn').click(function(){
        $('nav').toggleClass('open');
        $(this).toggleClass('close-btn');
        $('.container').toggle();
    })
})