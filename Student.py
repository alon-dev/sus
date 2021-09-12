
from Person import Person

class Student(Person):
    def __init__(self, id: int = None, name: str = None, student = None):
        self.__grades = ()
        if student == None and id is not None and name is not None:
            super().__init__(id, name)
        elif student is not None:
            super().__init__(student.id, student.name)
            self.__grades = student.grades
        else:
            raise ValueError("No Arguments Passed")
    @property
    def grades(self):
        return self.__grades
    @grades.setter
    def grades(self, grades):
        self.__grades = grades
    
    def add_grade(self, grade: int):
        """Adds a grade to the student's grade list

        Args:
            grade (int): the grade to add
        """
        self.__grades.append(grade)
    def average(self):
        """returns the student's grades' average

        Returns:
            int: the average of the student's grades
        """
        if len(self.__grades) > 0:
            sum = 0
            for grade in self.__grades:
                sum += grade
            return sum/len(self.__grades)
        else:
            return "No Grades."
    
    def __repr__(self):
        return f'{super().__repr__()}, Grade Average: {self.average()}'