class Person:
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
    
    def fullname(self):
        return self.first + " "+self.middle+" "+self.last
    
    def formalname(self, title):
        return title+self.fullname()

person = Person("Aaron", "dexter","Maxwell")
print(person.formalname("Dr."))
