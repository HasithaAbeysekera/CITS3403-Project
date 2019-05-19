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

function validateForm2(form) {

  field = /^\w+$/;
  if(!field.test(form.username.value)) {
    alert("Error: Username must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }

  if(!field.test(form.pollname.value)) {
    alert("Error: Poll Name must contain only letters, numbers and underscores!");
    form.username.focus();
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
  if(radioValue = checkRadioButton(form.option)) {
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
  if(!field.test(form.name.value)) {
    alert("Error: The new entry must contain only letters, numbers and spaces!");
    form.other.focus();
    return false;
  }
  if(!field.test(form.country.value)) {
    alert("Error: The new entry must contain only letters, numbers and spaces!");
    form.other.focus();
    return false;
  }
  if(!field.test(form.club.value)) {
    alert("Error: The new entry must contain only letters, numbers and spaces!");
    form.other.focus();
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
  players[i-1] = table.rows[i].cells[0].innerHTML;
  votes[i-1] = table.rows[i].cells[1].innerHTML;
}

for (var i = 1; i < table.rows.length; i++) {
  percentageVotes[i-1] = (votes[i-1] / sumVal) * 100;
}

// var player1 = table.rows[1].cells[0].innerHTML;
// var player2 = table.rows[2].cells[0].innerHTML;
// var player3 = table.rows[3].cells[0].innerHTML;
// var player4 = table.rows[4].cells[0].innerHTML;
// var player5 = table.rows[5].cells[0].innerHTML;

// var votes1 = table.rows[1].cells[1].innerHTML;
// var votes2 = table.rows[2].cells[1].innerHTML;
// var votes3 = table.rows[3].cells[1].innerHTML;
// var votes4 = table.rows[4].cells[1].innerHTML;
// var votes5 = table.rows[5].cells[1].innerHTML;
//
// var percentageVotes1 = (votes[1] / sumVal) * 100;
// var percentageVotes2 = (votes[2] / sumVal) * 100;
// var percentageVotes3 = (votes[3] / sumVal) * 100;
// var percentageVotes4 = (votes[4] / sumVal) * 100;
// var percentageVotes5 = (votes[5] / sumVal) * 100;

// console.log(sumVal);
console.log(players);
console.log(votes);
console.log(percentageVotes);
// console.log(player2);
// console.log(player3);
// console.log(player4);
// console.log(player5);
// console.log(votes1);
// console.log(votes2);
// console.log(votes3);
// console.log(votes4);
// console.log(votes5);
// console.log(percentageVotes1);
// console.log(percentageVotes2);
// console.log(percentageVotes3);
// console.log(percentageVotes4);
// console.log(percentageVotes5);




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
    maintainAspectRatio: false
  }
});

function updateChart() {
  chart.data.datasets[0].data = [45, 40, 9, 0, 3];

  chart.update();
}
