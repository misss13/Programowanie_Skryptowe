var button = document.getElementById('guzikk');
function wypisanie() {
    alert("YOOOO")
    console.log(document.forms[0].elements[0].value);
}
button.onclick = wypisanie;

/**describe("Testy", function() {
    wszy = 0
    it("cyfry_Same_cyfry", function() {
        expect(cyfry('111')).to.equal(3)
    })
})**/