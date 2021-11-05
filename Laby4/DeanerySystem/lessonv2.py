from termv3 import Term
from day import Day
from action import Action


def koniec(term):
    h, m = divmod(term.duration + term.minute + (term.hour * 60), 60)
    return Term(h, m, term.day, term.duration)

def poczatek(term):
    h, m = divmod( term.minute - term.duration + (term.hour * 60), 60)
    return Term(h, m, term.day, term.duration)

class Lesson():
    def __init__(self, term, name, teacherName, year):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = self.tryb()    #1 - stacjo
                                          #0 - niestacjo
    def __str__(self):
        ko=koniec(self.__term)
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

#       stacjo
# Term(20, 00, Day.THU)
# Term(8, 00, Day.MON)
# Term(8, 00, Day.FRI)
# Term(17, 00, Day.FRI)
#      niestacjo
# Term(20, 00, Day.SUN)
# Term(8, 00, Day.SAT)
# Term(20, 00, Day.FRI)
# Term(17, 00, Day.FRI)

    def earlierDay(self):
        ko=koniec(self.__term)
        ko.day=Day((self.__term.day.value-1)%7)
        if self.__full_time == 1: #stacjo
            if ko.day == Day.SAT or ko.day == Day.SUN:
                return False
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko>= Term(8, 00, d)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.__term=Term(self.__term.hour, self.__term.minute, ko.day)
                return True
            else:
                return False
        else: #niestacjo
            if ko.__term.day >= Day.MON and ko.__term.day <= Day.THU:
                return False
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.__term=Term(self.__term.hour, self.__term.minute, ko.day)
                return True
            else:
                return False

    def laterDay(self):
        ko=koniec(self.__term)
        ko.day=Day((self.__term.day.value+1)%7)
        if self.__full_time == 1: #stacjo
            if(ko <= Term(20, 00, Day.THU) and ko >= Term(8, 00, Day.MON)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.__term=Term(self.__term.hour, self.__term.minute, ko.day)
                return True
            else:
                return False
        else: #niestacjo
            if(ko <= Term(20, 00, Day.SUN) and ko >= Term(8, 00, Day.SAT)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.__term=Term(self.__term.hour, self.__term.minute, ko.day)
                return True
            else:
                return False
                
    def earlierTime(self):
        po=poczatek(self.__term)
        ko=self.__term
        if self.__full_time == 1: #stacjo
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and po >= Term(8, 00, d)) or ( (po >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.__term=po
                return True
            else:
                return False
        else: #niestacjo
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and po >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and po >= Term(17, 00, Day.FRI)):
                self.__term=po
                return True
            else:
                return False

    def laterTime(self):
        o=koniec(self.__term)
        ko=koniec(o)
        if self.__full_time == 1: #stacjo
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.__term=o
                return True
            else:
                return False
        else: #niestacjo
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.__term=o
                return True
            else:
                return False

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

lesson = Lesson(Term(18, 0, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
print(lesson)
lesson.earlierTime()
print(lesson)
