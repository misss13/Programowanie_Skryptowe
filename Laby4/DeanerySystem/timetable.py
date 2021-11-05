from typing import List
from .lessonv3 import Lesson
from .termv3 import Term
from .day import Day
from .action import Action

class t_tablele1(object):
    """ Class containing a set of operations to manage the t_tablele """
    def __init__(self):
        self.lesson_list = []

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
        for i in self.lesson_list:
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

    def put(self, lesson: Lesson) -> bool:
        """
        Add the given lesson to the t_tablele.
        Parameters
        ----------
        lesson : Lesson
            The added  lesson
        Returns
        -------
        bool
        **True**  if the lesson was added.  The lesson cannot be placed if the t_tablele slot is already occupied.
        """
        if type(lesson) is not Lesson:
            raise TypeError("To nie jest lekcja")
            return False
        else:
            for i in self.lesson_list:
                if i.term == lesson.term:
                    return False
            self.lesson_list.append(lesson)
            return True
        return False

    def parse(self, actions: List[str]) -> List[Action]:
        """
        Converts an array of strings to an array of 'Action' objects.
        Parameters
        ----------
        actions:  List[str]
            A list containing the strings: "d-", "d+", "t-" or "t+"
        Returns
        -------
            List[Action]
                A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """
        actions = actions.split()
        ac_list = []
        for action in actions:
            if action == "d-":
                ac_list.append(Action.DAY_EARLIER)
            elif action == "d+":
                ac_list.append(Action.DAY_LATER)
            elif action == "t-":
                ac_list.append(Action.TIME_EARLIER)
            elif action == "t+":
                ac_list.append(Action.TIME_LATER)
        return ac_list

    def perform(self, actions: List[Action]):
        """
        Transfer the lessons included in the t_tablele as described in the list of actions. N-th action should be sent the n-th lesson in the t_tablele.
        Parameters
        ----------
        actions : List[Action]
            Actions to be performed
        """
        pom = 0
        for i in actions:
            if   i == Action.DAY_EARLIER:
                self.lesson_list[pom].earlierDay()
            elif i == Action.DAY_LATER:
                self.lesson_list[pom].laterDay()
            elif i == Action.TIME_EARLIER:
                self.lesson_list[pom].earlierTime()
            elif i == Action.TIME_LATER:
                self.lesson_list[pom].laterTime()
            pom = (pom + 1)%len(self.lesson_list)

    def get(self, term: Term) -> Lesson:
        """
        Get object (lesson) indicated by the given term.
        Parameters
        ----------
        term: Term
            Lesson date
        Returns
        -------
        lesson: Lesson
            The lesson object or None if the term is free
            """
        for i in self.lesson_list:
            if i.term == term:
                return i
        return None

    def __str__(self):
        #czasy
        t_table = []
        for i in self.lesson_list:
            t_table.append(i.term)
        #print(t_table)
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
            table_final[0][c + 1] = f'{t.start_print()}-{t.koniec_print()}' #"%s-%s" %(t.start_print(), t.koniec_print())
        for i in self.lesson_list:
            table_final[i.term.day.value][t_table.index(i.term) + 1] = i.name
        nic = " "
        pad = "\n%s%s\n" %(nic*12, "*"*92)
        e = "%s" %(nic*12)
        fin = ""
        for i in range(len(t_table) + 1):
            for j in range(8):
                fin += f'{table_final[j][i]: ^12}*'
            fin += pad
        return fin

#print(t_tablele1().parse("d+ d- t+ t- d+ Kot"))
#l=t_tablele1()
#l.put(Lesson(Term(18, 0, Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2))
#print(l)