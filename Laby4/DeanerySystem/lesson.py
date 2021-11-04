from termv2 import Term
from day import Day

def koniec(term):
    h, m = divmod(term.duration + term.minute + (term.hour * 60), 60)
    return Term(h, m, term.day, term.duration)

def poczatek(term):
    h, m = divmod( term.minute - term.duration + (term.hour * 60), 60)
    return Term(h, m, term.day, term.duration)

class Lesson():
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = str(name)
        self.teacherName = str(teacherName)
        self.year = int(year)
        self.full_time = self.tryb()    #1 - stacjo
                                        #0 - niestacjo
    def __str__(self):
        h, m = divmod(self.term.duration + self.term.minute + (self.term.hour * 60), 60)
        rok=["Pierwszy", "Drugi", "Trzeci", "Czwarty", "Piąty"]
        rodzaj_studiow=["niestacjonarnych", "stacjonarnych"]
        return"%s (%s %d:%02d-%d:%02d)\n%s rok studiów %s\nProwadzący: %s" %(self.name, self.term.day, self.term.hour, self.term.minute, h, m, rok[self.year-1], rodzaj_studiow[self.full_time], self.teacherName)

    def tryb(self):
        if ( self.term.day.value >= 0 and self.term.day.value <= 3 and ( self.term.hour <= 20 and self.term.hour >=8)):
            return True
        elif (self.term.day.value == 4 and self.term.hour <= 17 and self.term.hour >=8):
            if self.term.hour == 17 and self.term.minute != 0:
                return False
            return True
        else:
            return False

# Term(20, 00, Day.THU)
# Term(8, 00, Day.MON)
# Term(8, 00, Day.FRI)
# Term(17, 00, Day.FRI)

# Term(20, 00, Day.SUN)
# Term(8, 00, Day.SAT)
# Term(20, 00, Day.FRI)
# Term(17, 00, Day.FRI)

    def earlierDay(self):
        ko=koniec(self.term)
        ko.day=Day((self.term.day.value-1)%7)
        if self.full_time == 1: #stacjo
            if ko.day == Day.SAT and ko.day == Day.SUN:
                return False
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko>= Term(8, 00, d)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.term=Term(self.term.hour, self.term.minute, ko.day)
                return True
            else:
                return False
        else: #niestacjo
            if ko.term.day >= Day.MON and ko.term.day <= Day.THU:
                return False
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.term=Term(self.term.hour, self.term.minute, ko.day)
                return True
            else:
                return False

    def laterDay(self):
        ko=koniec(self.term)
        ko.day=Day((self.term.day.value+1)%7)
        if self.full_time == 1: #stacjo
            if(ko <= Term(20, 00, Day.THU) and ko >= Term(8, 00, Day.MON)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.term=Term(self.term.hour, self.term.minute, ko.day)
                return True
            else:
                return False
        else: #niestacjo
            if(ko <= Term(20, 00, Day.SUN) and ko >= Term(8, 00, Day.SAT)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.term=Term(self.term.hour, self.term.minute, ko.day)
                return True
            else:
                return False
                
    def earlierTime(self):
        po=poczatek(self.term)
        ko=self.term
        if self.full_time == 1: #stacjo
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and po >= Term(8, 00, d)) or ( (po >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.term=po
                return True
            else:
                return False
        else: #niestacjo
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and po >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and po >= Term(17, 00, Day.FRI)):
                self.term=po
                return True
            else:
                return False

    def laterTime(self):
        o=koniec(self.term)
        ko=koniec(o)
        if self.full_time == 1: #stacjo
            d=Day.MON
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or ( (ko >= Term(8, 00, Day.FRI)) and (ko <= Term(17, 00, Day.FRI)) ):
                self.term=o
                return True
            else:
                return False
        else: #niestacjo
            d=Day.SAT
            if ko.day != Day.FRI:
                d=ko.day
            if(ko <= Term(20, 00, d) and ko >= Term(8, 00, d)) or (ko <= Term(20, 00, Day.FRI) and ko >= Term(17, 00, Day.FRI)):
                self.term=o
                return True
            else:
                return False


lesson = Lesson(Term(17, 0, Day.SUN), "Programowanie skryptowe", "Stanisław Polak", 2)
print(lesson)
lesson.laterDay()
lesson.laterTime()
print(lesson)
lesson.earlierTime()
print(lesson)
lesson.earlierTime()
print(lesson)
lesson.earlierTime()
lesson.earlierTime()
print(lesson)
lesson.earlierTime()
print(lesson)
lesson.earlierTime()
lesson.earlierTime()
print(lesson)
print(lesson.earlierTime())