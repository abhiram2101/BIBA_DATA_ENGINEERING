"""
class Dog():
    def __init__(self,name):
        self.name = name
    def dog_details(self) :
        print("dog name is :",self.name)
dog1 = Dog("rapy")
dog1.dog_details()



class Dog:
# class attribute
    attr1 = "mammal"
    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

"""

class Dog2():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("my name is :",self.name)
cherry = Dog2("Cherry")
rapo = Dog2("Rapo")

cherry.speak()
rapo.speak()
