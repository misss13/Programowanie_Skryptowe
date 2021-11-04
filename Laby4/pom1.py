from term import Term
from day import Day

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
        return"%s (%s %d:%02d-%d:%02d)\n%s rok studiów %s\nProwadzący: %s" %(self.name, self.term._day, self.term.hour, self.term.minute, h, m, rok[self.year-1], rodzaj_studiow[self.full_time], self.teacherName)

    def tryb(self):
        if ( self.term._day.value >= 0 and self.term._day.value <= 3 and ( self.term.hour <= 20 and self.term.hour >=8)):
            return True
        elif (self.term._day.value == 4 and self.term.hour <= 17 and self.term.hour >=8):
            if self.term.hour == 17 and self.term.minute != 0:
                return False
            return True
        else:
            return False

    def earlierDay(self):
        d=(self.term._day.value+1)%7
        if self.full_time == 0: #niestacjo
            if d >=0 and d <=3:
                return False
            elif d == 4 and self.term.hour >= 17 and  self.term.hour <= 20:
                if self.term.hour == 20 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
        else: #stacjo
            if d >=5 and d <=6:
                return False
            elif d == 4 and self.term.hour >= 8 and  self.term.hour <= 17:
                if self.term.hour == 17 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
    def laterDay(self):
        d=(self.term._day.value-1)%7
        if self.full_time == 0: #niestacjo
            if d >=0 and d <=3:
                return False
            elif d == 4 and self.term.hour >= 17 and  self.term.hour <= 20:
                if self.term.hour == 20 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
        else: #stacjo
            if d >=5 and d <=6:
                return False
            elif d == 4 and self.term.hour >= 8 and  self.term.hour <= 17:
                if self.term.hour == 17 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
                
    def earlierTime(self):
        d=(self.term._day.value+1)%7
        if self.full_time == 0: #niestacjo
            if d >=0 and d <=3:
                return False
            elif d == 4 and self.term.hour >= 17 and  self.term.hour <= 20:
                if self.term.hour == 20 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
        else: #stacjo
            if d >=5 and d <=6:
                return False
            elif d == 4 and self.term.hour >= 8 and  self.term.hour <= 17:
                if self.term.hour == 17 and self.term.minute != 0:
                    return False
                self.term._day =d
                return True
            else:
                self.term._day = Day(d)
                return True 
    def laterTime(self):
        print("Yo :3")


lesson = Lesson(Term(17, 00, Day.THU), "Programowanie skryptowe", "Stanisław Polak", 5)
print(lesson)
lesson.earlierDay()
print(lesson)