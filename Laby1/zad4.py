import sys

if __name__ == "__main__":
    for arg in sys.argv[1::]:
        liczba_osob_=int(arg)
    
    print("Dodawanie_osob: [z/w]:[kurs]:[nazwisko]")
    operacje = []
    kursy = {}
    zawartosc_operacji = [[0 for x in range(3)] for y in range(liczba_osob_)]
    i=0
    while True:
        try:
            b=input()
            if b == '':
                print("Puste pole - nie wprowadzam")
            else:
                operacje.append(b)
                try:
                    zawartosc_operacji[i] = operacje[i].split(sep=":")
                except:
                    print("Nie psuj mi tego!!!")
                    i+=1
                    break
                if((zawartosc_operacji[i][0] != 'w') and (zawartosc_operacji[i][0] != 'z')):
                    print("Zła opcja usuwam wpis")
                    zawartosc_operacji.pop(i)
                    operacje.pop(i)
                else:
                    if(zawartosc_operacji[i][0]=="z"):
                        #tutaj jest zapis
                        if(zawartosc_operacji[i][1] in kursy.keys() and len(kursy[zawartosc_operacji[i][1]])<= liczba_osob_):
                            kursy.setdefault(zawartosc_operacji[i][1], []).append(zawartosc_operacji[i][2])
                            print("Dodano ", zawartosc_operacji[i][2], " do istniejacego kursu ", zawartosc_operacji[i][1])
                        else:
                            kursy[zawartosc_operacji[i][1]]=[zawartosc_operacji[i][2]]
                            print("Dodano ", zawartosc_operacji[i][2], " do nowego kursu ", zawartosc_operacji[i][1])
                    else:
                        #tutaj wypis
                        if zawartosc_operacji[i][1] in kursy.keys():
                            del kursy[zawartosc_operacji[i][1]]
                        else:
                            print("Złe zapytanie nic nie robie")
                i+=1
        except EOFError:
            break
    
    print("Usuwanie kursów: [kurs]:[m-modyfikuj,d-dodaj,u-usuń]")
    print(kursy)