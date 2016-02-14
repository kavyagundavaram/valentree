console.log("poop");
$(document).ready(function() {
  console.log("hello");

  $(".envelope").hover(function() { 
      $('.paper').css('top', '-99px');
  });
  
  $(".envelope").mouseout(function() { 
      $('.paper').css('top', '-0px');
  });
});
