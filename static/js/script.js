// Add your javascript here
$(function() {
  $("h1").animate({
    "margin-left": "110px"
  }, "slow");

  $(".nav li").on("click", function() {
    $(".nav li").removeClass("active");
    $(this).addClass("active");
  });
});