# What is a Class Variable? (English)

# A class variable is a variable that belongs to the class itself, not to any specific object.

# 👉 It is shared among all objects of the class.
# 👉 It is defined outside the constructor (__init__) but inside the class.

# Example
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Arshad")
s2 = Student("Ali")

print(s1.school)
print(s2.school)

# Output:

# ABC School
# ABC School