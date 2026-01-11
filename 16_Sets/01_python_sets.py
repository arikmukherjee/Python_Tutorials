myset = {"apple", "banana", "cherry"}
print(myset)
# Output: {'banana', 'cherry', 'apple'}
# Note: The order of elements in a set is not guaranteed.
#A set is a collection which is unordered, unchangeable*, and unindexed.


#No duplicartes allowed.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #Output: {'banana', 'cherry', 'apple'}
#Note: Duplicates will be ignored.
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #Output: {'banana', 'cherry', 'apple', True, 1, 2}
#Note: True is considered as 1 in a set, so it will not be added

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #Output: 3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1) #Output: {'banana', 'cherry', 'apple'}
print(set2) #Output: {1, 3, 5, 7, 9}
print(set3) #Output: {False, True}


#Note: Sets can contain different data types.
set1 = {"abc", 34, True, 40, "male"}
print(set1) #Output: {34, True, 40, 'abc', 'male'}

#type()
print(type(set1)) #Output: <class 'set'>
#Note: Sets are defined by curly brackets {}.
#But do not confuse sets with dictionaries, which also use curly brackets {}.
#Dictionaries have key:value pairs, while sets just have values.

#Creating a set using the set() constructor
thisset = set(("apple", "banana", "cherry")) #Note the double round-brackets
print(thisset) #Output: {'banana', 'cherry', 'apple'}

#Note: The set() constructor can be used to make a set from any iterable object.
#Example: a list, a tuple, a dictionary etc.