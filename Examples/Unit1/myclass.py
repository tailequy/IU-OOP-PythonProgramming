class MyClass: # Normal method
    def instance_method(self):
        print("This is an instance method.")
    # Static method
    @staticmethod
    def static_method():
        print("This is a static method.")
    # Class method
    @classmethod
    def class_method(cls):
        print("This is a class method. The class name is", cls.__name__)
# Create an object of MyClass
obj = MyClass()
# Call the instance method on the object
obj.instance_method() # This is an instance method.
# Call the static method on the class
MyClass.static_method() # This is a static method.
# Call the class method on the class
MyClass.class_method() # This is a class method. The class name is MyClass
