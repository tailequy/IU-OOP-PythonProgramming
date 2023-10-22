class Animal:
    def __init__ (self, name):
        self.name = name
    def speak2(self):
        print( "This animal speaks." )
class Dog(Animal):
    def __init__ (self, name):
        super().__init__(name)
    def speak(self):
        print("Woof!")
dog = Dog("Pelle")
animal = Animal( "Generic" )
dog.speak2()
animal.speak2()