from typing import List
from .lessonv3 import Lesson
from .basicterm import Term
from .day import Day
from .action import Action
from .basictimetable import BasicTimetable
from .breakT import Break

class Timetable2(BasicTimetable):
    skipBreaks = False
    """ Class containing a set of operations to manage the t_tablele """
    def __init__(self, breaks: List[Break]):
        self.breaks = breaks
        super().__init__()

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        """
        Informs whether a lesson can be transferred to the given term
        Parameters
        ----------
        term : Term
            The term checked for the transferability
        full_time : bool
            Full-time or part-time studies
        Returns
        -------
        bool
            **True** if the lesson can be transferred to this term
        """
        if term.hour < 8:
            return False
        t = term.koniec_h_m()
        if t.hour > 20:
            return False
        if t.hour == 20 and t.minute > 0:
            return False
        #odrzuciliśmy przedziały 20-8
        if not self.busy(term):
            if term.day.value < 4:
                is_ft = True
            elif term.day.value > 4:
                is_ft = False
            else:
                if term.hour < 17:
                    is_ft = True
                else:
                    is_ft = False
            if is_ft == full_time:
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
        if type(lesson) is not Lesson:
            raise TypeError("To nie jest lekcja")
            return False
        else:
            for i in list(self.lesson.values()):
                if i.term == lesson.term:
                    raise ValueError("Podany termin jest zajęty przez inną lekcję")
                    return False

            if self.onbreaks(lesson.term):
                raise ValueError("Podany termin jest zajęty przez przerwę")
                return False

            self.lesson[f'{lesson.term.start_print()}-{lesson.term.koniec_print()}-{lesson.term.day}'] = lesson
            return True
        return False

    def busy(self, term: Term) -> bool:
        """
        Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
        since there might be free term where the lesson cannot be transferred.
        Parameters
        ----------
        term : Term
            Checked term
        Returns
        -------
        bool
            **True** if the term is busy
        """        
        for i in list(self.lesson.values()):
            if i.term == term:
                return True
            #moze nie działać term
            l_start = Term(i.term.hour, i.term.minute, i.term.day, i.term.duration)
            l_end = i.term.koniec_h_m()
            t_start = Term(term.hour, term.minute, term.day, term.duration)
            t_end = term.koniec_h_m()
            if l_end > t_start and l_end < t_end: 
                return True
            if t_end > l_start and t_end < l_end:
                return True
            if l_start > t_start and l_start < t_end:
                return True
            if t_start > l_start and t_start < l_end: 
                return True
        return False

    def onbreaks(self, term: Term) -> bool:
            t_start = term.getStartTime()
            t_end = term.getEndTime()
            for i in self.breaks:
                b_start = i.term.getStartTime()
                b_end = i.term.getEndTime()
                if t_start > b_start and t_start < b_end:
                    return (True, i.term.duration)
                if t_end > b_start and t_end < b_end:
                    return (True, i.term.duration)
                if t_start == b_start and t_end > b_end:
                    return (True, i.term.duration)
                if t_start < b_start and t_end == b_end:
                    return (True, i.term.duration)
            return False


    def __str__(self):
        #lekcje
        t_table = []
        for i in list(self.lesson.values()):
            h_for = f'{i.term.start_print()}-{i.term.koniec_print()}'
            if not h_for in t_table:
                t_table.append(h_for)
        #przerwy
        for i in self.breaks:
            h_for = f'{i.term.start_print()}-{i.term.koniec_print()}'
            if not h_for in t_table:
                t_table.append(h_for)

        t_table = sorted(t_table)
        #z wartosciami
        table_final = []
        for i in range(8):
            table_final.append([])
            for j in range(len(t_table) + 1):
                table_final[i].append("")
        #dni tygodnia
        for i in Day:
            table_final[i.value+1][0] = str(i)
        for c, t in enumerate(t_table):
            table_final[0][c + 1] = f'{t}' #"%s-%s" %(t)
        #lekcje do tabelki
        for i in list(self.lesson.values()):
            h_for = f'{i.term.start_print()}-{i.term.koniec_print()}'
            table_final[i.term.day.value][t_table.index(h_for) + 1] = i.name
        for bre in self.breaks:
            h_for = f'{bre.term.start_print()}-{bre.term.koniec_print()}'
            for i in range(1, 8):
                table_final[i][t_table.index(h_for) + 1] = f'xxxxx'
        nic = " "
        pad = "\n%s%s\n" %(nic*12, "*"*92)
        e = "%s" %(nic*12)
        fin = ""
        for i in range(len(t_table) + 1):
            for j in range(8):
                fin += f'{table_final[j][i]: ^12}*'
            fin += pad
        return fin