# constructor

# A constructor is a special method in a class that is automatically called when an object is created.

# In Python, the constructor method is:

# __init__()

# It is used to initialize object data (attributes).


# types

# 1 parameterized constructor
# A constructor that takes parameters to initialize object data.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Arshad", 22)
print(s1.name)

# 2 non parameterized constructor
# A constructor that  not takes parameters to initialize object data.

class Student:
    def __init__(self):
        self.name = "arshad"
        self.age = 22

s1 = Student()
print(s1.name)

# 3 default constructor

# A constructor that does not take any parameters


# A constructor that does not take any parameters





# What is self? 

# self refers to the current object of the class.
# self current object ko refer karta hai.

# 👉 Jab hum object banate hain, to self us object ko point karta hai.
# 👉 Iske through hum object ki properties ko access karte hain.



# What is isinstance()? (English)

# isinstance() is a built-in function in Python used to check whether an object belongs to a specific class (or data type).

# 👉 It returns True or False.

# 🔹 Syntax
# isinstance(object, class)
# Example 1 (Basic)
x = 10

print(isinstance(x, int))     # True
print(isinstance(x, str))     # False