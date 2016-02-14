//we can swap hover out to login
$(".envelope").hover(function() {
  
    $('.paper').css('top', '-200px');
    $('.paper').css('height', '300px');
    $('.envelope').css('opacity', '0.0');
    $('#outside').css('opacity', '1.0');
});

$(".envelope").mouseout(function() { 
    $('.paper').css('top', '-0px');
    $('.paper').css('height', '190px');
    $('#outside').css('opacity', '0.0');
    $('.envelope').css('opacity', '1.0');
});





// $(".paper").click(function() {
//    $(this).toggleClass("hilite"); {
     
//       $('.paper').css('top', '-0px'); 
//    }
   
// });




// if ($('.paper').css('top') === '-0px') {
//     $('.paper').css('top', '-99px');
// }
