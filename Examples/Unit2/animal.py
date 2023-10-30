class Animal:
    def __init__ (self, name):
        self.name = name
    def speak(self):
        print( "This animal speaks." )
class Dog(Animal):
    def __init__ (self, name):
        super().__init__(name)
    def speak(self):
        print("Woof!")
dog = Dog("Pelle")
animal = Animal("Generic" )
dog.speak()
animal.speak()