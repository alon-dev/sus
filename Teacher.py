from Person import Person

class Teacher(Person):

    def __init__(self, id = None, name = None, week_hours_of_work = None, copy = None):
        """Builds a new Teacher object

        Args:
            id (int, optional): The teacher's id. Defaults to None.
            name (str, optional): The teacher's name. Defaults to None.
            week_hours_of_work (int, optional): The teacher's hours of work in a week. Defaults to None.
            copy (Teacher, optional): A teacher object to copy from. Defaults to None.

        Raises:
            ValueError: When arguments are used incorrectly
        """
        self.MAX_HOURS_OF_WORK = 24
        if(copy is not None):
            super().__init__(copy.id, copy.name)
            self.__week_hours_of_work = copy.week_hours_of_work
        elif((id is not None) and (name is not None) and (week_hours_of_work is not None)):
            super().__init__(id, name)
            self.MAX_HOURS_OF_WORK = 24
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
        return super().__repr__()  + f"Max hours of work in a week: {self.MAX_HOURS_OF_WORK}, Hours of work i a week: {self.__week_hours_of_work}"

        