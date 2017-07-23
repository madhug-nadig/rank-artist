$(document).ready(function(){       
   var scroll_start = 0;
   var Cities = $('#Cities');
   var offset = Cities.offset();   
   var analytics = $('.analytics');
   var off = analytics.offset();
   var contribute = $('.contribute');
   var offc = contribute.offset();
   

   //For navbar change-color
    if (contribute.length){
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
	  if(scroll_start > (offc.top-10)) {
          $(".navbar-default").css('background-color', '#05778C');
       }else  if(scroll_start > (off.top-10)) {
          $(".navbar-default").css('background-color', '#00A85D');
       } else  if(scroll_start > (offset.top-10)) {
          $(".navbar-default").css('background-color', '#000');
       } 
	   else {
          $('.navbar-default').css('background-color', '#5CDEBD');
       }
      });
    }//Navbbar change-color
});
$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 800);
        return false;
      }
    }
  });
});



