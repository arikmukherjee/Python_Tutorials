set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # Output: {'a', 1, 2, 3, 'b', 'c'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 # Using the '|' operator instead of union() method
print(set3) # Output: {'a', 1, 2, 3, 'b', 'c'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset) # Output: {'a', 1, 2, 3, 'b', 'c', 'John', 'Elena', 'apple', 'bananas', 'cherry'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset) # Output: {'a', 1, 2, 3, 'b', 'c', 'John', 'Elena', 'apple', 'bananas', 'cherry'}

# Joining a set with a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z) # Output: {'a', 1, 2, 3, 'b', 'c'}

#update() method to join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # Output: {'a', 1, 2, 3, 'b', 'c'}

#intersection() method to get the common elements between two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # Output: {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 # Using '&' operator instead of intersection() method
print(set3) # Output: {'apple'}

#intersection_update() method to remove the elements that are not common between two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) # Output: {'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3) # Output: {1, 'apple'}

#difference() method to get the difference between two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) # Output: {'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 # Using '-' operator instead of difference() method
print(set3) # Output: {'banana', 'cherry'}

#difference_update() method to remove the elements found in another set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) # Output: {'banana', 'cherry'}

#symmetric_difference() method to get the elements that are not common between two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # Output: {'banana', 'cherry', 'google', 'microsoft'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 # Using '^' operator instead of symmetric_difference() method
print(set3) # Output: {'banana', 'cherry', 'google', 'microsoft'}

#symmetric_difference_update() method to remove the elements that are common between two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1) # Output: {'banana', 'cherry', 'google', 'microsoft'}