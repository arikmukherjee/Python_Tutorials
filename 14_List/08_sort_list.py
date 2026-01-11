# Sort List Alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort List Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

# Sort List in Descending Order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist) # [100, 82, 65, 50, 23]

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist) # [50, 65, 23, 82, 100]

# Case Sensitive Sort
# Uppercase letters come before lowercase letters in ASCII values. So in case of a mix of uppercase and lowercase letters, uppercase letters will be listed first , then lowercase letters.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order of List Elements
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.reverse()
print(thislist) # [23, 82, 65, 50, 100]