from enum import Enum

class Day(Enum):

    MON=0 
    TUE=1
    WED=2
    THU=3
    FRI=4
    SAT=5
    SUN=6

    def difference(self, day):
        roz = day.value - self.value
        if roz > 3:
            return roz - 7
        elif roz < -3:
            return roz + 7
        else:
            return roz


def nthDayFrom(n, day):
        return Day((day.value+n)%7)