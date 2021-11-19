from .basicterm import BasicTerm

class Break:
    def __init__(self, term: BasicTerm):
        self.__term = term

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        if type(value) is not BasicTerm:
            raise TypeError('TO NIE BASICTERM!!!')
        else:
            self.__term = value

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return str(self.__term)