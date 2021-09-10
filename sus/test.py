
from MyPerson import MyPerson
a = MyPerson(10000000, "Alon", 2021, 3, 10)
b = MyPerson(20000000, "Omer", 1998, 1, 21)
list1 = []
list1.append(a)
list1.append(b)
print("start")
MyPerson.sort_by_birth_date(list1)
