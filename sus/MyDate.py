import datetime
import random
class MyDate():

    def __init__(self, year, month, day):
        self.hashRnd = random.randint(1, 1000000000)
        self.year = year
        self.month = month
        self.day = day
        if(not self.validDate(self)):
            raise ValueError("INVALID DATE")
    
    @staticmethod
    def validDate(date):
        try:
            datetime.date(date.year, date.month, date.day)
        except ValueError:
            return False
        return True
    @property
    def day(self):
        return self.__day
    @property
    def month(self):
        return self.__month
    @property
    def year(self):
        return self.__year
    
    @day.setter
    def day(self, day):
        self.__day = day
    @month.setter
    def month(self, month):
        self.__month = month
    @year.setter
    def year(self, year):
        self.__year = year
    
    def am_i_earlier(self, date):
        if (self < date):
            return True
        else:
            return False
    def __repr__(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    def __lt__(self, other):
        if(self.year != other.year):
            return self.year < other.year
        elif(self.month != other.month):
            return self.month < other.month
        elif(self.day != other.day):
            return self.day < other.day
        return False
    
    def __eq__(self, other):
        if(self.year != other.year):
            return False
        elif(self.month != other.month):
            return False
        elif(self.day != other.day):
            return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    def __gt__(self, other):
        return not self.__le__(other)
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
    def __hash__(self):
        return hash(self.hashRnd)
    
    
    
    
    
