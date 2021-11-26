from inspect import signature
from typing import Type

def argumenty(lista_argumentow_Operacyjne):
    #pobieram pzekazany argument z tablicą do args a właściwie 2 tablice dla odpowiedniej funkcji inne
    def argumenty_inner(funkcja):
        #pobieram funkcje
        def argumenty_argumenty(*karg):
            #pobieram podane do funkcji argumenty pierwsza wartosc to gdzie jest funkcja <__main__.Operacje object at 0x7fa439445e80>
            lista_argumentow_funkcji = list(karg)
            dlugosc_minimalna_do_operacji = len(list(signature(funkcja).parameters)) #sumy/różnicy
            dlugosc_lista_argumentow_funkcji = len(lista_argumentow_funkcji)
            dlugosc_lista_argumentow_Operacyjne = len(lista_argumentow_Operacyjne)
            #print(lista_argumentow_funkcji)
            #print(lista_argumentow_Operacyjne)
            #print(dlugosc_minimalna_do_operacji)
            
            if dlugosc_lista_argumentow_funkcji + dlugosc_lista_argumentow_Operacyjne < dlugosc_minimalna_do_operacji:
                raise TypeError(str(funkcja.__name__) + " takes exactly "+str(dlugosc_minimalna_do_operacji-1)+" arguments (" + str(len(lista_argumentow_funkcji)-1) + " given)")
            i = 0
            while(len(lista_argumentow_funkcji) < dlugosc_minimalna_do_operacji):
                lista_argumentow_funkcji.append(lista_argumentow_Operacyjne[i])
                i+=1
            funkcja(*lista_argumentow_funkcji)

            #do zwracania wartosci wynik -.-
            try:
                return lista_argumentow_Operacyjne[i]
            except:
                return None

        return argumenty_argumenty
    return argumenty_inner

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print("%d+%d+%d=%d" %(a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self, x ,y):
        print("%d-%d=%d" % (x,y,x-y))

    def suma_kop(self, a, b, c): #zeby sie zapdejtowaly argumenty roznica
        print("%d+%d+%d=%d" %(a,b,c,a+b+c))

    def roznica_kop(self, x ,y):
        print("%d-%d=%d" % (x,y,x-y))
    
    def __setitem__(self,name,numbers):
        if name == 'suma':
            self.argumentySuma = numbers
            self.suma = argumenty(self.argumentySuma)(self.suma_kop)
        elif name == 'roznica':
            self.argumentyRoznica = numbers
            self.roznica = argumenty(self.argumentyRoznica)(self.roznica_kop)