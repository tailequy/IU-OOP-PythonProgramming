from abc import ABC, abstractmethod
class Shape(ABC):
    '''
    An @ symbol at the beginning of a line is used for class and function decorators.
    A function returning another function, usually applied as a function transformation using the @wrapper syntax
    The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:
    def f(arg):
        ...
    f = staticmethod(f)

    @staticmethod
    def f(arg):
        ...
    '''
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def area(self):
        return self._length * self._width
    def perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self,radius):
        self.__radius =  radius
    def area(self):
        return 3.14 * self.__radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.__radius

#Creating objects of different shapes
rectangle = Rectangle(5,3)
circle = Circle(4)

#Caling the abtract methods on the objects
print(rectangle.area())
print(rectangle.perimeter())
print(circle.area())
print(circle.perimeter())