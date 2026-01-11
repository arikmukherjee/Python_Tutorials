#Remove an item by value using the remove() method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Remove an item by index using the pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']
#If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']
#Remove an item by index using the del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']
#The del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #this will raise an error because the list no longer exists

#Clear the list using the clear() method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]
#You can also clear a list by assigning an empty list to it
thislist = ["apple", "banana", "cherry"]
thislist = []
print(thislist) #[]