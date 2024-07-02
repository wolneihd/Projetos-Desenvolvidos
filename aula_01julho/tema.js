$(document).ready(function() {
    $('#tema-escuro').click(function(){
        $('body').addClass('dark-mode');
        $('header').addClass('dark-mode');
    })
});

$(document).ready(function() {
    $('#tema-claro').click(function(){
        $('body').removeClass('dark-mode');
        $('header').removeClass('dark-mode');
    })
});