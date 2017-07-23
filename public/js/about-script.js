$(document).ready(function(){       
   var scroll_start = 0;
   var actual = $('#actual');
   var offset = actual.offset();   

   //For navbar change-color
  if (actual.length){
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
	  if(scroll_start > (offset.top-10)) {
          $(".navbar-default").css('background-color', '#E86B4B');
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
