$(window).scroll(function(){
	var scroll = $(window).scrollTop();

	bruh = document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";
	 // console.log(bruh)
	if (scroll >= 300) {
		$("#myNav").addClass("bg-dark");
	} else {
		$("#myNav").removeClass("bg-dark");
	}
});