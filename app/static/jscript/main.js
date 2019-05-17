// Header code starts

// Scrolling Effect
$(window).on("scroll", function () {
  if ($(window).scrollTop()) {
    $('nav').addClass('colourchange');
  } else {
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
  if (navbarMenu.classList.contains("open")) {
    navbarToggle.click();
  }
}

// header code ends

// footer code

var d = new Date();
document.getElementById("demo").innerHTML = d;
var a = "This page was last modified on: " + document.lastModified + "";
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
  if (!field.test(form.username.value)) {
    alert("Error: Username must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }
  if (!field.test(form.password.value)) {
    alert("Error: Password must contain only letters, numbers and underscores!");
    form.username.focus();
    return false;
  }

  if (form.password.value.length < 6) {
    alert("Error: Password must contain at least six characters!");
    form.password.focus();
    return false;
  }

  if (form.password.value == form.username.value) {
    alert("Error: Password must be different from Username!");
    form.password.focus();
    return false;
  }

  field = /[0-9]/;
  if (!field.test(form.password.value)) {
    alert("Error: password must contain at least one number (0-9)!");
    form.password.focus();
    return false;
  }
  field = /[a-z]/;
  if (!field.test(form.password.value)) {
    alert("Error: password must contain at least one lowercase letter (a-z)!");
    form.password.focus();
    return false;
  }
  field = /[A-Z]/;
  if (!field.test(form.password.value)) {
    alert("Error: password must contain at least one uppercase letter (A-Z)!");
    form.password.focus();
    return false;
  }
  if (form.password.value != form.passwordrepeat.value) {
    alert("Error: Passwords don't match!");
    form.password.focus();
    return false;
  }
}

// Login Validation code ends

//bar chart code

var table = document.getElementById("myTable"),
  sumVal = 0;
var players = [];
var votes = [];
var percentvotes = [];
for (var i = 1; i < table.rows.length; i++) {
  sumVal = sumVal + parseInt(table.rows[i].cells[1].innerHTML);
  players[i] = table.rows[i].cells[0].innerHTML;
  votes[i] = parseInt(table.rows[i].cells[1].innerHTML);
  percentvotes[i] = (votes[i] / sumVal) * 100;
  // players += table.rows[i].cells[0].innerHTML;
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

// var percentageVotes1 = (votes1 / sumVal) * 100;
// var percentageVotes2 = (votes2 / sumVal) * 100;
// var percentageVotes3 = (votes3 / sumVal) * 100;
// var percentageVotes4 = (votes4 / sumVal) * 100;
// var percentageVotes5 = (votes5 / sumVal) * 100;

// // console.log(sumVal);
// console.log(players);
// console.log(player1);
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
  type: 'bar',
  data: {
    // labels:[player1,player2,player3,player4, player5],
    labels: players,
    datasets: [{
      "label": 'Percentage vote',
      // data:[
      //   percentageVotes1,
      //   percentageVotes2,
      //   percentageVotes3,
      //   percentageVotes4,
      //   percentageVotes5
      // ],
      "data": percentvotes
      // backgroundColor:'#009879'
      // backgroundColor:[
      //   'rgba(153,102,255,0.6)',
      //   'rgba(75,192,192,0.6)',
      //   'rgba(255,99,132,0.6)',
      //   // 'rgba(255,159,64,0.6)',
      //   'rgba(54,162,235,0.6)',
      //   'rgba(255,206,86,0.6)'

    }]
  },
  options: {
    maintainAspectRatio: false
  }
});

function updateChart() {
  // chart.data.datasets[0].data = [45, 40, 9, 0, 3];

  chart.update();
}



// loop through HTML table
// 5 global variables for percentages of player votes found by
// looping through column and summing the votes (1 global variable for that)
// divided by specific players votes (another 5 global varaiables)