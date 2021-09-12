from Person import Person

class Teacher(Person):

    def __init__(self, id = None, name = None, week_hours_of_work = None, copy = None):
        self.MAXHOUROFWORK = 24
        if(copy is not None):
            super().__init__(copy.id, copy.name)
            self.__week_hours_of_work = copy.week_hours_of_work
        elif((id is not None) and (name is not None) and (week_hours_of_work is not None)):
            super().__init__(id, name)
            self.MAXHOUROFWORK = 24
            self.__week_hours_of_work = week_hours_of_work
        else:
            raise ValueError("No Arguments Passed")

    @property
    def week_hours_of_work(self):
        return self.__week_hours_of_work
    
    @week_hours_of_work.setter
    def week_hours_of_work(self, week_hours_of_work):
        self.__week_hours_of_work = week_hours_of_work

    def __repr__(self):
        return super().__repr__()  + f"Max hours of work in a week: {self.MAXHOUROFWORK}, Hours of work i a week: {self.__week_hours_of_work}"

        