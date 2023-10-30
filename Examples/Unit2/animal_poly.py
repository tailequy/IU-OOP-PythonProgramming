class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("This animal speaks.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Meow!")

dog = Dog("Fido")
animal = Animal("Animal")

dog.speak() #Woof!
animal.speak() #This animal speaks.

def make_animal_speak(animal):
    animal.speak()
#Create instances of different animals
dog = Dog("Fido")
cat = Cat("Wishers")
#Call the make_animal_speack function
make_animal_speak(dog)
make_animal_speak(cat)