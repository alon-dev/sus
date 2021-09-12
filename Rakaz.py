from Teacher import Teacher

class Rakaz(Teacher):
    def __init__(self, id: int = None, name: str = None, week_hours_of_work: int = None, teacher: Teacher = None, reward: int = None, rakaz = None):
        """Initiates a new Rakaz object

        Args:
            id (int, optional): The id of the Rakaz. Defaults to None.
            name (str, optional): The name of the Rakaz. Defaults to None.
            week_hours_of_work (int, optional): The weekly hours of work of the Rakaz. Defaults to None.
            teacher (Teacher, optional): A Teacher to copy from. Defaults to None.
            reward (int, optional): The Teacher's reward. Defaults to None.
            rakaz (Rakaz, optional): A Rakaz to copy from. Defaults to None.

        Raises:
            ValueError: When params are incorrect
        """
        if id is not None and name is not None and week_hours_of_work is not None and teacher is None and reward is None and rakaz is None:
            super().__init__(id, name, week_hours_of_work)
        elif id is None and name is None and week_hours_of_work is None and teacher is not None and reward is not None and rakaz is None:
            super().__init__(copy = teacher)
            self.__reward = reward
        elif id is None and name is None and week_hours_of_work is None and teacher is None and reward is None and rakaz is not None:
            super().__init__(rakaz.id, rakaz.name, rakaz.week_hours_of_work)
            self.__reward = rakaz.reward
        else:
            raise ValueError("No")
    
    @property
    def reward(self):
        return self.__reward
    @reward.setter
    def reward(self, reward):
        self.__reward = reward
    
    def __repr__(self):
        return f'{super().__repr__()}, Reward: {self.__reward}' 


