mytuple = ("apple", "banana", "cherry")
print(mytuple) # Output: ('apple', 'banana', 'cherry')
print(type(mytuple)) # Output: <class 'tuple'>

# Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuples can contain different data types
tuple1 = ("apple", 1, True, 3.14)
print(tuple1) # Output: ('apple', 1, True, 3.14)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # Output: 3


# Creating a tuple with one item
# Correct way to create a single-item tuple is to include a comma 
thistuple = ("apple",)
print(type(thistuple)) # Output: <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # Output: <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1) # Output: ('apple', 'banana', 'cherry')
print(tuple2) # Output: (1, 5, 7, 9, 3)
print(tuple3) # Output: (True, False, False)

# Using the tuple() constructor to create a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double parentheses
print(thistuple) # Output: ('apple', 'banana', 'cherry')