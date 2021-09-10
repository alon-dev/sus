from Person import Person
from MyDate import MyDate



class MyPerson(Person):
    
    def __init__(self, id, name, year, month, day):
        super().__init__(id, name)
        birthdate = MyDate(year,month,day)
        self.__birthdate = birthdate
    
    def __repr__(self):
        return super().__repr__() + f", Birthdate: {self.birtdate}"
    
    @property
    def birthdate(self):
        return self.__birthdate
    
    @birthdate.setter
    def birtdate(self, birthdate):
        self.__birthdate = birthdate
    
    
    
    """
    assumption: There are no reoccuring dates
    """  
    @staticmethod
    def sort_by_birth_date(MyPersonList):
        dict = {}
        for i in MyPersonList:
            dict[i.birthdate] = i
        for j in sorted(dict):
            print(dict[j])
            
    
    