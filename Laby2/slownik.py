print('Ładowanie modułu "{0}"'.format(__name__))
############################################
slownik = dict()


def zapisz(string):
    for znak in string:
        if((znak <='9') and (znak >='0')):
            if znak in slownik:
                slownik[znak]+=1
            else:
                slownik[znak]=1


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for i in slownik:
        print("%s:%d" %(i, slownik[i]), end="")
        if(i != sorted(slownik.keys())[-1]):
            print(",", end="")
    print('')


############################################
print('Załadowano moduł "{0}"'.format(__name__))