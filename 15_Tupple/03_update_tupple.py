x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)# Output: ('apple', 'kiwi', 'cherry')

#1.Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')

# Remove an item: Since tuples are immutable, you cannot remove items from it directly. But you can convert the tuple into a list, remove the item, and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # Output: ('banana', 'cherry')

# Delete the tuple completely: You cannot delete items from a tuple, but you can delete the tuple completely using the del keyword:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) # This will raise an error because the tuple no longer exists