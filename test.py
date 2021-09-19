from Person import Person
from Student import Student
from Teacher import Teacher
from Rakaz import Rakaz
from Megama import Megama


def test():
    sage = Person(1111, "sage")
    limor = Student(123, "limor")
    limor.add_grade(79)
    limor.add_grade(70)
    limor.add_grade(45)
    limor.add_grade(91)
    limor.add_grade(87)
    limor.add_grade(100)
    eli = Student(456,"eli")
    eli.add_grade(76)
    eli.add_grade(94)
    eli.add_grade(60)
    yael = Student(789, "yael")
    Michael = Teacher(111, "Michael", 30)
    Maria = Teacher(222,"Maria",25)
    Micha = Teacher(333,"Micha",24)
    Steve = Rakaz(888,"Steve",32)
    Steve.reward = 7
    person_list = [sage, limor, eli, yael, Michael, Maria, Micha, Steve]
    BINA = Megama("BINA", person_list)
    print(BINA)
    person_list = [Micha, Steve]
    CS = Megama("CS", person_list)
    print(CS)

test()