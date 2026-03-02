# what is list comprehension ?

# list comprehension is a short and easy way to create a new list in a single line of code 

list=[1,2,3,4,5]

new_list=[i**2 for i in list]

print(new_list)



# dict comprehension 
# in this have key value pair

dict={1,2,3,4,5}

new_dict={i:i**2 for i in dict}

print (new_dict)
# new_dict.update({5:5})