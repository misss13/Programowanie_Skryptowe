from logging import setLoggerClass
import unittest
from day import Day
from term1 import Term

class Zadanie_z_labow4(unittest.TestCase):
    def test_dur1(self):
       term = Term(Day.TUE, 9 ,45)
       term.setTerm("Środa 8:00", 510)
       self.assertEqual(term.__str__(), "Środa 08:00 [30]")
    
    def test_dur2(self):
        term=Term(Day.TUE, 9 ,45)
        term.setTerm("Środa 00:00", 1440)
        self.assertEqual(term.__str__(), "Środa 00:00 [1440]")
    
    def test_dur3(self):
       term = Term(Day.TUE, 9 ,45)
       term.setTerm("Środa 8:00", 520)
       self.assertEqual(term.__str__(), "Środa 08:00 [40]")

    def test_end1(self):
        term = Term(Day.WED, 8 ,0, 30)
        self.assertEqual(term.endTime(), "Środa 08:30")
    
    def test_end2(self):
        term = Term(Day.WED, 0 ,0, 1440)
        self.assertEqual(term.endTime(), "Czwartek 00:00")
    
    def test_end3(self):
        term = Term(Day.MON, 0 ,0, 2880)
        self.assertEqual(term.endTime(), "Środa 00:00")

if __name__ == "__main__":
    unittest.main()