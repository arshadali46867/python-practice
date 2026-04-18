# Object-Oriented Programming (OOP) is a programming paradigm(kisi kaam ko karne ka tarika ya sochne ka pattern.) that is based on objects and classes.

# In OOP:

# A class is a blueprint or template used to create objects..

# An object is an instance of a class.

# It helps organize code using real-world concepts.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

s1 = Student("Arshad", 22)
s1.greet()



# constructor

# A constructor is a special method in a class that is automatically called when an object is created.

# In Python, the constructor method is:

# __init__()

# It is used to initialize object data (attributes).