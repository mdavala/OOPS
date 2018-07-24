class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    
    def describe(self):
        #print (self.name)
        return "the dog says woof"

class LapDog(Dog):
    def describe(self):
        #print (self.name)
        return "The lapdog says yip"

jimmy = Dog("Jimmy")
print(jimmy.name)
jimmy.describe()

tommy = LapDog("tommy")
print (tommy.name)
tommy.describe()