from zadanie1 import Operacje

op=Operacje()
op.suma(1,2,3) #Wypisze: 1+2+3=6
op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
#op.suma() #TypeError: suma() takes exactly 3 arguments (2 given) - wypisuje i zatrzymuje program
op.roznica(2,1) #Wypisze: 2-1=1
op.roznica(2) #Wypisze: 2-4=-2
wynik=op.roznica() #Wypisze: 4-5=-1
print(wynik) #Wypisze: 6

#Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
op['suma']=[1,2]
#oznacza, że   argumentySuma=[1,2]
op.suma(1)
#Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
op['roznica']=[1,2,3]
op.roznica(1,2)
#oznacza, że   argumentyRoznica=[1,2,3]