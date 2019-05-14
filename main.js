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

// footer code ends

// Login and register Validation code starts

// function validateForm2(form) {
//
//     if(form.password.value != form.passwordrepeat.value) {
//       alert("Error: Passwords don't match!");
//       form.password.focus();
//       return false;
//     }
//
// }

function validateForm(form) {

  field = /^\w+$/;
  if(!field.test(form.username.value)) {
    alert("Error: Username must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }
  if(!field.test(form.password.value)) {
    alert("Error: Password must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }

  if(form.password.value.length < 6) {
    alert("Error: Password must contain at least six characters!");
    form.password.focus();
    return false;
  }

  if(form.password.value == form.username.value) {
    alert("Error: Password must be different from Username!");
    form.password.focus();
    return false;
  }
  
  field = /[0-9]/;
  if(!field.test(form.password.value)) {
    alert("Error: password must contain at least one number (0-9)!");
    form.password.focus();
    return false;
  }
  field = /[a-z]/;
  if(!field.test(form.password.value)) {
    alert("Error: password must contain at least one lowercase letter (a-z)!");
    form.password.focus();
    return false;
  }
  field= /[A-Z]/;
  if(!field.test(form.password.value)) {
    alert("Error: password must contain at least one uppercase letter (A-Z)!");
    form.password.focus();
    return false;
  }
  if(form.password.value != form.passwordrepeat.value) {
    alert("Error: Passwords don't match!");
    form.password.focus();
    return false;
  }
}

// Login Validation code ends
