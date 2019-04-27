// Header code starts

// Scrolling Effect
$(window).on("scroll", function() {
  if($(window).scrollTop()) {
    $('nav').addClass('colourchange');
  }
  else {
    $('nav').removeClass('colourchange');
  }
})

var navbarToggle = document.querySelector(".navbar-toggle");
var navbarMenu = document.querySelector(".navbar ul");
var navbarLinks = document.querySelectorAll(".navbar a");

navbarToggle.addEventListener("click", navbarToggleClick);

function navbarToggleClick() {
  navbarToggle.classList.toggle("open-navbar-toggle");
  navbarMenu.classList.toggle("open");
}

navbarLinks.forEach(a => a.addEventListener("click", navbarLinkClick));

function navbarLinkClick() {
  if(navbarMenu.classList.contains("open")) {
    navbarToggle.click();
  }
}

// header code ends

// footer code

var d = new Date();
document.getElementById("demo").innerHTML = d;
var a = "This page was last modified on: " + document.lastModified +"";
document.getElementById("demo2").innerHTML = a;
