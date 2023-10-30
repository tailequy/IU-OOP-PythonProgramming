from abc import ABC, abstractmethod
class People(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Customer(People):
    def __init__(self, name, product):
        self._name = name
        self._product = product
    def show_info(self):
        return f"The customer {self._name} buys {self._product}."

class Student(People):
    def __init__(self,name, university, country):
        self._name = name
        self._university = university
        self._country = country
    def show_info(self):
        return f"The student {self._name} is studying at {self._university} in {self._country}."

#Creating objects
customer = Customer("Alice","iPhone")
student = Student("Bob","IU","Germany")

#Caling the abtract methods on the objects
print(customer.show_info())
print(student.show_info())