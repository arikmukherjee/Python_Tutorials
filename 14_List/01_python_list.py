mylist = ["apple", "banana", "cherry"]

#Since lists are indexed, lists can have items with the same value.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"] #list of strings
list2 = [1, 5, 7, 9, 3]               #list of integers
list3 = [True, False, False]          #list of booleans

print(list1)
print(list2)
print(list3)

#A list can contain different data types:
list4 = ["abc", 34, True, 40, "male"]
print(list4)

#What is a datatype of a list?
print(type(list4)) #<class 'list'>


#We can also use the list() constructor to make a list.
thislist = list(("apple", "banana", "cherry")) #note the double round
print(thislist)