#remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # {'cherry', 'apple'}

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # {'cherry', 'apple'}

#pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # could be 'apple', 'banana', or 'cherry'
print(thisset) # {'banana', 'cherry'} (or similar, since sets are unordered)

#clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()

#del
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # This would raise a NameError since 'thisset' is deleted