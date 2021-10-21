print('Ładowanie modułu "{0}"'.format(__name__))
############################################
lista = list()


def zapisz(string):
    for znak in string:
        pom=1
        if((znak <='9') and (znak >='0')):
            for cyfra in lista:
                if(cyfra[0] == znak):
                    cyfra[1]=cyfra[1]+1
                    pom = 0
            if(pom==1):
                lista.append([znak, 1])

def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for i in range(len(lista)):
        print("%s:%d" %(lista[i][0], lista[i][1]), end="")
        if(i != len(lista)-1):
            print(",", end="")
    print('')


############################################
print('Załadowano moduł "{0}"'.format(__name__))