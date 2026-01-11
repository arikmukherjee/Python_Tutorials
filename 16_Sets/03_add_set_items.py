thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'banana', 'orange', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'banana', 'cherry', 'papaya', 'mango', 'apple', 'pineapple'}


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'banana', 'orange', 'cherry', 'kiwi', 'apple'}