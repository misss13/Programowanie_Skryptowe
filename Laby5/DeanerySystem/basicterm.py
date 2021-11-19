from .day import Day


class BasicTerm():
    def __init__(self, hour, minute, duration=90):
        self.__hour = int(hour)
        self.__minute = int(minute)
        self.__duration = int(duration)

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, value):
        if type(value) is not int:
            raise TypeError("Godzina musi być liczbą całkowitą")
        elif value < 0 or value > 23:
            raise ValueError("Godzina należy do przedziału 0-23")
        else:
            self.__hour = value
    
    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, value):
        if type(value) is not int:
            raise TypeError("Minuta musi byc liczba całkowitą")
        elif value > 59 or value < 0:
            raise TypeError("Minuta należy do przedziału 0-59")
        else:
            return self.__minute

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        if type(value) is not int:
            TypeError("Czas trwania lekcji nie jest liczbą całkowitą")
        else:
            return self.__duration

    def __str__(self):
        return "%02d:%02d" %(self.__hour, self.__minute)
    
    def start_print(self):
        return "%02d:%02d" %(self.__hour, self.__minute)

    def koniec_print(self):
        h, m = divmod(self.__duration + self.__minute + (self.__hour * 60), 60)
        return "%02d:%02d" %(h, m)
    
    def koniec_h_m(self):
        h, m = divmod(self.__duration + self.__minute + (self.__hour * 60), 60)
        return BasicTerm(h, m, self.__duration)
    
    def getEndTime(self):
        add_hour = self.__duration // 60
        add_min = self.__duration % 60
        end_min = self.__minute + add_min

        if end_min >= 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.__hour + add_hour

        return (end_hour, end_min)
    
    def getStartTime(self):
        return (self.hour, self.minute)
    
    def earlierThan(self, termin):
        if (self.hour < termin.hour ) or (self.hour == termin.hour and self.minute < termin.minute):
            return True
        return False

    def laterThan(self, termin):
        if (self.hour > termin.hour ) or (self.hour == termin.hour and self.minute > termin.minute):
            return True
        return False

    def equals(self, termin):
        if(self.hour == termin.hour) and (self.minute == termin.minute) and ( self.duration == termin.duration):
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
        add_hour, add_min = divmod (self.duration, 60)
        dur = 0
        h = (self.hour + add_hour - ter.hour)%24
        m = (self.minute + add_min - ter.minute)%60
        dur += h * 60 + m
        return Term(ter.hour, ter.minute, Day(ter.day), dur)


class Term(BasicTerm):
    def __init__(self, hour, minute, day, duration=90):
        super().__init__(hour, minute, duration)
        self.day = Day(day)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError("To nie dzień")
        else:
            self.__day=value

    def earlierThan(self, termin):
        if (self.hour < termin.hour ) or (self.hour == termin.hour and self.minute < termin.minute):
            return True
        return False

    def laterThan(self, termin):
        if self.day.value > termin.day.value:
            return True
        elif self.day.value == termin.day.value:
            if (self.hour > termin.hour ) or (self.hour == termin.hour and self.minute > termin.minute):
                return True
            return False
        else:
            False

    def equals(self, termin):
        if (self.day == termin.day) and (self.hour == termin.hour) and (self.minute == termin.minute) and ( self.duration == termin.duration):
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
        add_hour, add_min = divmod (self.duration, 60)
        dur = 0
        h = (self.hour + add_hour - ter.hour)%24
        m = (self.minute + add_min - ter.minute)%60
        dur += h * 60 + m
        return Term(ter.hour, ter.minute, Day(ter.day), dur)