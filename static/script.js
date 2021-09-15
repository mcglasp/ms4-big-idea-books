// EXPERIMENTAL
$(window).scroll(function () {
    setTimeout(() => {
        $('#shape-2').css('visibility', 'visible');
    setTimeout(() => { 
        $('#shape-3').css('visibility', 'visible');
    }, 200);
    
}, 200);
});