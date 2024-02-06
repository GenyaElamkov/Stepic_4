class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname
    
    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
