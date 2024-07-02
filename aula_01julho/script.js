'use strict'

$(document).ready(function() {
    $('#inputRange').on('input',function(){
        console.log($('#inputRange').val());
        $('#rangeValue').text($('#inputRange').val());
    })
})