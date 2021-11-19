from DeanerySystem import Day, Term, Lesson, Action, Timetable1, BasicTerm, Break, BasicTimetable, Timetable2

term1 = Term(8, 0, Day.WED)
term2 = Term(9, 30, Day.WED)
term3 = Term(9, 35, Day.THU)
tab2 = Timetable2([Break(Term(9, 30, Day.MON, 5))])
les1 = Lesson(tab2, term1, 'operacyjne', 'matematyka', 2)
les2 = Lesson(tab2, term3, 'śledcza', 'polski', 2)
les3 = Lesson(tab2, term2, 'skryptowe', 'przyroda', 2)

print(tab2)
try:
    tab2.put(les1)
except Exception as err:
    print(err)
    quit()

print()
print(tab2)

try:
    tab2.put(les2)
except Exception as err:
    print(err)
    quit()    

print()
print(tab2)
try:
    tab2.put(les3)
except Exception as err:
    print(err)
    quit()
    
print(tab2)
