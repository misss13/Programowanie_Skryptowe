from typing import List
from .lessonv3 import Lesson
from .basicterm import Term
from .day import Day
from .action import Action

class BasicTimetable:
    def __init__(self):
        self.lesson = {}
    
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
        for i in list(self.lesson.values()):
            if i.term == term:
                return i
        return None
    
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
            for i in list(self.lesson.values()):
                if i.term == lesson.term:
                    raise ValueError("Podany termin jest zajęty przez inną lekcję")
                    return False
            self.lesson[f'{lesson.term.start_print()}-{lesson.term.koniec_print()}-{lesson.term.day}'] = lesson
            return True
        raise ValueError("Dany termin zajęty")
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
            else:
                raise ValueError("Niepoprawna akcja")
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
                list(self.lesson.values())[pom].earlierDay()
            elif i == Action.DAY_LATER:
                list(self.lesson.values())[pom].laterDay()
            elif i == Action.TIME_EARLIER:
                list(self.lesson.values())[pom].earlierTime()
            elif i == Action.TIME_LATER:
                list(self.lesson.values())[pom].laterTime()
            pom = (pom + 1)%len(list(self.lesson.values()))