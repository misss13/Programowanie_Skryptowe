from day import Day

def parsowanie(strink):
    d = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    for i in range(7):
        if d[i]==strink:
            return i

class Term:
    def __init__(self, day, hour, minute):
        self.__day = day
        self.hour=hour
        self.minute=minute
        self.duration=90

    def __str__(self):
        return "%s %02d:%02d [%d]" %(self.__day, self.hour, self.minute, self.duration)

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

    def endTime(self):
        koniec_h, koniec_m = divmod((self.minute+self.duration), 60)
        dy=self.__day
        koniec_h+=self.hour
        if koniec_h >= 24:
            koniec_h%=24
            dy = Day((self.__day.value+1)%7)
        return ("%s %02d:%02d" %(dy, koniec_h, koniec_m))
    
    def setTerm(self, strr, trwania):
        strr.replace('"',"")
        gm=strr.split()
        dzien=gm[0]
        godzina, minuta=gm[1].split(":")
        self.hour=int(godzina)
        self.minute=int(minuta)
        self.duration=trwania
        self.__day=Day(parsowanie(dzien))


