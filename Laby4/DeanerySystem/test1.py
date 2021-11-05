import unittest
from termv2 import Term
from day import Day
from lesson import Lesson

class Test_Term(unittest.TestCase):
    term1 = Term(9, 45, Day.TUE)
    term2 = Term(10, 15, Day.WED)
    term3 = Term(11, 45, Day.SAT)
    term4 = Term(11, 45, Day.WED)
    term5 = Term(9, 45, Day.TUE)

    def test_earlierThen(self):
        self.assertTrue(self.term5 < self.term2)
        self.assertTrue(self.term4 < self.term3)
        self.assertTrue(self.term2 < self.term4)
        self.assertFalse(self.term5 < self.term1)
        self.assertFalse(self.term4 < self.term2)

    def test_laterThen(self):
        self.assertFalse(self.term5 > self.term2)
        self.assertFalse(self.term4 > self.term3)
        self.assertFalse(self.term2 > self.term4)
        self.assertTrue(self.term3 > self.term1)
        self.assertTrue(self.term4 > self.term2)

    def test_equals(self):
        self.assertTrue(self.term5 == self.term5)
        self.assertFalse(self.term4 == self.term3)
        self.assertFalse(self.term2 == self.term4)
        self.assertTrue(self.term5 == self.term1)
        self.assertFalse(self.term4 == self.term2)

    def test_str(self):
        self.assertEqual(self.term1.__str__(), "Wtorek 9:45 [90]")
        self.assertEqual(self.term2.__str__(), "Środa 10:15 [90]")
        self.assertEqual(self.term3.__str__(), "Sobota 11:45 [90]")
        self.assertEqual(self.term4.__str__(), "Środa 11:45 [90]")
        self.assertEqual(self.term5.__str__(), "Wtorek 9:45 [90]")


class Test_Lesson(unittest.TestCase):
    def test_earlierDay(self):
        self.lesson1 = Lesson(Term(8, 0, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson2 = Lesson(Term(8, 30, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson3 = Lesson(Term(18, 40, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson4 = Lesson(Term(18, 30, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson5 = Lesson(Term(16, 0, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(self.lesson1.earlierDay())
        self.assertFalse(self.lesson2.earlierDay())
        self.assertFalse(self.lesson3.earlierDay()) #bo koniec jest o 20:10 a sr
        self.assertTrue(self.lesson4.earlierDay())
        self.assertTrue(self.lesson5.earlierDay())

    def test_laterDay(self):
        self.lesson1 = Lesson(Term(8, 0, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson2 = Lesson(Term(8, 30, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson3 = Lesson(Term(18, 40, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson4 = Lesson(Term(18, 30, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson5 = Lesson(Term(16, 0, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertTrue(self.lesson1.laterDay())
        self.assertTrue(self.lesson2.laterDay())
        self.assertFalse(self.lesson3.laterDay()) #bo koniec jest o 20:10 a sr
        self.assertTrue(self.lesson4.laterDay())
        self.assertFalse(self.lesson5.laterDay())

    def test_earlierTime(self):
        self.lesson1 = Lesson(Term(9, 0, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson2 = Lesson(Term(9, 30, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson3 = Lesson(Term(18, 40, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson4 = Lesson(Term(18, 30, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson5 = Lesson(Term(18, 30, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(self.lesson1.earlierTime())
        self.assertTrue(self.lesson2.earlierTime())
        self.assertTrue(self.lesson3.earlierTime())
        self.assertTrue(self.lesson4.earlierTime())
        self.assertTrue(self.lesson5.earlierTime())

    def test_laterTime(self):
        self.lesson1 = Lesson(Term(9, 0, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson2 = Lesson(Term(9, 30, Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson3 = Lesson(Term(18, 30, Day.WED), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson4 = Lesson(Term(16, 0, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.lesson5 = Lesson(Term(18, 30, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertTrue(self.lesson1.laterTime())
        self.assertTrue(self.lesson2.laterTime())
        self.assertFalse(self.lesson3.laterTime()) #bo koniec jest o 20:10 a środa
        self.assertFalse(self.lesson4.laterTime())
        self.assertFalse(self.lesson5.laterTime())


if __name__ == '__main__':
    unittest.main()