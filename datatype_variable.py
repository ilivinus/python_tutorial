num = 23
print(num)
num = "first string"
print(num)
num = 23.33
print(num)

my_string = "This is not my name"

print(my_string[1]) # this prints element in index 1
print(my_string[5:9]) #this prints element between index 5 and index 9 excluding index 9 element.
"""
This is multiline comment which is also called docstring
"""
print(my_string[4:])# from fourth index to the last index

print("This is the string length ",len(my_string))

print(my_string[4::2])
print(my_string[4:len(my_string):2])

print(my_string[3])