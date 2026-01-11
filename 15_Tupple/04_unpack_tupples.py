fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Unpacking with Asterisk*
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y) = fruits
print(y) # Output: ['banana', 'cherry', 'mango']

fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y) # Output: ['banana', 'cherry']
