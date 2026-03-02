# A generator is a special type of function that returns an iterator and generates values one by one using the yield keyword instead of return.
# Generator ek special function hota hai jo yield keyword ka use karke values ko ek-ek karke generate karta hai.

def generator():
    i=1
    while i<=20:
        yield i
        i+=1

g=generator()
print(next(g))
print(next(g))
print(next(g))