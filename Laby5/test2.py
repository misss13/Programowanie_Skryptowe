import unittest
from DeanerySystem import Day, Term, Lesson, Action, Timetable1 

class Test_TestTimetable1(unittest.TestCase):

    def test_put(self):
        tab1 = Timetable1()
        les0 = Lesson(tab1, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tab1.put(les0), True)

    def test_put_err(self):
        tab1 = Timetable1()
        les0 = Lesson(tab1, Term(9, 35, Day.TUE), "-", "-", 2)
        tab1.put(les0)
        with self.assertRaises(ValueError):
            tab1.put(les0)

    def test_get(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.get(ter0), les0)

    def test_get(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        self.assertEqual(tab1.get(les0), None)

    def test_busy(self):
        tab1 = Timetable1()
        les0 = Lesson(tab1, Term(9, 35, Day.TUE), "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.busy(les0.term), True)

    def test_busy(self):
        tab1 = Timetable1()
        les0 = Lesson(tab1, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tab1.busy(les0.term), False)

    def test_can_be_transferred(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.can_be_transferred_to(ter1, True), True)

    def test_can_be_transferred(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.can_be_transferred_to(ter1, True), False)

    def test_can_be_transferred(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.can_be_transferred_to(ter1, False), True)

    def test_can_be_transferred(self):
        tab1 = Timetable1()
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tab1, ter0, "-", "-", 2)
        tab1.put(les0)
        self.assertEqual(tab1.can_be_transferred_to(ter1, False), False)

    def test_parase(self):
        tab1 = Timetable1()
        strl = "d- d+ t- t+"
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(tab1.parse(strl), actl)

    def test_parase_err(self):
        tab1 = Timetable1()
        strl = "d- d+ t- t+ yoooo"
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        with self.assertRaises(ValueError):
            tab1.parse(strl)

    def test_peform(self):
        tab1 = Timetable1()
        tt1 = Timetable1()
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tt1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tab1.put(les1)
        tt1.put(les1)
        tt1.perform(actl)
        self.assertEqual(tt1.lesson, tab1.lesson)


if __name__ == '__main__':
    unittest.main()