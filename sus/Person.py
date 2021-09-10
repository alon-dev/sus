class Person:
    
    def __init__(self, id, name):
        if self.validId(id):
            self.id=id
        else:
            raise ValueError("ID NEEDS TO BE 8 DIGITS")
        self.name = name
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setId(self, id):
        if self.validId(id):
            self.id = id
        else:
            raise ValueError("ID NEEDS TO BE 8 DIGITS")
    
    def setName(self, name):
        self.name = name

    @staticmethod  
    def validId(id):
        return len(id) == 8
    
    """amogus"""