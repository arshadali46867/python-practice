# Instance Variables kya hoti hain? (Hindi)

# Instance variables wo variables hote hain jo object ke andar store hote hain.

#  Har object ke paas apni alag copy hoti hai.
#  Inhe self ke through define kiya jata hai.


class Car:
    def __init__(self, brand):
        self.brand = brand   # instance variable

c1 = Car("Toyota")
c2 = Car("Honda")

print(c1.brand)  # Toyota
print(c2.brand)  # Honda