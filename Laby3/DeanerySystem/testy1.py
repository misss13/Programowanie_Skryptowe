import unittest
from day import Day
from term1 import Term
from day import nthDayFrom

class Test_TestDeanerySystem(unittest.TestCase):

    def test_term_earlierThan(self):
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.WED, 10, 15)))
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.TUE, 10, 15)))
        self.assertFalse(Term(Day.FRI, 8, 45).earlierThan(Term(Day.TUE, 9, 50)))#false
        self.assertFalse(Term(Day.FRI, 7, 45).earlierThan(Term(Day.WED, 9, 40))) 

    def test_term_laterThan(self):
        self.assertTrue(Term(Day.WED, 10, 15).laterThan(Term(Day.TUE, 9, 45)))
        self.assertTrue(Term(Day.TUE, 10, 15).laterThan(Term(Day.TUE, 9, 45)))
        self.assertFalse(Term(Day.MON, 9, 50).laterThan(Term(Day.TUE, 9, 45)))
        self.assertFalse(Term(Day.TUE, 5, 10).laterThan(Term(Day.TUE, 5, 11)))

    def test_term_equals(self):
        self.assertTrue(Term(Day.TUE, 9, 45).equals(Term(Day.TUE, 9, 45)))
        self.assertTrue(Term(Day.MON, 10, 15).equals(Term(Day.MON, 10, 15)))
        self.assertFalse(Term(Day.TUE, 9, 40).equals(Term(Day.TUE, 10, 40)))
        self.assertFalse(Term(Day.MON, 10, 40).equals(Term(Day.TUE, 9, 45)))

    def test_nthDayFrom(self):
        self.assertEqual(nthDayFrom(1, Day.SAT), Day.SUN)
        self.assertEqual(nthDayFrom(2, Day.SAT), Day.MON)
        self.assertEqual(nthDayFrom(-1, Day.TUE), Day.MON)
        self.assertEqual(nthDayFrom(-2, Day.TUE), Day.SUN)

    def test_difference(self):
        self.assertEqual(Day.MON.difference(Day.TUE), 1)
        self.assertEqual(Day.MON.difference(Day.SUN), -1)
        self.assertEqual(Day.SUN.difference(Day.MON), 1)
        self.assertEqual(Day.SUN.difference(Day.SAT), -1)

    def test_endTime(self):
        self.assertEqual(Term(Day.TUE, 9, 45).endTime(),"Wtorek 11:15" )
        self.assertEqual(Term(Day.MON, 9, 00).endTime(),"Poniedziałek 10:30" )
        self.assertEqual(Term(Day.FRI, 9, 45).endTime(),"Piątek 11:15" )
        self.assertEqual(Term(Day.FRI, 10,10 ).endTime(),"Piątek 11:40" )

    def test_setTerm(self):
        t=Term(Day.FRI, 9, 45)
        t.setTerm("Wtorek 11:15", 1440)
        self.assertEqual(t.__str__(),"Wtorek 11:15 [1440]")
        t.setTerm("Środa 00:00", 1440)
        self.assertEqual(t.__str__(),"Środa 00:00 [1440]")
        t.setTerm("Środa 8:00", 510)
        print(t)
        print(t.endTime())
        self.assertEqual(t.__str__(),"Środa 08:00 [30]")

if __name__ == '__main__':
    unittest.main()