import unittest
from DeanerySystem import Day, Term, Lesson, Action, Timetable1, BasicTerm, Break, BasicTimetable, Timetable2 

class Test_Timetable2(unittest.TestCase):
    def test_put(self):
        tab0 = Timetable2([Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))])
        les0 = Lesson(tab0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tab0.put(les0), True)

    def test_put_err(self):
            br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
            tab0 = Timetable2(br1)
            les0 = Lesson(tab0, Term(9, 30, Day.TUE), "-", "-", 2)
            with self.assertRaises(ValueError):
                tab0.put(les0)
    
    def test_get(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 35, Day.TUE)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.get(ter0), les0)
    
    def test_get_none(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        self.assertEqual(tab0.get(les0), None)
    
    def test_busy(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        les0 = Lesson(tab0, Term(9, 35, Day.TUE), "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.busy(les0.term), True)
    
    def test_busy(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        les0 = Lesson(tab0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertFalse(tab0.busy(les0.term))
    
    def test_can_be_transferred(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 35, Day.TUE)
        ter1 = Term(11, 15, Day.TUE)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.can_be_transferred_to(ter1, True), True)

    def test_can_be_transferred(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 35, Day.TUE)
        ter1 = Term(11, 15, Day.SAT)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.can_be_transferred_to(ter1, True), False)

    def test_can_be_transferred(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 35, Day.SAT)
        ter1 = Term(11, 15, Day.SAT)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.can_be_transferred_to(ter1, False), True)
    
    def test_can_be_transferred(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        ter0 = Term(9, 35, Day.SAT)
        ter1 = Term(11, 15, Day.TUE)
        les0 = Lesson(tab0, ter0, "-", "-", 2)
        tab0.put(les0)
        self.assertEqual(tab0.can_be_transferred_to(ter1, False), False)

    def test_parase(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        strl = "d- d+ t- t+"
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(tab0.parse(strl), actl)

    def test_parase_err(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        strl = "d- d+ t- t+ yoooo"
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        with self.assertRaises(ValueError):
            tab0.parse(strl)

    def test_skipBreak(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        tab1 = Timetable2(br1)
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tab1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tab0.put(les1)
        tab1.skipBreaks = False
        tab1.put(les1)
        tab1.perform(actl)
        self.assertEqual(tab1.lesson, tab0.lesson)

    def test_skipBreak(self):
        br1= [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tab0 = Timetable2(br1)
        tab1 = Timetable2(br1)
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tab1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tab0.put(les1)
        tab1.skipBreaks = True
        tab1.put(les1)
        tab1.perform(actl)
        self.assertEqual(tab1.lesson, tab0.lesson)


if __name__ == '__main__':
    unittest.main()