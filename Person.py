class Person:
    def __init__(self, id, name):
        """Initializes a new Student object

        Args:
            id (int): student's id number
            name (str): student's name

        Raises:
            ValueError: if id number is longer than 8 characters
        """
        if self.validId(id):
            self.__id=id
        else:
            raise ValueError("ID NEEDS TO BE 8 DIGITS")
        self.__name = name
        
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

    @staticmethod  
    def validId(id):
        return len(str(id)) == 8