var click, typing, date;

function Clicar() {
  click = document.getElementById("clicar");
  if (click.style.display === "none") {
    click.style.display = "block";
    typing = document.getElementById("typing");
    setTimeout(function () {
      hide(typing);
      show(message);
    }, 2000);
    function hide(element) {
      element.style.display = "none";
    }
    function show(element) {
      element.style.display = "block";
    }
  } else {
    click.style.display = "none";
  }
}

date = new Date();
document.getElementById("date-time").innerHTML =
  date.getHours() + ":" + date.getMinutes();
