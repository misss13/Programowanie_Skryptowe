import sys


if __name__ == "__main__":
    for arg in sys.argv[1::]:
        opcja=str(arg)

    pom=0
    if opcja == "--lista":
        import lista
        pom=1
    if opcja ==  "--słownik":
        import slownik
        pom=2

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