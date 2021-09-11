import Person

class Student(Person.Person):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.__grades = []

    @classmethod
    def copy(cls, student):
        """builds a new student object using another student object

        Args:
            student (Student): the student object to copy

        Returns:
            Student: a new student object
        """
        a = cls(student.id, student.name)
        for grade in student.grades:
            a.add_grade(grade)
        return a
    
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