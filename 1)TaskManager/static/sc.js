var clicks = 0;
    function onClick() {
        clicks += 1;
        document.getElementById("clicks").innerHTML = clicks;
    };



var counterVal = 0;

function incrementClick() {
    updateDisplay(++counterVal);
}

function resetCounter() {
    counterVal = 0;
    updateDisplay(counterVal);
}

function updateDisplay(val) {
    document.getElementById("counter-label").innerHTML = val;
}

let blok_login = document.getElementById("login");


document.addEventListener("DOMContentLoaded", (event) => {
    //console.log("DOM fully loaded and parsed");
    //console.log(blok_login);
    //blok_login.innerText="Вход/Регистрация";
    blok_login.innerHTML="<a href=localhost>Вход</a>/<a href=localhost>Регистрация</a>";
  });