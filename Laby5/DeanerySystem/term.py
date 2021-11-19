from .day import Day
from .basicterm import BasicTerm

class Term(BasicTerm):
    def __init__(self, hour, minute, day, duration=90):
        super().__init__(hour, minute, duration)
        self.__day = Day(day)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError("To nie dzień")
        else:
            self.__day=value

    def __str__(self):
        return "%02d:%02d" %(self.__hour, self.__minute)

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if (self.__hour < termin.__hour ) or (self.__hour == termin.__hour and self.__minute < termin.__minute):
                return True
            return False
        else:
            return False

    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if (self.__hour > termin.__hour ) or (self.__hour == termin.__hour and self.__minute > termin.__minute):
                return True
            return False
        else:
            False

    def equals(self, termin):
        if (self.__day == termin.__day) and (self.__hour == termin.__hour) and (self.__minute == termin.__minute) and ( self.__duration == termin.__duration):
            return True
        return False
    
    #override
    def __lt__(self, ter):
        return self.earlierThan(ter)
    
    def __gt__(self, ter):
        return self.laterThan(ter)
    
    def __le__(self, ter):
        return (self.earlierThan(ter) or self.equals(ter))
    
    def __ge__(self, ter):
        return (self.laterThan(ter) or self.equals(ter))
    
    def __eq__(self, ter):
        return self.equals(ter)
    
    def __sub__(self, ter):
        add_hour, add_min = divmod (self.__duration, 60)
        dur = 0
        h = (self.__hour + add_hour - ter.__hour)%24
        m = (self.__minute + add_min - ter.__minute)%60
        dur += h * 60 + m
        return Term(ter.__hour, ter.__minute, Day(ter.__day), dur)

    def start_print(self):
        return "%02d:%02d" %(self.__hour, self.__minute)

    def koniec_print(self):
        h, m = divmod(self.__duration + self.__minute + (self.__hour * 60), 60)
        return "%02d:%02d" %(h, m)
    
    def koniec_h_m(self):
        h, m = divmod(self.__duration + self.__minute + (self.__hour * 60), 60)
        return Term(h, m, self.__day, self.__duration)
    
    def getEndTime(self):
        add_hour = self.__duration // 60
        add_min = self.__duration % 60
        end_min = self.__minute + add_min

        if end_min >= 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.__hour + add_hour

        return (end_hour, end_min)