from .termv3 import Term
from .day import Day

class Lesson():
    def __init__(self, timetable, term, name, teacherName, year):
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = self.tryb()    #1 - stacjo
                                          #0 - niestacjo
    def __str__(self):
        ko = self.koniec()
        rok=["Pierwszy", "Drugi", "Trzeci", "Czwarty", "Piąty"]
        rodzaj_studiow=["niestacjonarnych", "stacjonarnych"]
        return"%s (%s %d:%02d-%d:%02d)\n%s rok studiów %s\nProwadzący: %s" %(self.__name, self.__term.day, self.__term.hour, self.__term.minute, ko.hour, ko.minute, rok[self.__year-1], rodzaj_studiow[self.__full_time], self.__teacherName)

    def tryb(self):
        if ( self.__term.day.value >= 0 and self.__term.day.value <= 3 and ( self.__term.hour <= 20 and self.__term.hour >=8)):
            return True
        elif (self.__term.day.value == 4 and self.__term.hour <= 17 and self.__term.hour >=8):
            if self.__term.hour == 17 and self.__term.minute != 0:
                return False
            return True
        else:
            return False

    def koniec(self):
        h, m = divmod(self.__term.duration + self.__term.minute + (self.__term.hour * 60), 60)
        return Term(h, m, self.__term.day, self.__term.duration)

    def poczatek(self):
        h, m = divmod( self.__term.minute - self.__term.duration + (self.__term.hour * 60), 60)
        return Term(h, m, self.__term.day, self.__term.duration)

    def earlierDay(self):
        dzien = Day((self.__term.day.value-1)%7)
        if not self.timetable.can_be_transferred_to(Term(self.__term.hour, self.__term.minute, dzien), self.full_time):
            return False
        self.__term.day = dzien
        return True

    def laterDay(self):
        dzien = Day((self.__term.day.value+1)%7)
        if not self.__timetable.can_be_transferred_to(Term(self.__term.hour, self.__term.minute, dzien), self.full_time):
            return False
        self.__term.day = dzien
        return True
                
    def earlierTime(self):
        ko = self.koniec()
        if not self.__timetable.can_be_transferred_to(ko, self.full_time):
            return False
        self.__term = ko
        return True
        

    def laterTime(self):
        po = self.koniec()
        if not self.__timetable.can_be_transferred_to(po, self.full_time):
            return False
        self.__term = po
        return True

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, value):
        if type(value) is not t_tablele1:
            raise TypeError("To nie jest tabelka")
        else:
            self.__timetable = value

    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError("To nie jest termin!!!")
        else:
            self.__term = value
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Nazwa nie jest stringiem")
        else:
            self.__name = value 
    
    @property
    def teacherName(self):
        return self.__teacherName
    
    @teacherName.setter
    def teacherName(self, value):
        if type(value) is not str:
            raise TypeError("TO NIE STRINK W NAZWIE")
        else:
            self.__teacherName = value
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if type(value) is not int:
            raise TypeError("Rok musi być liczba całkowitą")
        if value > 4 or value < 0:
            raise TypeError("Nie ma takiego roku studiów")
        else:
            self.__year = value
    
    @property
    def full_time(self):
        return self.__full_time

from .timetable import t_tablele1