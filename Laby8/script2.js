"use strict";

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

describe('The sum() function', function() {
 it('Returns 4 for 2+2', function() {
   expect(sum(2,2)).to.equal(4);
 });
 it('Returns 0 for -2+2', function() {
   expect(sum(-2,2)).to.equal(0);
 });
});


var wszy =0;

function cyfry(napis) {
    var cyferki = napis.replace(/[^0-9]/g, '')
    cyferki = cyferki.split('')

    if (cyferki.length == 0)
        return 0

    var i = 0;
    var sum = 0;
    while (i < cyferki.length) {
        sum += parseInt(cyferki[i]);
        i++;
    }
    if (isNaN(sum)) {
        return 0
    } else {
        return sum
    }
}

function litery(napis) {
    napis = napis.replace(/[0-9]/g, '');
    return napis.length;
}

function suma(napis) {
    var liczba = parseInt(napis)
    if (!isNaN(liczba))
        wszy += liczba
    return wszy
}

var dane = ''
while (true) {
    dane = window.prompt('Podaj dane')
    if (dane == null)
        break
    console.log('\t' + cyfry(dane) + '\t' + litery(dane) + '\t' + suma(dane));
}

describe("The cyfry() litery() suma() functions", function() {
    wszy = 0
    // 111 -> 3 0 111
    it("cyfry_Same_cyfry", function() {
        expect(cyfry('111')).to.equal(3)
    })
    it("litery_Same_Cyfry", function() {
        expect(litery('111')).to.equal(0)
    })
    it("suma_Same_Cyfry", function() {
        expect(suma('111')).to.equal(111)
    })
    // ala -> 0 3 111
    it("cyfry_Same_Litery", function() {
        expect(cyfry('ala')).to.equal(0)
    })
    it("litery_Same_Litery", function() {
        expect(litery('ala')).to.equal(3)
    })
    it("suma_Same_Litery", function() {
        expect(suma('ala')).to.equal(111)
    })
    //b3345a -> 15 2 111
    it("cyfry_Litery_a_po_nich_cyfry", function() {
        expect(cyfry('b3345a')).to.equal(15)
    })
    it("litery_Litery_a_po_nich_cyfry", function() {
        expect(litery('b3345a')).to.equal(2)
    })
    it("suma_Litery_a_po_nich_cyfry", function() {
        expect(suma('b3345a')).to.equal(111)
    })
    //11aa -> 2 2 122
    it("cyfry_Cyfry_a_po_nich_litery", function() {
        expect(cyfry('11aa')).to.equal(2)
    })
    it("litery_Cyfry_a_po_nich_litery", function() {
        expect(litery('11aa')).to.equal(2)
    })
    it("suma_Cyfry_a_po_nich_litery", function() {
        expect(suma('11aa')).to.equal(122)
    })
    // -> 0 0 122
    it("cyfry_Pusty_napis", function() {
        expect(cyfry('')).to.equal(0)
    })
    it("litery_Pusty_napis", function() {
        expect(litery('')).to.equal(0)
    })
    it("suma_Pusty_napis", function() {
        expect(suma('')).to.equal(122)
    })
})