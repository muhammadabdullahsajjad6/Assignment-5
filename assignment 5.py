#Q1: Logging Metaclass
class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        print(f"Class {name} created")
        return new_class

    def __init__(cls, name, bases, dct):
        print(f"Initializing class: {name}")
        super().__init__(name, bases, dct)

# Example usage:
class MyClass(metaclass=LoggingMeta):
    def __init__(self):
        print("Instance of MyClass created")

# Output:
# Class MyClass created
# Initializing class: MyClass

