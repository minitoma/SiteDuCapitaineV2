function goTo() {
  document.getElementById("nav_go").scrollIntoView({ behavior: 'smooth' })
}

$('.nav li').click(function(){
      $('.nav li').removeClass('active');
      $(this).addClass('active');
    });
