# ✅ 1️⃣ Class Method
# 🔹 English

# A class method is a method that works with the class itself, not with individual objects.

# 👉 It uses @classmethod decorator.
# 👉 It takes cls as first parameter (instead of self).
# 👉 It can access class variables.

# 🔹 Hindi

# Class method wo method hota hai jo class ke level par kaam karta hai, object ke level par nahi.

# 👉 @classmethod se define hota hai.
# 👉 Pehla parameter cls hota hai.
# 👉 Ye class variable ko access kar sakta hai.

# 🔹 Example
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")

print(Student.school)

# 👉 Yaha cls class ko represent karta hai.

# ✅ 2️⃣ Static Method
# 🔹 English

# A static method is a method that does not depend on class or object.

# 👉 It uses @staticmethod decorator.
# 👉 It does not take self or cls.
# 👉 It behaves like a normal function but inside a class.

# 🔹 Hindi

# Static method wo method hota hai jo na object se related hota hai na class se.

# 👉 @staticmethod se define hota hai.
# 👉 Isme na self hota hai na cls.
# 👉 Ye normal function ki tarah hota hai.

# 🔹 Example
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))

# 👉 Yaha method class ke andar hai, par class data use nahi kar raha.

# 🔥 Difference Table
# Feature	Class Method	Static Method
# Decorator	@classmethod	@staticmethod
# First Parameter	cls	None
# Access Class Variable	Yes	No
# Access Instance Variable	No	No
# Related to	Class	Utility Function
# 🎯 Simple Samjho

# self → Object ke liye

# cls → Class ke liye

# Static → Kisi ke liye nahi 😄

# 🎯 Interview Line

# Class method works with class variables and uses cls.

# Static method does not access class or instance data and works like a normal function inside a class.








# 🔹 English

# A class method works with the class itself.
# It takes cls as the first parameter.
# It can access and modify class variables.

# 🔹 Hindi

# Class method class ke level par kaam karta hai.
# Iska pehla parameter cls hota hai.
# Ye class variable ko access aur modify kar sakta hai.

# 🔹 Example
# class Student:
#     school = "ABC School"

#     @classmethod
#     def change_school(cls, name):
#         cls.school = name

# Student.change_school("XYZ School")
# print(Student.school)

# 👉 Yaha cls class ko represent karta hai.

# ✅ 2️⃣ Static Method
# 🔹 English

# A static method does not depend on class or object.
# It does not take self or cls.
# It behaves like a normal function inside a class.

# 🔹 Hindi

# Static method na object se related hota hai na class data se.
# Isme na self hota hai na cls.
# Ye normal function ki tarah hota hai.