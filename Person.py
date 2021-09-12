class Person:
    def __init__(self, id, name):
        self.__id = id
        self.__id = id
        """Initializes a new Student object

        Args:
            id (int): student's id number
            name (str): student's name
        """
    def __repr__(self):
        return f"Name: {self.name}, Id: {self.id}"
    
    @property    
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    
    @id.setter
    def id(self, id):
        if self.validId(id):
            self.__id = id
        else:
            raise ValueError("ID NEEDS TO BE 8 DIGITS")
        
    @name.setter
    def name(self, name):
        self.__name = name