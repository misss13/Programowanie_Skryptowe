from DeanerySystem import Day, Term, Lesson, Action, t_tablele1

tt1 = t_tablele1()
less1 = Lesson(tt1, Term(8, 0, Day.WED), 'less1', 'less1', 2)
less2 = Lesson(tt1, Term(12, 0, Day.FRI), 'less2', 'less2', 2)
less3 = Lesson(tt1, Term(16, 30, Day.SAT), 'less3', 'less3', 2)
print(tt1)
tt1.put(less1)
tt1.put(less2)
tt1.put(less3)
print(tt1)
tt1.perform(tt1.parse("t- d- t+ d-"))
print(tt1)