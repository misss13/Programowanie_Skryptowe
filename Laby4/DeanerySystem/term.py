from day import Day

class Term:
    def __init__(self, hour, minute, day):
        self.__day = day
        self.hour=hour
        self.minute=minute
        self.duration=90

    def __str__(self):
        return "%s %d:%d [%d]" %(self.__day, self.hour, self.minute, self.duration)

    def earlierThan(self, termin):
        if self.__day.difference(termin.__day) > 0:
            return True
        elif self.__day.difference(termin.__day) == 0:
            if (self.hour < termin.hour ) or (self.hour == termin.hour and self.minute < termin.minute):
                return True
            return False

    def laterThan(self, termin):
        if self.__day.difference(termin.__day) < 0:
            return True
        elif self.__day.difference(termin.__day) == 0:
            if (self.hour > termin.hour ) or (self.hour == termin.hour and self.minute > termin.minute):
                return True
            return False

    def equals(self, termin):
        if (self.__day == termin.__day) and (self.hour == termin.hour) and (self.minute == termin.minute) and ( self.duration == termin.duration):
            return True
        return False
