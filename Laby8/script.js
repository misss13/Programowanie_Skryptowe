var paragraph = document.getElementById("p");
var button = document.getElementById('guzikk');
function wypisanie() {
    paragraph.textContent = "tekst: ";
    paragraph.textContent += document.forms[0].elements[0].value;
    // string dla liczby
    // string dla tekstu
    // pusty string dla braku wartości
    paragraph.textContent += " wartość: ";
    paragraph.textContent += document.forms[0].elements[1].value;
    // string dla liczby
    // pusty string dla tekstu
    // pusty string dla braku wartości
}
button.onclick = wypisanie;