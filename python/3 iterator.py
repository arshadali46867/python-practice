# iterrator is a object that is enable  you to travserse the collection like list, tuple, dict ....  (Iterator ek object hota hai jo hume collection (jaise list, tuple, dictionary, etc.) ke elements ko ek-ek karke dekhne ya access karne ki suvidha deta hai)
# type - 1 iter, 2 next (__iter__ , __next__)
# __iter__ return iterator object itself
# __next__ return next value of the collection

# if the collection of list will empty then it will raise error

list=[1,2,3,4,5]
iter_value=iter(list)
print(next(iter_value))
print(next(iter_value))

