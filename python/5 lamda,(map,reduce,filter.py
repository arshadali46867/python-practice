# A lambda function is a small anonymous (nameless) function in Python that is written in a single line using the lambda keyword.

# It can take any number of arguments but can have only one expression.

# 🔹 Syntax
# lambda arguments : expression


square = lambda x: x * x
print(square(5))

sum=lambda x,y : x+y
print(sum(4,5))


1 # map() applies a function to every element of an iterable (like list) and returns a new iterator.
# map() har element par ek function apply karta hai aur nayi list deta hai.
# Syntax:
# map(function, iterable)
# Example:
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)



2 # filter() filters elements based on a condition.
# filter() condition check karta hai aur sirf wahi elements rakhta hai jo condition satisfy kare.

# It keeps only those elements where condition is True.

# Syntax:
# filter(function, iterable)
# Example:
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)



# 3 reduce() use karne ke liye import karna padta hai:

# from functools import reduce

# reduce() applies a function cumulatively to the items of an iterable and reduces them to a single value.
#  It combines elements into one result.

# Syntax:
# reduce(function, iterable)
# Example:
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print(result)