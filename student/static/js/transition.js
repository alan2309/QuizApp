var opacity = 0;
var intervalID = 0;
window.onload = fadeIn;

function fadeIn() {
    setInterval(show, 50);
}

function show() {
    var card = document.getElementById("card");
    opacity = Number(window.getComputedStyle(card).getPropertyValue("opacity"));
    if (opacity < 1) {
        opacity = opacity + 0.1;
        card.style.opacity = opacity
    } else {
        clearInterval(intervalID);
    }
}