fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # ['apple', 'banana', 'mango']

# Using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']

# List comprehension syntax:
# newlist = [expression for item in iterable if condition == True]
# The expression is the item itself, a call to a method, or any operation on the item.
# The iterable can be any iterable object, like a list, tuple, set, etc.
# The condition is like a filter that only accepts the items that valuate to True.
# Example 1: Create a new list with the values doubled
numbers = [1, 2, 3, 4, 5]
newlist = [x * 2 for x in numbers]
print(newlist) # [2, 4, 6, 8, 10]
# Example 2: Create a new list with only the even values
numbers = [1, 2, 3, 4, 5]
newlist = [x for x in numbers if x % 2 == 0]
print(newlist) # [2, 4]


newlist = [x.upper() for x in fruits]
print(newlist) # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist = [x for x in fruits if x != "apple"]
print(newlist) # ['banana', 'cherry', 'kiwi', 'mango']
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Example 3: Create a new list with the square of each number
numbers = [1, 2, 3, 4, 5]
newlist = [x**2 for x in numbers]
print(newlist) # [1, 4, 9, 16, 25]
# Example 4: Create a new list with only the numbers greater than 2
numbers = [1, 2, 3, 4, 5]
newlist = [x for x in numbers if x > 2]
print(newlist) # [3, 4, 5]
# Example 5: Create a new list with the first letter of each fruit
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x[0] for x in fruits]
print(newlist) # ['a', 'b', 'c', 'k', 'm']
