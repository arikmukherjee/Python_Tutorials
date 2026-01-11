thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the length of the list when replacing a range of values
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon", "pear"]
print(thislist)

#Replace more than one item with one item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist) #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
thislist[2:5] = ["watermelon"]
print(thislist) #['apple', 'banana', 'watermelon', 'mango']

#Insert items without replacing existing values
thislist = ["apple", "banana", "cherry"]
thislist[1:1] = ["watermelon"]
print(thislist)
#Insert items using the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)