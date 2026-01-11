#Append items to the end of the list using the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Extend a list using the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#You can also use the += operator to extend a list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist += tropical
print(thislist)
#Append any iterable object (tuples, sets, dictionaries etc.) using the extend() method
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#Append characters of a string to a list using the extend() method
thislist = ["apple", "banana", "cherry"]
thislist.extend("orange")
print(thislist)
#Append characters of a string to a list using the += operator
thislist = ["apple", "banana", "cherry"]
thislist += "orange"
print(thislist)
