import sys

if __name__ == "__main__":
    for arg in sys.argv[1::]:
        liczba_osob_=int(arg)
    
    print("Dodawanie_osob: [z/w]:[kurs]:[nazwisko]")
    operacje = []
    kursy = {}
    zawartosc_operacji = [[0 for x in range(3)] for y in range(liczba_osob_+2)]
    i=0
    while True:
        try:
            b=input()
            if (b == '') or (b.count(':') != 2):
                print("Coś jest nie tak - nie wprowadzam")
            else:
                operacje.append(b)
                try:
                    zawartosc_operacji[i] = operacje[i].split(sep=":")
                except:
                    continue
                if((zawartosc_operacji[i][0] != 'w') and (zawartosc_operacji[i][0] != 'z')):
                    print("Zła opcja [z/w] usuwam wpis")
                    zawartosc_operacji.pop(i)
                    operacje.pop(i)
                    i-=1
                else:
                    if(zawartosc_operacji[i][0]=="z"):
                        #tutaj jest zapis osoby na kurs
                        if(zawartosc_operacji[i][1] in kursy.keys()):
                            if(len(kursy[zawartosc_operacji[i][1]])< liczba_osob_):
                                kursy.setdefault(zawartosc_operacji[i][1], []).append(zawartosc_operacji[i][2])
                                print("Dodano ", zawartosc_operacji[i][2], " do istniejacego kursu ", zawartosc_operacji[i][1])
                            else:
                                print("Maxymalna liczba osób w kursie osiągnięta - nie wpisuje")
                        else:
                            kursy[zawartosc_operacji[i][1]]=[zawartosc_operacji[i][2]]
                            print("Dodano ", zawartosc_operacji[i][2], " do nowego kursu ", zawartosc_operacji[i][1])
                    else:
                        #tutaj wypis osoby z kursu
                        if zawartosc_operacji[i][1] in kursy.keys():
                            if len(kursy[zawartosc_operacji[i][1]])==1:
                                print("Usuwam ",zawartosc_operacji[i][2]," z kursu i kurs", zawartosc_operacji[i][1]," bo nikogo w nim nie ma")
                                del kursy[zawartosc_operacji[i][1]]
                            else:
                                print("Usuwam ",zawartosc_operacji[i][2]," z kursu ", zawartosc_operacji[i][1])
                                print(zawartosc_operacji[i][2])
                                kursy[zawartosc_operacji[i][1]].remove(zawartosc_operacji[i][2])
                        else:
                            print("Złe zapytanie nic nie robie")
                i+=1
        except EOFError:
            break

    #K U R S Y
    print(kursy)
    print("Opcje kursów: [m-modyfikuj,d-dodaj,u-usuń]:[kurs]")
    zawartosc_operacji = [[0 for x in range(2)] for y in range(20)]
    operacje = []
    i=0
    while True:
        try:
            b=input()
            if (b == '') or (b.count(':') != 1):
                print("Coś jest nie tak - nie wprowadzam")
            else:
                operacje.append(b)
                try:
                    zawartosc_operacji[i] = operacje[i].split(sep=":")
                except:
                    continue
                if((zawartosc_operacji[i][0] != 'm') and (zawartosc_operacji[i][0] != 'd') and (zawartosc_operacji[i][0] != 'u')):
                    print("Zła opcja [m/d/u] usuwam wpis")
                    zawartosc_operacji.pop(i)
                    operacje.pop(i)
                    i-=1
                else:
                    if(zawartosc_operacji[i][0]=="d"):
                        #tutaj jest dodawanie kursu
                        if(zawartosc_operacji[i][1] in kursy.keys()):
                           print("Taki kurs już istnieje")
                        else:
                            kursy[zawartosc_operacji[i][1]]=[]
                            print("Dodano kurs", zawartosc_operacji[i][1])
                    if(zawartosc_operacji[i][0]=="u"):
                        #usuwanie kursu
                        if(zawartosc_operacji[i][1] in kursy.keys()):
                            del kursy[zawartosc_operacji[i][1]]
                        else:
                           print("Nie ma takiego kursu - nic nie robie") 
                    if(zawartosc_operacji[i][0]=="m"):
                        #tutaj jest modyfikacja kursu
                        if(zawartosc_operacji[i][1] in kursy.keys()):
                            nazwa=input("Podaj nową nazwę kursu: ")
                            kursy[nazwa]=kursy.pop(zawartosc_operacji[i][1])
                        else:
                           print("Nie ma takiego kursu - nic nie robie") 

                i+=1
        except EOFError:
            break
    print()
    #listowanie kursów i zapisanych w nich osób
    print("Kurs\tOsoby w kursie")
    for kurs in kursy:
        print(kurs, "\t", kursy[kurs])