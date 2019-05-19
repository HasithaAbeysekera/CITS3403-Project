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

function validateForm(form) {

  field = /^\w+$/;
  if(!field.test(form.username.value)) {
    alert("Error: Username must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }

  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if(!re.test(form.email.value)) {
    alert("Error: The email must be valid!");
    form.email.focus();
    return false;
  }

  if(!field.test(form.password.value)) {
    alert("Error: Password must contain only letters, numbers and underscores!");
    form.password.focus();
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

  if(form.password.value != form.password2.value) {
    alert("Error: Passwords don't match!");
    form.password.focus();
    return false;
  }
}

function validateForm2(form) {

  field = /^\w+$/;
  if(!field.test(form.pollname.value)) {
    alert("Error: Poll Name must contain only letters, numbers and underscores!");
    form.pollname.focus();
    return false;
  }
}

function checkRadioButton(field) {
  if(!field.length) {
    field = [field];
  }

  for(var i=0; i < field.length; i++) {
    if(field[i].checked) return field[i].value;
  }
  return false;
}

function validateForm3(form) {
  var radioValue;
  if(radioValue = checkRadioButton(form.entries)) {
    // alert("You selected " + radioValue);
    return true;
  }

  else {
    alert("Error: Please select an option!");
    return false;
  }
}

function validateForm4(form) {
  field = /^[a-zA-Z0-9 ]+$/;
  if(!field.test(form.playername.value)) {
    alert("Error: The new players name must contain only letters, numbers and spaces!");
    form.playername.focus();
    return false;
  }
  if(!field.test(form.country.value)) {
    alert("Error: The new players country must contain only letters, numbers and spaces!");
    form.country.focus();
    return false;
  }
  if(!field.test(form.club.value)) {
    alert("Error: The new players club must contain only letters, numbers and spaces!");
    form.club.focus();
    return false;
  }

  else return true;
}

// Login Validation code ends

//bar chart code

var table = document.getElementById("myTable"), sumVal = 0;
var players = [];
var votes = [];
var percentageVotes = [];

for (var i = 1; i < table.rows.length; i++) {
  sumVal = sumVal + parseInt(table.rows[i].cells[1].innerHTML);
  players[i-1] = table.rows[i].cells[0].innerHTML.split(" ").slice(-1);
  votes[i-1] = table.rows[i].cells[1].innerHTML;
}

for (var i = 1; i < table.rows.length; i++) {
  percentageVotes[i-1] = (votes[i-1] / sumVal) * 100;
}

// console.log(players);
// console.log(votes);
// console.log(percentageVotes);

let myChart = document.getElementById('myChart').getContext('2d');
let barChart = new Chart(myChart, {
  type:'bar',
  data: {
    labels:players,
    datasets:[{
      label:'Percentage vote',
      data:percentageVotes,
      // backgroundColor:'#009879'
      backgroundColor:[
        'rgba(153,102,255,0.6)',
        'rgba(75,192,192,0.6)',
        'rgba(255,99,132,0.6)',
        // 'rgba(255,159,64,0.6)',
        'rgba(54,162,235,0.6)',
        'rgba(255,206,86,0.6)'
      ]
    }]
  },
  options:{
      scales: {
          yAxes:[{
              display: true,
              ticks: {
                  beginAtZero: true,
                  min: 0,
                  max: 100
              }
          }],
      }
  }
});


function updateChart() {
  chart.data.datasets[0].data = [45, 40, 9, 0, 3];

  chart.update();
}
