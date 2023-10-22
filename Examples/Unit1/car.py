# Define a class called Car
class Car:
    # Class attribute
    wheels = 4
    # Constructor method
    def __init__(self, make, model, year=None):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
    # Instance method
    def get_make_model(self):
        return "{} {}".format(self.make, self.model)
# Create two Car objects
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Honda", "Civic", 2022)
# Access the class attribute through the class
print("Number of wheels (class attribute):", Car.wheels)
# Access the instance attribute through the object
print("Make of car 1 (instance attribute):", car1.make)
# Change the instance attribute through the object
car1.make = "Nissan"
print("Make of car 1 after change:", car1.make)
# Access the instance method through the object
print("Make and model of car 2 (instance method):", car2.get_make_model())
print(car1.wheels)
car1.wheels = 3
print(car1.wheels)

print(Car.wheels)

Car.wheels = 5

print("Class attribute:", Car.wheels)

print("Car1:",car1.wheels)