
from MyPerson import MyPerson
a = MyPerson(10000000, "Alon", 2021, 3, 10)
b = MyPerson(20000000, "Omer", 1998, 1, 21)
c = MyPerson(30000000, "Bar Kokhva", 1997, 1, 21)
d = MyPerson(40000000, "Daniel", 1999, 2, 11)
e = MyPerson(50000000, "Adolf", 1939, 9, 1)
f = MyPerson(60000000, "Joseph", 1990, 2, 28)
g = MyPerson(70000000, "Moris", 2004, 7, 15)
h = MyPerson(80000000, "Bob", 2003, 12, 21)
i = MyPerson(90000000, "Yasuo", 1997, 1, 24)
j = MyPerson(51000000, "Scott", 1998, 1, 22)
list1 = []
list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)
list1.append(e)
list1.append(f)
list1.append(g)
list1.append(h)
list1.append(i)
list1.append(j)

print("start")
MyPerson.sort_by_birth_date(list1)
