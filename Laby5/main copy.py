from DeanerySystem import Day, Term, Lesson, Action, Timetable1, BasicTerm, Break, BasicTimetable, Timetable2

bl = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
tt0 = Timetable2(bl)
les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
print(tt0.busy(les0.term))