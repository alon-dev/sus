from Student import Student
from Teacher import Teacher
from Rakaz import Rakaz

class Megama:
    def __init__(self, mname: str = None, people: list = None):
        """Initiates a new Megama object

        Args:
            mname (str, optional): The Megama's name. Defaults to None.
            people (list, optional): The list of people in the Megama. Defaults to None.

        Raises:
            ValueError: Raises when paramaters are incorrect
        """
        self.__mn = None
        self.__rakaz = None
        self.__teacher_list = ()
        self.__student_list = ()
        if mname is not None and people is None:
            self.__mn = mname
        elif mname is None and people is not None:
            for person in people:
                if type(person) == Rakaz:
                    self.__rakaz = person
                elif type(person) == Teacher:
                    self.__teacher_list.append(person)
                elif type(person) == Student:
                    self.__student_list.append(person)
        else:
            raise ValueError("No Job")
    def add_person(self, person):
        """Adds a new person to the Megama

        Args:
            person (Rakaz, Teacher, or Student): The person to add

        Raises:
            ValueError: When person has an invalid type
        """
        job = type(person)
        if job == Rakaz:
            self.__rakaz = person
        if job == Teacher:
            self.__teacher_list.append(person)
        if job == Student:
            self.__student_list
        else:
            raise ValueError("No Job")
    
    @property
    def mn(self):
        return self.__mn
    @property
    def rakaz(self):
        return self.__rakaz
    @property
    def teacher_list(self):
        return self.__teacher_list
    @property
    def student_list(self):
        return self.__student_list
    
    @mn.setter
    def mn(self, mn):
        self.__mn = mn
    @rakaz.setter
    def rakaz(self, rakaz):
        self.__rakaz = rakaz
    @teacher_list.setter
    def teacher_list(self, teacher_list):
        self.__teacher_list = teacher_list
    @student_list.setter
    def student_list(self, student_list):
        self.__student_list = student_list
    
    def __repr__(self):
        ret = f"nm: {self.__nm}, rakaz: {self.__rakaz.__repr__()}\n"
        ret += "teacher list:\n"
        for i in self.__teacher_list:
            ret += i.__repr__() + "\n"
        ret += "student list:\n"
        for i in self.___student_list:
            ret += i.__repr__() + "\n"
        return ret
