#Copy a list using the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']
#You can also use the list() constructor to make a copy
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']

#Copy a list using slicing : operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #['apple', 'banana', 'cherry']

#Copy a list using list comprehension
thislist = ["apple", "banana", "cherry"]
mylist = [item for item in thislist]
print(mylist) #['apple', 'banana', 'cherry']

#Copy a list using the extend() method
thislist = ["apple", "banana", "cherry"]
mylist = []
mylist.extend(thislist)
print(mylist) #['apple', 'banana', 'cherry']
