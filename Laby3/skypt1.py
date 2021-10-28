from klasa import Klasa

if __name__=="__main__":
    obiekt = Klasa([4, 5, 6], 10, 20)
    print("Zmienna chroniona: ", obiekt._zmienna1)
    print("Zmienna prywatna: ", obiekt._Klasa__zmienna2)