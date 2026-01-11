thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Output: banana

# Negative indexing
print(thistuple[-1])  # Output: cherry

# Slicing
print(thistuple[0:2])  # Output: ('apple', 'banana')

# Accessing items using a loop
for item in thistuple:
    print(item)
# Output:
# apple
# banana
# cherry

print(thistuple[-1])  # Output: cherry
print(thistuple[-3:-1])  # Output: ('apple', 'banana')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # Output: ('cherry', 'orange', 'kiwi')

print(thistuple[:4]) # Output: ('apple', 'banana', 'cherry', 'orange')

print(thistuple[3:]) # Output: ('orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # Output: ('orange', 'kiwi', 'melon')

# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") # Output: Yes, 'apple' is in the fruits tuple