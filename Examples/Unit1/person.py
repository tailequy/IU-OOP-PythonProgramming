class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print(f"Hi, my name is {self.name} and Is {self.age} years old.")

person1 = Person("Alice", 25)
person2 = Person("Bob", 35)
person1.say_hi()
person2.say_hi()

person3 = Person(name="Charlie", age=person1.age)
person3.say_hi()