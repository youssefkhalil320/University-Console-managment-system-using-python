class Student:
    def __init__(self, name = "Human", sid = 0000, dbirth = "20-12-2000", nat = "EG", gender = "M"):
        self.name = name
        self.id = sid 
        self.dbirth = dbirth
        self.nat = nat
        self.gender = gender 

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getDbirth(self):
        return self.dbirth

    def getNat(self):
        return self.nat

    def getGender(self):
        return self.gender 

    def setName(self,name):
        self.name = name

    def setId(self,sid):
        self.id = sid 

    def selfDbirth(self,dbirth):
        self.dbirth = dbirth

    def setNat(self,nat):
        self.nat = nat

    def setGender(self,gender):
        self.gender = gender      

    def description(self):
        return f"Student Name is: {sel.name} id: {self.id} Gender is {self.gender}"                                  
