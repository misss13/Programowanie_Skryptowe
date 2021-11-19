from DeanerySystem import Day, Action, Term, Lesson, t_tablele1
import unittest

class Test_Time_Table(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(t_tablele1().parse("d+"), [Action.DAY_LATER])
        self.assertEqual(t_tablele1().parse("ala ma kota"), [])
        self.assertEqual(t_tablele1().parse("d+ t-"), [Action.DAY_LATER, Action.TIME_EARLIER])
        self.assertEqual(t_tablele1().parse("t+ alama kota d+"), [Action.TIME_LATER ,Action.DAY_LATER])
        self.assertEqual(t_tablele1().parse("t- d- t+ d-"), [Action.TIME_EARLIER, Action.DAY_EARLIER, Action.TIME_LATER, Action.DAY_EARLIER])

    def test_peform(self):
        t0 = t_tablele1()
        t1 = t_tablele1()
        l1 = Lesson(t1, Term(8, 0, Day.WED), 'less1', 'less1', 1)
        act = [ Action.DAY_LATER, Action.DAY_EARLIER, Action.TIME_EARLIER, Action.TIME_LATER]
        t0.put(l1)
        t1.put(l1)
        t1.perform(act)
        self.assertEqual(t1.lesson_list, t0.lesson_list)

    def test_str(self):
        t0 = t_tablele1()
        t1 = t_tablele1()
        l1 = Lesson(t1, Term(8, 0, Day.WED), 'less1', 'less1', 1)
        l0 = Lesson(t1, Term(9, 30, Day.WED), 'less1', 'less1', 1)
        t0.put(l0)
        t1.put(l1)
        act = [ Action.TIME_LATER]
        t1.perform(act)
        self.assertEqual(t1.__str__(), t0.__str__())

    def test_busy_false(self):
        t = t_tablele1()
        l = Lesson(t, Term(15, 35, Day.TUE), "less1", "less1", 2)
        self.assertEqual(t.busy(l.term), False)  

    def test_can_be_transferred_to_true(self):
        t0 = t_tablele1()
        ter0 = Term(8, 0, Day.TUE)
        ter1 = Term(9, 30, Day.TUE)
        les0 = Lesson(t0, ter0, "less1", "less1", 2)
        t0.put(les0)
        self.assertEqual(t0.can_be_transferred_to(ter1, True), True)

    def test_can_be_transferred_to_false(self):
        t0 = t_tablele1()
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(t0, ter0, "less1", "less1", 2)
        t0.put(les0)
        self.assertEqual(t0.can_be_transferred_to(ter1, True), False)  

    def test_can_be_transferred_to_after(self):
        t0 = t_tablele1()
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(20, 00, Day.SAT)
        les0 = Lesson(t0, ter0, "less1", "less1", 2)
        t0.put(les0)
        self.assertEqual(t0.can_be_transferred_to(ter1, False), False)
    
    def test_get(self):
        t0 = t_tablele1()
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(t0, ter0, "less1", "less1", 2)
        t0.put(les0)
        self.assertEqual(t0.get(ter0), les0)
    
    def test_put_true(self):
        t0 = t_tablele1()
        l0 = Lesson(t0, Term(9, 35, Day.TUE), "less1", "less1", 2)
        self.assertEqual(t0.put(l0), True)
    

if __name__ == "__main__":
    unittest.main()