# What is Decorator in python ?

# Decorator is a function that takes a function as a argument and return a function .

# Example

def Hello():
    print("main function line print ...." )

def wrapper(Hello):
    def fun():
        print("first line print ....")
        Hello()
        print("third line print ....")
    return fun

f=wrapper(Hello)

f()  # calling without decorator (@) simble

# Using decorator simble(@)
@wrapper
def hello1():
    print(" using decorator print line ---")

hello1()    














