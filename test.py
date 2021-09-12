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
    