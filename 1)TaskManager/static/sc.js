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