class Klasa(object):
    tab = [1,2,3]
    def __init__(self, tablica, _zmienna1, __zmienna2):
        self.tab=tablica
        self._zmienna1=_zmienna1
        self.__zmienna2=__zmienna2
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def __repr__(self):
        return "Wywołano metodę '__repr__()'"

    def metodaInstancyjna(self):
        print("Instancyjna:", self.tab)
        print("Klasowa:", Klasa.tab)
        print("Wywołano metodę 'metodaInstancyjna()'")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")