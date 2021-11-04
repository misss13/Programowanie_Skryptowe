from day import Day

class Term:
    def __init__(self, hour, minute, duration=90):
        self.hour=hour
        self.minute=minute
        self.duration=duration

    def __str__(self):
        return "%d:%02d [%d]" %(self.hour, self.minute, self.duration)

    def earlierThan(self, termin):
        if (self.hour < termin.hour ) or (self.hour == termin.hour and self.minute < termin.minute):
            return True
        return False

    def laterThan(self, termin):
        if (self.hour > termin.hour ) or (self.hour == termin.hour and self.minute > termin.minute):
            return True
        return False

    def equals(self, termin):
        if (self.hour == termin.hour) and (self.minute == termin.minute) and ( self.duration == termin.duration):
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
        return Term(ter.hour, ter.minute, dur)