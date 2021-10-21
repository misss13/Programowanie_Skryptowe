import re


def wypisywanie(napis):
    liczby=re.findall('[0-9]+', napis) #cyfry 0-9 albo + oznacza ciągi z nimi
    wyraz=re.findall('[a-zćąóżźłęśń]+', napis, flags=re.IGNORECASE)
    if(len(liczby)>0):
        print("Liczba: ", *liczby)
    if(len(wyraz)>0):
        print("Wyraz: ", *wyraz)


def s():
    while True:
        try:
            n=input()
        except:
            break
        wypisywanie(n)


if __name__=="__main__":
    s()