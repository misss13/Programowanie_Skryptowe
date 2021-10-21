import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], 'm', ["moduł:="])
except getopt.GetoptError as err:
    print("złe parametry")
    quit()

pom=0
print(opts)
for opcja, argument in opts:
    if opcja == '--moduł:' and argument =='lista':
        import lista
        pom=1
    if opcja == '--moduł:' and argument =='słownik':
        import slownik
        pom=2

if __name__ == "__main__":
    while pom!=0:
        try:
            strink = input()
        except:
            print("koncze program")
            break
        if pom==1:
            lista.zapisz(strink)
            lista.wypisz()
        else:
            slownik.zapisz(strink)
            slownik.wypisz()