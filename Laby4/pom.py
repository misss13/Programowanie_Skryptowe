class jakas():
    def __init__(self, val):
        self.__a = val
    
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        self.__a = val

